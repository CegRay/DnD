import glob
import json
import logging
import os
import re
from typing import Any, Dict, List


from bs4 import BeautifulSoup
from DnD.config import Formatter
from DnD.consts import (FILTER_TO_ABILITY, FILTER_TO_ALINGMENT,
                        FILTER_TO_OTHER, FILTER_TO_PROFIENCY,
                        FILTER_TO_REQUIRE, FILTER_TO_SKILL,
                        FILTERID_TO_ARCHETYPE, FILTERID_TO_CLASS,
                        FILTERID_TO_LANGUAGE, FILTERID_TO_QUALITY,
                        FILTERID_TO_SET, FILTERID_TO_SIZE,
                        FILTERID_TO_SOURCE, FILTERID_TO_TYPE)
from DnD.utils import Dumper
import markdownify
import yaml


class BaseFormatter():
    def __init__(self, config: Formatter) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.base_path = os.path.join(os.getcwd(), config.base_path)
        self.is_remove_files = config.is_remove_files

    async def get_head_data(self, filepath: str):
        with open(filepath, "r") as file:
            return json.load(file)

    async def get_body_data(self, filepath: str) -> bytes:
        with open(filepath, "rb") as html:
            return html.read()

    async def remove_additional_data(self, data_dir: str) -> None:
        from shutil import rmtree
        rmtree(os.path.join(self.base_path, data_dir))

    async def get_yaml_head(self, filespath: str) -> Dict[str, Any]:
        head_data = await self.get_head_data(f"{filespath}.json")

        md_source = [
            FILTERID_TO_SOURCE[int(i)]
            for i in head_data["source"]]

        return {
            "source": md_source}

    async def save_yaml_head(self, filespath: str, filename: str) -> None:
        yaml_head = await self.get_yaml_head(filespath)
        filepath = os.path.join(self.base_path, "mds", f"{filename}.md")

        with open(filepath, "w", encoding="utf-8") as md_file:
            md_file.write("---\n")
            yaml.dump(yaml_head, md_file,
                      sort_keys=False, allow_unicode=True,
                      default_flow_style=False, Dumper=Dumper)
            md_file.write("---")

    async def get_formatted_stats(self, stat_li: Any) -> str:
        # Make table with 2 rows os stats
        stat_row_1, stat_row_2 = "", ""
        for stat in stat_li.find_all("div", class_="stat", recursive=False):
            divs = stat.find_all("div", recursive=False)
            stat_row_1 += f"<td>{divs[0]}</td>"
            stat_row_2 += f"<td>{divs[1]}</td>"

        return f"<table><tr>{stat_row_1}</tr><tr>{stat_row_2}</tr></table>"

    async def get_formatted_body_data(self, body_data: bytes):
        md_name = "# " + \
            BeautifulSoup(body_data, "lxml").find(itemprop="url").text

        params_lis = list(BeautifulSoup(body_data, "lxml").find(
            "ul", class_="params").find_all(recursive=False))

        formatted_str = ""
        for li in params_lis:
            if li.get("class") == ["stats"]:
                subbed_str = await self.get_formatted_stats(li)

            elif li.get("class") == ["subsection", "desc"]:
                description = li.find("div", recursive=False)

                # Replace all \n and \r in td tags before closing td tag
                subbed_str = re.sub(
                    r'(?<=<td>)(.*?)(?:\r\n|\n|\r)(?=.*?</td>)',
                    lambda match: match.group(1).replace(
                        '\n', ' ').replace('\r', ' '),
                    "\n" + str(description))

            else:
                # Replace li tags for more beautiful syntax in md
                subbed_str = re.sub(r"<li.*?>(.*?)<\/li>",
                                    r"\1<br/>", str(li))

            formatted_str += markdownify.markdownify(subbed_str)

        return f"\n\n{md_name}\n\n{formatted_str}"

    async def get_md_body(self, filespath: str) -> str:
        body_data = await self.get_body_data(f"{filespath}.html")
        formatted_body_data = await self.get_formatted_body_data(body_data)

        return formatted_body_data

    async def create_md_data_list(self) -> List[str]:
        md_data_list = []
        save_path = os.path.join(self.base_path, "mds")
        os.makedirs(save_path, exist_ok=True)

        for filepath in glob.glob(os.path.join(
                self.base_path, "add_data", "*.html")):

            filespath = filepath.split(".")[0]
            filename = os.path.basename(filespath)

            await self.save_yaml_head(filespath, filename)

            md_data_list.append((filename, await self.get_md_body(filespath)))
            self.logger.debug(f"{filename} --- ADDED")

        return md_data_list

    async def save_to_md(self, md_list: List[str]):
        save_path = os.path.join(self.base_path, "mds")

        for filename, md_data in md_list:
            file_save_path = os.path.join(save_path, f"{filename}.md")

            with open(file_save_path, "a", encoding="utf-8") as md_file:
                md_file.write(md_data)

        if self.is_remove_files:
            await self.remove_additional_data("add_data")


