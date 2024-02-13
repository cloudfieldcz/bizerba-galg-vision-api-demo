import logging
import sys

from app.configuration import config
from app.logging.galg_logger import init_logger
from app.server import server

init_logger()


def run_server():
    server(host=config.HOST, port=config.PORT)


if __name__ == "__main__":
    logging.info(f"Reading start parameters. Param count = {len(sys.argv)}, {sys.argv}")
    raise SystemExit(run_server())
