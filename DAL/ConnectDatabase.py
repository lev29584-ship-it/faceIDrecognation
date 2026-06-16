import pyodbc
import os


class ConnectDatabase:

    @staticmethod
    def Connect():
        try:
            server = os.getenv("DB_SERVER", r"LAPTOP-JE3G4QTM\SQLEXPRESS")
            database = os.getenv("DB_NAME", "faceid_db")
            username = os.getenv("DB_USER", "sa")
            password = os.getenv("DB_PASS", "12345")

            conn = pyodbc.connect(
                "DRIVER={SQL Server};"
                f"SERVER={server};"
                f"DATABASE={database};"
                f"UID={username};"
                f"PWD={password};"
                "TrustServerCertificate=yes;"
            )

            return conn

        except Exception as e:
            print("❌ Database connection error:", e)
            return None