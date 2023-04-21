import glob
import json
import logging
import os
import re
from typing import Dict, List

from bs4 import BeautifulSoup
from DnD.consts import (FILTERID_TO_ARCHETYPE,
                        FILTERID_TO_CLASS, FILTERID_TO_SOURCE)
import yaml


class BaseFormatter():
    def __init__(self, base_path: str, is_remove_data: bool) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.base_path = os.path.join(os.getcwd(), base_path)
        self.is_remove_files = is_remove_data

    async def get_head_data(self, filepath: str):
        with open(filepath, "r") as file:
            return json.load(file)

    async def get_body_data(self, filepath: str):
        with open(filepath, "rb") as html:
            return html.read()

    async def remove_additional_data(self, data_dir: str) -> None:
        from shutil import rmtree
        rmtree(os.path.join(self.base_path, data_dir))

    async def save_to_md(self, md_list: List[str]):
        save_path = os.path.join(self.base_path, "mds")
        os.makedirs(save_path, exist_ok=True)

        for filename, md_data in md_list:
            file_save_path = os.path.join(save_path, f"{filename}.md")

            with open(file_save_path, "a", encoding="utf-8") as md_file:
                md_file.write(md_data)

        if self.is_remove_files:
            await self.remove_additional_data("add_data")


class SpellsFormatter(BaseFormatter):
    def __init__(self, base_path: str, is_remove_data: bool) -> None:
        super().__init__(base_path, is_remove_data)
        self.base_path = os.path.join(self.base_path, "spells")

    async def get_yaml_head(self, filespath: str) -> Dict:
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
            "level": int(head_data["level"]),
            "spell_school": head_data["school"],
            "spell_classes": md_classes,
            "spell_archetypes": md_archetypes,
            "spell_source": md_source}

    async def save_yaml_head(self, filespath: str, filename: str) -> None:
        yaml_head = await self.get_yaml_head(filespath)
        filepath = os.path.join(self.base_path, "mds", f"{filename}.md")

        with open(filepath, "w", encoding="utf-8") as md_file:
            md_file.write("---\n\n")
            yaml.dump(yaml_head, md_file,
                      sort_keys=False, allow_unicode=True)
            md_file.write("\n---")

    async def get_md_body(self, filespath: str) -> str:
        body_data = await self.get_body_data(f"{filespath}.html")

        params_ul = BeautifulSoup(body_data, "lxml").find(
            "ul", class_="params").findAll("li")

        md_name = "# " + \
            BeautifulSoup(body_data, "lxml").find(itemprop="url").text
        md_prefix_title = f"_{params_ul[0].text}_"
        md_body = ""

        for i in params_ul[1:]:
            # Replace all <strong> tags to **
            formatted_param = re.sub(
                r"<strong>(.*?)</strong>", r"**\1**", str(i))
            # Replace all <em> tags to _
            formatted_param = re.sub(
                r"<em>(.*?)</em>", r"_\1_", formatted_param)
            # Replace all <p> tags to markdown paragraph format
            formatted_param = re.sub(
                r"<p>(.*?)</p>", r"\n\1", formatted_param)
            # Remove other html tags
            formatted_param = re.sub(r"<.*?>", "", formatted_param)

            md_body += "  \n" + formatted_param

        return f"\n\n{md_name}\n\n{md_prefix_title}{md_body}"

    async def create_md_data_list(self) -> List[str]:
        md_data_list = []

        for filepath in glob.glob(os.path.join(
                self.base_path, "add_data", "*.html")):
            filespath = filepath.split(".")[0]
            filename = os.path.basename(filespath)

            await self.save_yaml_head(filespath, filename)

            md_data_list.append((filename, await self.get_md_body(filespath)))

        return md_data_list
