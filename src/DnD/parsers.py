import json
import logging
import re
from typing import Dict, Optional

import aiohttp
from bs4 import BeautifulSoup
from celery import Celery
from DnD import celeryconfig
from DnD.config import Config
from fp.fp import FreeProxy


class BaseParser():
    def __init__(self, config: Config) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.main_page_url = ""
        # self.proxy = FreeProxy(timeout=1, https=True).get(
        #     repeat=True) if config.proxy else None
        self.aiohttp_session = aiohttp.ClientSession(headers=config.headers)
        self.celery_app = Celery(self.__class__.__name__)

    async def get_main_page_html(self) -> Optional[str]:
        try:
            async with self.aiohttp_session.get(
                    self.main_page_url,
                    proxy=self.proxy,
                    allow_redirects=False) as response:

                if response.status == 200:
                    return await response.text()
                return None

        except aiohttp.ClientError as ex:
            self.logger.error(f"MAIN page request: {ex}")
            return None


class SpellsParser(BaseParser):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.main_page_url = "https://dnd.su/spells/"

    async def get_main_page_info(self, html: str) -> Dict[str, str]:
        soup = BeautifulSoup(html, "lxml")
        script_tag_text = soup.find(
            "script", string=re.compile("window.LIST")).get_text()
        formatted_script_text = script_tag_text.replace(
            "window.LIST = ", "").replace(';', "")
        json_data = json.loads(formatted_script_text)

        return json_data

    async def get_detailed_info(self, data: Dict[str, str]) -> None:
        self.celery_app.config_from_object(celeryconfig)
        print(
            self.celery_app.task(self.get_detailed_info, data=data))


class ItemsParser(BaseParser):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.main_page_url = "https://dnd.su/items/"
