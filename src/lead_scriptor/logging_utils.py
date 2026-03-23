import json
import logging
import os
import sys
from typing import Any


def configure_logging() -> logging.Logger:
    level_name = os.environ.get("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)
    logging.basicConfig(level=level, stream=sys.stderr, format="%(message)s")
    return logging.getLogger("lead_scriptor")


def log_event(logger: logging.Logger, level: int, event: str, **payload: Any) -> None:
    record = {"event": event, **payload}
    logger.log(level, json.dumps(record, ensure_ascii=True, sort_keys=True))
