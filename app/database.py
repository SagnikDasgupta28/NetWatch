
import sqlite3
from pathlib import Path

DB_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "netwatch.db"
)


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_database():

    with get_connection() as connection:

        connection.execute("""
            CREATE TABLE IF NOT EXISTS traffic (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                src_ip TEXT NOT NULL,
                dst_ip TEXT NOT NULL,
                protocol TEXT NOT NULL,
                domain TEXT,
                bytes_sent INTEGER NOT NULL,
                bytes_received INTEGER NOT NULL,
                duration_ms INTEGER NOT NULL
            )
        """)


def insert_event(event):

    with get_connection() as connection:

        connection.execute("""
            INSERT INTO traffic (
                timestamp,
                src_ip,
                dst_ip,
                protocol,
                domain,
                bytes_sent,
                bytes_received,
                duration_ms
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            event["timestamp"],
            event["src_ip"],
            event["dst_ip"],
            event["protocol"],
            event["domain"],
            event["bytes_sent"],
            event["bytes_received"],
            event["duration_ms"]
        ))


def get_statistics():

    with get_connection() as connection:

        cursor = connection.execute("""
            SELECT
                COUNT(*),
                COALESCE(SUM(bytes_sent), 0),
                COALESCE(SUM(bytes_received), 0)
            FROM traffic
        """)

        total, uploaded, downloaded = cursor.fetchone()

    return {
        "total_events": total,
        "uploaded_bytes": uploaded,
        "downloaded_bytes": downloaded
    }
