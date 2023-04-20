import asyncio
import logging
import time

from DnD.config import Config, load_config
from DnD.formatters import SpellsFormatter
from DnD.parsers import SpellsParser


logger = logging.getLogger("main")


async def scrap_spells(config: Config, parser: SpellsParser):
    html = await parser.get_page_html(page_url="https://dnd.su/spells/")
    if not html:
        await parser.aiohttp_session.close()
        logger.error("Can't scrap spells - no HTML")
        return None

    json_data = await parser.scrap_main_page_info(html)
    detailed_data_list = await parser.get_spells_info(json_data)

    await parser.save_json_html_data(detailed_data_list)
    await parser.aiohttp_session.close()

    # Format and save md
    formatter = SpellsFormatter(config.base_path)

    md_data_list = await formatter.create_md_data_list()
    await formatter.save_to_md(md_data_list, remove_files=False)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting crawler")

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
        logger.error("Crawler stopped!")


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
        logger.error("Crawler stopped!")
