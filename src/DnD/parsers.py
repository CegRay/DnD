import asyncio
import json
import logging
import os
import re
from typing import Any, Dict, List, Optional, Tuple

import aiohttp
from bs4 import BeautifulSoup
from DnD.config import Config
from DnD.consts import SPELL_HTML_CONST


class BaseParser():
    def __init__(self, config: Config) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.main_page_url = ""
        self.aiohttp_session = aiohttp.ClientSession(headers=config.headers)
        self.max_concurence = config.max_concurence
        self.base_path = os.path.join(os.getcwd(), config.base_path)
        if config.proxy:
            from fp.fp import FreeProxy
            self.proxy = FreeProxy(timeout=1, https=True).get(
                repeat=True)

    async def get_page_html(self, page_url: str) -> Optional[str]:
        try:
            async with self.aiohttp_session.get(
                    url=page_url,
                    proxy=self.proxy,
                    allow_redirects=False) as response:

                if response.status == 200:
                    return await response.text()
                return None

        except aiohttp.ClientError as ex:
            self.logger.error(f"Page request {page_url}:\n {ex}")
            return None


class SpellsParser(BaseParser):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.base_path = os.path.join(self.base_path, "spells", "add_data")

    async def scrap_main_page_info(self, html: str) -> Dict[str, str]:
        soup = BeautifulSoup(html, "lxml")

        # Find and format spells filter info
        script_tag_text = soup.find(
            "script", string=re.compile("window.LIST")).get_text()
        formatted_script_text = script_tag_text.replace(
            "window.LIST = ", "").replace(';', "")
        json_data = json.loads(formatted_script_text)

        return json_data

    async def get_spell_info(
            self, card: Dict[Any, Any]) -> Tuple[Dict[Any, Any], str]:

        card_link = "https://dnd.su" + str(card["link"].replace("\\", ""))
        card_html = await self.get_page_html(page_url=card_link)

        if not card_html:
            self.logger.info(
                f"Can't scrap spell - {card_link}")
            return (card, SPELL_HTML_CONST)

        self.logger.info(f"{card_link} --- DONE")
        return (card, card_html)

    async def get_spells_info(
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
                    result = await self.get_spell_info(card)
                    combined_data_list.append(result)

        # Run some workers
        workers = [fetch_worker() for _ in range(self.max_concurence)]
        await asyncio.gather(*workers)

        return combined_data_list

    async def save_json_html_data(
        self,
            combined_data_list: List[Tuple[Dict[Any, Any], str]]) -> None:

        os.makedirs(self.base_path, exist_ok=True)

        for i, spell in enumerate(combined_data_list):
            spell_path = os.path.join(self.base_path, str(i))

            with open(f"{spell_path}.json", 'w', encoding="utf-8") as file:
                json.dump(spell[0], file, indent=4)

            with open(f"{spell_path}.html", "w", encoding="utf-8") as file:
                file.write(spell[1])
