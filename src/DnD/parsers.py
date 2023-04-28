import asyncio
import json
import logging
import os
import re
from typing import Any, Coroutine, Dict, List, Optional, Tuple

import aiohttp
from bs4 import BeautifulSoup
from DnD.config import Parser
from DnD.consts import (BESTIARY_HTML_CONST, FEATS_HTML_CONST,
                        ITEM_HTML_CONST, SPELL_HTML_CONST)


class BaseParser():
    def __init__(self, config: Parser) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.HTML_CONST = ""

        self.max_concurence = config.max_concurence
        self.max_retries = config.max_retries
        self.base_path = os.path.join(os.getcwd(), config.base_path)

        self.aiohttp_session = aiohttp.ClientSession(headers=config.headers)

        if config.proxy:
            from fp.fp import FreeProxy
            self.proxy = FreeProxy(timeout=1, https=True).get(
                repeat=True)
        else:
            self.proxy = None

    async def get_page_html(self, page_url: str) -> Optional[str]:
        try:
            async with self.aiohttp_session.get(
                    url=page_url,
                    proxy=self.proxy,
                    allow_redirects=False) as response:

                if response.status == 200:
                    return await response.text()
                return None

        except aiohttp.ClientError:
            return None

    async def try_n_times(self,
                          func: Coroutine[Any, Any, Any],
                          *args: Any, **kwargs: Any) -> Any:

        for _ in range(self.max_retries):
            response = await func(*args, **kwargs)  # type: ignore

            if response is not None:
                return response                     # type: ignore

        return None

    async def scrap_main_page_info(self, html: str) -> Dict[str, str]:
        soup = BeautifulSoup(html, "lxml")

        # Find and format cards filter info
        script_tag_text = soup.find(
            "script", string=re.compile("window.filterItems")).get_text()
        formatted_script_text = script_tag_text.replace(
            "window.filterItems = ", "").replace(';', "")
        json_data = json.loads(formatted_script_text)

        cards = soup.find("div", class_="list").find_all(
            "div", {"data-id": True})

        # Add links to cards
        for card in cards:
            json_data[card['data-id']].update(
                {"link": str(card.a["href"])})

        return json_data

    async def get_card_info(
            self, card: Dict[Any, Any]) -> Tuple[Dict[Any, Any], str]:

        card_link = "https://dnd.su" + str(card["link"].replace("\\", ""))
        card_html = await self.try_n_times(self.get_page_html,
                                           page_url=card_link)

        if not card_html:
            self.logger.warn(
                f"Can't scrap card - {card_link}")
            return (card, self.HTML_CONST)

        self.logger.debug(f"{card_link} --- DONE")
        return (card, card_html)

    async def get_cards_info(
            self, data: Dict[str, str]) -> List[Tuple[Dict[Any, Any], str]]:

        semaphore = asyncio.Semaphore(self.max_concurence)
        tasks = asyncio.Queue()
        combined_data_list = []

        for card in list(data.values()):
            await tasks.put(card)

        # Create worker for parsing detailed info
        async def fetch_worker():
            while not tasks.empty():
                card = await tasks.get()
                async with semaphore:
                    result = await self.get_card_info(card)
                    combined_data_list.append(result)

        # Run some workers
        workers = [fetch_worker() for _ in range(self.max_concurence)]
        await asyncio.gather(*workers)

        return combined_data_list

    async def save_json_html_data(
        self,
            combined_data_list: List[Tuple[Dict[Any, Any], str]]) -> None:

        os.makedirs(self.base_path, exist_ok=True)

        for i, card in enumerate(combined_data_list):
            card_path = os.path.join(self.base_path, str(i))

            with open(f"{card_path}.json", 'w', encoding="utf-8") as file:
                json.dump(card[0], file, indent=4)

            with open(f"{card_path}.html", "w", encoding="utf-8") as file:
                file.write(card[1])


class SpellsParser(BaseParser):
    def __init__(self, config: Parser) -> None:
        super().__init__(config)
        self.base_path = os.path.join(self.base_path, "spells", "add_data")
        self.HTML_CONST = SPELL_HTML_CONST

    async def scrap_main_page_info(self, html: str) -> Dict[str, str]:
        soup = BeautifulSoup(html, "lxml")

        # Find and format spells filter info
        script_tag_text = soup.find(
            "script", string=re.compile("window.LIST")).get_text()
        formatted_script_text = script_tag_text.replace(
            "window.LIST = ", "").replace(';', "")
        json_data = json.loads(formatted_script_text)

        return json_data

    async def get_cards_info(
            self, data: Dict[str, str]) -> List[Tuple[Dict[Any, Any], str]]:

        semaphore = asyncio.Semaphore(self.max_concurence)
        tasks = asyncio.Queue()
        combined_data_list = []

        for card in data["cards"]:
            await tasks.put(card)

        # Create worker for parsing detailed info
        async def fetch_worker():
            while not tasks.empty():
                card = await tasks.get()
                async with semaphore:
                    result = await self.get_card_info(card)
                    combined_data_list.append(result)

        # Run some workers
        workers = [fetch_worker() for _ in range(self.max_concurence)]
        await asyncio.gather(*workers)

        return combined_data_list


class ItemsParser(BaseParser):
    def __init__(self, config: Parser) -> None:
        super().__init__(config)
        self.base_path = os.path.join(self.base_path, "items", "add_data")
        self.HTML_CONST = ITEM_HTML_CONST


class BestiaryParser(BaseParser):
    def __init__(self, config: Parser) -> None:
        super().__init__(config)
        self.base_path = os.path.join(self.base_path, "bestiary", "add_data")
        self.HTML_CONST = BESTIARY_HTML_CONST


class FeatsParser(BaseParser):
    def __init__(self, config: Parser) -> None:
        super().__init__(config)
        self.base_path = os.path.join(self.base_path, "feats", "add_data")
        self.HTML_CONST = FEATS_HTML_CONST
