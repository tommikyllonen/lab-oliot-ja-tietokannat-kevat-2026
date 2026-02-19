import os
from unittest import TestCase
import db_conn
from sqlite3 import Connection, ProgrammingError
from pathlib import Path
import sqlite3
from io import StringIO

DBNAME = "dev.db"

PRAGMA_TABLE = [
    (0, 'id', 'INTEGER', 0, None, 1),
    (1, 'manufacturer', 'VARCHAR(255)', 1, None, 0),
    (2, 'brand', 'VARCHAR(255)', 1, None, 0),
    (3, 'cost', 'REAL', 1, None, 0),
    (4, 'price', 'REAL', 1, None, 0)
]

RECORDS = [
    ("FizzWorks", "ColaFusion", 1.5, 3.99),
    ("SoftCarbo", "SparkleSplash", 0.85, 2.35)
]

import main

def test_run_one(capsys, monkeypatch):
    insertions: str = ""
    for field in RECORDS[0]:
        insertions += str(field) + '\n'
    monkeypatch.setattr('sys.stdin', StringIO(insertions))
    main.Main()
    expected_out = """Program starting.\nInsert product details below:\n- Insert manufacturer: - Insert brand: - Insert cost: - Insert price: Storing product details into the database...\nProgram ending."""
    captured = capsys.readouterr()
    assert captured.out.rstrip('\n') == expected_out
    return None

def test_run_two(capsys, monkeypatch):
    insertions: str = ""
    for field in RECORDS[1]:
        insertions += str(field) + '\n'
    monkeypatch.setattr('sys.stdin', StringIO(insertions))
    main.DB_CONN = sqlite3.connect(db_conn.DB_FILEPATH) # reset connection
    main.Main()
    expected_out = """Program starting.\nInsert product details below:\n- Insert manufacturer: - Insert brand: - Insert cost: - Insert price: Storing product details into the database...\nProgram ending."""
    captured = capsys.readouterr()
    assert captured.out.rstrip('\n') == expected_out
    return None

class DBTests(TestCase):
    def test_db_existence(self):
        self.assertTrue(os.path.exists(DBNAME), f"'{DBNAME}' doesn't exist. Are you sure you created connection to the correct database?")
        return None
    def test_dbfilepath(self):
        self.assertIsInstance(db_conn.DB_FILEPATH, Path, "Couldn't find DB_FILEPATH object or the object is not instance of pathlib.Path type.")
        return None
    def test_dbconn_type(self):
        self.assertIsInstance(main.DB_CONN, Connection, "Couldn't find DB_CONN object or the object is not instance of sqlite3.Connection type.")
        return None
    def test_table_product_columns(self):
        dbconn = sqlite3.connect(DBNAME)
        cursor = dbconn.cursor()
        cursor.execute(f'PRAGMA table_info("product")')
        table_info = cursor.fetchall()
        self.assertListEqual(PRAGMA_TABLE, table_info, "Are you sure the table 'product' is defined correctly?")
        dbconn.commit()
        cursor.close()
        return None
    def test_table_product_records(self):
        dbconn = sqlite3.connect(DBNAME)
        cursor = dbconn.cursor()
        cursor.execute("SELECT * FROM product")
        records = cursor.fetchall()
        dbconn.commit()
        cursor.close()
        expected_records = [
            (1, *RECORDS[0]),
            (2, *RECORDS[1])
        ]
        self.assertListEqual(expected_records, records)
        return None