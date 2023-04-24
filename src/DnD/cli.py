import asyncio
import logging
import time
from typing import Any, Coroutine


from DnD.config import Config, load_config
from DnD.formatters import (
    BestiaryFormatter, FeatsFormatter, ItemsFormatter, SpellsFormatter)
from DnD.main import (format_catalogs, scrap_catalogs)
from DnD.parsers import (BestiaryParser, FeatsParser,
                         ItemsParser, SpellsParser)


logger = logging.getLogger("main")


async def run_scrap(config: Config):
    logger.info("Starting parsers")

    await scrap_catalogs(SpellsParser(config),
                         "spells", "https://dnd.su/spells/")
    await scrap_catalogs(ItemsParser(config),
                         "items", "https://dnd.su/items/")
    await scrap_catalogs(BestiaryParser(config),
                         "bestiary", "https://dnd.su/bestiary/")
    await scrap_catalogs(FeatsParser(config),
                         "feats", "https://dnd.su/feats/")

    logger.info("Parsers have done their work")


async def run_format(config: Config):
    logger.info("Starting formatters")

    await format_catalogs(
        SpellsFormatter(config.base_path, config.is_remove_files), "spells")
    await format_catalogs(
        ItemsFormatter(config.base_path, config.is_remove_files), "items")
    await format_catalogs(
        BestiaryFormatter(config.base_path, config.is_remove_files), "bestiary")  # noqa: E501
    await format_catalogs(
        FeatsFormatter(config.base_path, config.is_remove_files), "feats")

    logger.info("Formatters have done their work")


async def main(func: Coroutine[Any, Any, None]):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    logger.info("Loading configs...")
    config = load_config("./config.ini")
    logger.info("Configs loaded")

    await func(config)


def cli_scrap():
    """Wrapp for command line."""
    try:
        start_time = time.time()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(run_scrap))
        end_time = time.time()

        logger.info(
            f"Working time: {(end_time - start_time):.5f}")
    except (KeyboardInterrupt, SystemExit):
        logger.error("Parsing stopped!")


def cli_save():
    """Wrapp for command line."""
    try:
        start_time = time.time()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(run_format))
        end_time = time.time()

        logger.info(
            f"Working time: {(end_time - start_time):.5f}")
    except (KeyboardInterrupt, SystemExit):
        logger.error("Formatting stopped!")
