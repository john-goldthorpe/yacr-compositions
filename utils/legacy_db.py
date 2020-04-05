"""
legacy_db.py

Read the legacy MS Access database for information on historic YACR compositions.

May require MS Access Database Engine 2010 to be installed ...
https://www.microsoft.com/en-US/download/details.aspx?id=13255

John Goldthorpe
29-MAR-2020
"""

import pyodbc
from pathlib import Path


def _get_records(filename):
    """

    :param filename: Filename of old MS Access database
    :return: yield dictionaries representing each record from the Compositions table
             in the style of csv.DictReader
    """
    if not Path(filename).exists():
        raise FileExistsError(f"Database '{filename}' does not exist")
    connection_string = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=admin;PWD=' % filename
    con = pyodbc.connect(connection_string)
    cur = con.cursor()
    columns = [col.column_name for col in cur.columns(table='Compositions')]
    cur.execute("select * from compositions order by [comp no]")
    for rec in cur.fetchall():
        yield {columns[i]: value for i, value in enumerate(rec)}
    con.close()
