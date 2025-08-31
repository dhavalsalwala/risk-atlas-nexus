import subprocess
import sys

from risk_atlas_nexus.toolkit.logging import configure_logger
from typer import Typer


app = Typer()
logger = configure_logger(__name__)


@app.command()
def install(plugin_name: str) -> None:
    """
    Installs a plugin

    :param plugin_name: Name of the plugin to install
    """
    logger.info("Installing plugin: %s", plugin_name)

    plugin_location = (
        "git+ssh://git@github.com/IBM/ares.git#egg="
        + plugin_name
        + "&subdirectory=plugins/"
        + plugin_name
    )
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "plugins/", plugin_name]
    )  # nosec
