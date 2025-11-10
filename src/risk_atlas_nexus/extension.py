import subprocess
import sys

from typer import Typer

from risk_atlas_nexus.toolkit.logging import configure_logger


app = Typer()
logger = configure_logger(__name__)


@app.callback()
def main() -> None:
    """
    RAN Extension CLI Application
    """


@app.command()
def install(extension_name: str) -> None:
    """
    Installs an extension

    :param extension_name: Name of the extension to install
    """
    logger.info("Installing extension: %s", extension_name)

    extension_location = (
        "git+ssh://git@github.com/dhavalsalwala/risk-atlas-nexus-extensions.git"
        + "#subdirectory="
        + extension_name
    )
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", extension_location]
    )  # nosec
