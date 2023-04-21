import logging

from DnD.formatters import SpellsFormatter
from DnD.parsers import SpellsParser


async def format_spells(formatter: SpellsFormatter):
    logger = logging.getLogger("Spells formatter")
    logger.info("Start spells formatting")

    # Format and save md
    md_data_list = await formatter.create_md_data_list()
    await formatter.save_to_md(md_data_list)


async def scrap_spells(parser: SpellsParser):
    logger = logging.getLogger("Spells parser")
    logger.info("Start spells parsing")

    html = await parser.get_page_html(page_url="https://dnd.su/spells/")
    if not html:
        await parser.aiohttp_session.close()
        logger.error("Can't scrap spells - no HTML")
        return None

    json_data = await parser.scrap_main_page_info(html)
    detailed_data_list = await parser.get_spells_info(json_data)

    await parser.save_json_html_data(detailed_data_list)
    await parser.aiohttp_session.close()
