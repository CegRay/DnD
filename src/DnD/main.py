import logging
from typing import Union

from DnD.formatters import (BestiaryFormatter, FeatsFormatter,
                            ItemsFormatter, SpellsFormatter)
from DnD.parsers import (BestiaryParser, FeatsParser,
                         ItemsParser, SpellsParser)


async def scrap_catalogs(parser: Union[SpellsParser, ItemsParser,
                                       BestiaryParser, FeatsParser],
                         catalog_name: str,
                         catalog_url: str):

    logger = logging.getLogger(f"{catalog_name.capitalize()} parser")
    logger.info(f"Start {catalog_name} parsing")

    html = await parser.get_page_html(page_url=catalog_url)
    if not html:
        await parser.aiohttp_session.close()
        logger.error(f"Can't scrap {catalog_name} - no HTML")
        return None

    json_data = await parser.scrap_main_page_info(html)
    detailed_data_list = await parser.get_cards_info(json_data)

    await parser.save_json_html_data(detailed_data_list)
    await parser.aiohttp_session.close()

    logger.info(f"{catalog_name.capitalize()} parsing DONE")


async def format_catalogs(formatter: Union[SpellsFormatter, ItemsFormatter,
                                           BestiaryFormatter, FeatsFormatter],
                          catalog_name: str):
    logger = logging.getLogger(f"{catalog_name.capitalize()} formatter")
    logger.info(f"Start {catalog_name} formatting")

    # Format and save md
    md_data_list = await formatter.create_md_data_list()
    await formatter.save_to_md(md_data_list)

    logger.info(f"{catalog_name.capitalize()} formatting DONE")