class SpellsFormatter(BaseFormatter):
    def __init__(self, config: Formatter) -> None:
        super().__init__(config)
        self.base_path = os.path.join(self.base_path, "spells")

    async def get_yaml_head(self, filespath: str) -> Dict[str, Any]:
        head_data = await self.get_head_data(f"{filespath}.json")

        md_title = head_data["title"].replace(r"\/", " ")
        md_title_en = head_data["title_en"].replace(r"\/", " ")

        md_classes = [
            FILTERID_TO_CLASS[int(i)]
            for i in
            head_data["filter_class"] + head_data["filter_class_tce"]]

        md_source = [
            FILTERID_TO_SOURCE[int(i)]
            for i in head_data["filter_source"]]

        md_archetypes = [
            FILTERID_TO_ARCHETYPE[int(i)]
            for i in head_data["filter_archetype"]]

        return {
            "name": md_title,
            "name_en": md_title_en,
            "level": head_data["level"],
            "spell_school": head_data["school"],
            "spell_classes": md_classes,
            "spell_archetypes": md_archetypes,
            "spell_source": md_source}


class ItemsFormatter(BaseFormatter):
    def __init__(self, config: Formatter) -> None:
        super().__init__(config)
        self.base_path = os.path.join(self.base_path, "items")

    async def get_yaml_head(self, filespath: str) -> Dict[str, Any]:
        head_data = await self.get_head_data(f"{filespath}.json")

        md_type = [
            FILTERID_TO_TYPE[int(i)]
            for i in head_data["type"]]

        md_quality = [
            FILTERID_TO_QUALITY[int(i)]
            for i in head_data["quality"]]

        md_set = [
            FILTERID_TO_SET[int(i)]
            for i in head_data["set"]]

        md_source = [
            FILTERID_TO_SOURCE[int(i)]
            for i in head_data["source"]]

        return {
            "item_type": md_type,
            "item_quality": md_quality,
            "item_set": md_set,
            "item_source": md_source}


class BestiaryFormatter(BaseFormatter):
    def __init__(self, config: Formatter) -> None:
        super().__init__(config)
        self.base_path = os.path.join(self.base_path, "bestiary")

    async def get_yaml_head(self, filespath: str) -> Dict[str, Any]:
        head_data = await self.get_head_data(f"{filespath}.json")

        md_size = [
            FILTERID_TO_SIZE[int(i)]
            for i in head_data["size"]]

        md_type = [
            FILTERID_TO_TYPE[int(i)]
            for i in head_data["type"]]

        md_alignment = [
            FILTER_TO_ALINGMENT[i]
            for i in head_data["alignment"]]

        md_language = []
        # Some languages are "", some have id~distance~comment syntax
        for language in head_data["languages"]:
            if language == "":
                continue

            try:
                md_language.append(FILTERID_TO_LANGUAGE[int(language)])
            except ValueError:
                # 1 language have just comment without ~
                if "~" in language:
                    md_language.append(
                        FILTERID_TO_LANGUAGE[int(language.split("~")[0])])

        md_source = [
            FILTERID_TO_SOURCE[int(i)]
            for i in head_data["source"]]

        return {
            "bestiary_size": md_size,
            "bestiary_type": md_type,
            "bestiary_alignment": md_alignment,
            "bestiary_language": md_language,
            "bestiary_source": md_source}


class FeatsFormatter(BaseFormatter):
    def __init__(self, config: Formatter) -> None:
        super().__init__(config)
        self.base_path = os.path.join(self.base_path, "feats")

    async def get_yaml_head(self, filespath: str) -> Dict[str, Any]:
        head_data = await self.get_head_data(f"{filespath}.json")

        md_source = [
            FILTERID_TO_SOURCE[int(i)]
            for i in head_data["source"]]

        md_abilities = [
            FILTER_TO_ABILITY[i]
            for i in head_data["abilities"]]

        md_proficiency = [
            FILTER_TO_PROFIENCY[i]
            for i in head_data["proficiency"]]

        md_requires = [
            FILTER_TO_REQUIRE[i]
            for i in head_data["requires"]]

        md_skills = [
            FILTER_TO_SKILL[i]
            for i in head_data["skills"]]

        md_other = [
            FILTER_TO_OTHER[i]
            for i in head_data["other"]]

        return {
            "feat_source": md_source,
            "feat_abilities": md_abilities,
            "feat_proficiency": md_proficiency,
            "feat_requires": md_requires,
            "feat_skills": md_skills,
            "feat_other": md_other,

        }
