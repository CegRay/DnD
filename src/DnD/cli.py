import asyncio
import logging
import time

from celery import Celery
from DnD.config import Config, load_config
from DnD.parsers import ItemsParser, SpellsParser

logger = logging.getLogger("main")


async def scrap_spells(config: Config, parser: SpellsParser):
    # html = await parser.get_main_page_html()
    # if not html:
    #     await parser.aiohttp_session.close()
    #     return None

    # json_data = await parser.get_main_page_info(html)
    await parser.get_detailed_info({"", ""})
    await parser.aiohttp_session.close()

# async def scrap_items(config: Config):
#     parser = ItemsParser(config)
#     main_html = await parser.get_main_html()
#     logger.info(str(main_html))


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot")

    config = load_config("./config.ini")

    await scrap_spells(config, SpellsParser(config))


def cli():
    """Wrapp for command line."""
    try:
        start_time = time.time()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        end_time = time.time()

        logger.info(
            f"Working time: {(end_time - start_time):.5f}")
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")


def dev():
    """Wrapp for command line."""
    try:
        start_time = time.time()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        end_time = time.time()

        logger.info(
            f"Working time: {(end_time - start_time):.5f}")
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
