from pathlib import Path
from .im_gegevensverstrekking_warmtetransitie import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "im_gegevensverstrekking_warmtetransitie.yaml"
