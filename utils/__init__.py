from utils.legacy_db import _get_records
from utils.create_ffdb import _generate_toml_file
from utils.data_structure import _generate_composition_data

LEGACY_DB_FILENAME = r"C:\Users\john.goldthorpe\Dropbox\YACR\yacr-compositions\data\legacy\05peals.mdb"
FLAT_FILE_DB_ROOT_DIR = r"C:\Users\john.goldthorpe\Dropbox\YACR\yacr-compositions\data\ffdb"


def get_legacy_records():
    return [rec for rec in _get_records(LEGACY_DB_FILENAME)]


def generate_toml_files():
    for rec in get_legacy_records():
        comp_data = _generate_composition_data(rec)
        _generate_toml_file(FLAT_FILE_DB_ROOT_DIR, comp_data)
    print('Done')
