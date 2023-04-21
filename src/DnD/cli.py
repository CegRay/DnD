import asyncio
import logging
import time
from typing import Any, Coroutine


from DnD.config import Config, load_config
from DnD.formatters import SpellsFormatter
from DnD.main import (format_spells, scrap_spells)
from DnD.parsers import SpellsParser


logger = logging.getLogger("main")


async def run_scrap(config: Config):
    logger.info("Starting parsers")

    await scrap_spells(SpellsParser(config))

    logger.info("Parsers have done their work")


async def run_format(config: Config):
    logger.info("Starting formatters")

    await format_spells(SpellsFormatter(
        config.base_path, config.is_remove_files))

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
