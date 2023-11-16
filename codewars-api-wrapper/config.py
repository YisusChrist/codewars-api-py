"""Configuration module for the project."""
import configparser
from argparse import Namespace
from pathlib import Path
from typing import Tuple

from rich import print

from .consts import CONFIG_FILE
from .logs import logger


def create_config_file() -> None:
    """
    Create the configuration file.
    """
    logger.debug("Creating configuration file at %s", CONFIG_FILE)

    config = configparser.ConfigParser()

    config.add_section("Paths")

    default_src_path = "D:\\3D Objects\\instagram"
    default_dest_path = "D:\\3D Objects\\move"

    src_path = input(f"Enter the source path (default: {default_src_path}): ")
    dest_path = input(f"Enter the destination path (default: {default_dest_path}): ")

    config.set("Paths", "src_path", src_path or default_src_path)
    config.set("Paths", "dest_path", dest_path or default_dest_path)

    with open(CONFIG_FILE, "w", encoding="utf-8") as config_file:
        config.write(config_file)


def configure_paths(args: Namespace) -> Tuple[Path, Path]:
    """
    Get the source and destination path values from the configuration file or
    the command-line arguments.

    Args:
        args (Namespace): The parsed command-line arguments.

    Returns:
        Tuple[Path, Path]: The source and destination path values.
    """
    logger.debug("Configuring paths")
    if not CONFIG_FILE.is_file():
        # Configuration file doesn't exist, prompt the user for values and create the file
        # Warn the user that the configuration file doesn't exist
        print(
            "[yellow]Configuration file doesn't exist. "
            f"Creating configuration file at {CONFIG_FILE}[/yellow]"
        )
        create_config_file()

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    if args.source_path is None:
        args.source_path = config.get("Paths", "src_path")

    if args.dest_path is None:
        args.dest_path = config.get("Paths", "dest_path")

    src_path = Path(args.source_path).resolve()
    dest_path = Path(args.dest_path).resolve()

    return src_path, dest_path
