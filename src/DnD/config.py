import configparser
from dataclasses import dataclass
import json
import logging.config
from typing import Dict


@dataclass
class Parser:
    base_path: str
    max_retries: int
    max_concurence: int
    proxy: bool
    headers: Dict[str, str]


@dataclass
class Formatter:
    base_path: str
    is_remove_files: bool


@dataclass
class Config:
    parser: Parser
    formatter: Formatter


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    return Config(
        Parser(
            base_path=config["main"].get("base-path"),
            max_retries=config["parser"].getint("max-retries"),
            max_concurence=config["parser"].getint("max-concurence"),
            proxy=config["parser"].getboolean("is-proxy"),
            headers={**config["headers"]},
        ),
        Formatter(
            base_path=config["main"].get("base-path"),
            is_remove_files=config["formatter"].getboolean(
                "is-remove-additional-files")),
    )


def load_logging_configs(path: str):
    with open(path, "r") as f:
        config = json.load(f)

    logging.config.dictConfig(config)
