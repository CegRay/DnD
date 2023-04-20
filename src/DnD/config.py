import configparser
from dataclasses import dataclass
from typing import Dict


@dataclass
class Config:
    headers: Dict[str, str]
    proxy: bool
    max_concurence: int
    base_path: str


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    return Config(
        headers={**config["headers"]},
        proxy=config["parser"].getboolean("is_proxy"),
        max_concurence=config["parser"].getint("max-concurence"),
        base_path=config["parser"].get("base-path"),
    )
