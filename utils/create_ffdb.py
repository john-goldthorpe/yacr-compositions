"""
create_ffdb.py

Create the Flat File database using data from the legacy database.

John Goldthorpe
04-APR-2020
"""

from pathlib import Path
import toml
import os


def _generate_toml_file(ffdb_dir, comp_data):
    rpt = comp_data['legacy_db'].get('Report No')
    rpt_dir = Path(ffdb_dir) / f"report-{rpt:03}"
    if not rpt_dir.exists():
        os.mkdir(rpt_dir)
    filename = f"{comp_data['legacy_db'].get('Peal No')}-{comp_data['legacy_db'].get('Comp No')}.toml"
    full_filename = rpt_dir / filename
    if not full_filename.exists():
        print(full_filename)
        with open(full_filename, 'w') as h:
            toml.dump(comp_data, h)
