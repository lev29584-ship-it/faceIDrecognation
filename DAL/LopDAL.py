import os
import sys
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .Lop import Lop
from .ConnectDatabase import ConnectDatabase


class LopDAL:

    @staticmethod
    def iter_row(cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    # ===== GET =====
    @staticmethod
    def get():
        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM lop")

            for row in LopDAL.iter_row(cursor, 10):
                list_data.append(row)

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return list_data

    # ===== COUNT =====
    @staticmethod
    def countAll():
        count = 0
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM lop")
            row = cursor.fetchone()

            if row:
                count = row[0]

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return count

    # ===== GENERATE ID =====
    @staticmethod
    def generateID():
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT TOP 1 malop
                FROM lop
                ORDER BY malop DESC
            """)

            row = cursor.fetchone()

            last_id = row[0] if row else "L000"

            num = int(re.sub(r"\D", "", last_id)) + 1
            return f"L{num:03}"

        except Exception as e:
            print("Lỗi generate ID:", e)
            return "L001"

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ===== ADD =====
    @staticmethod
    def add(lop: Lop):
        query = """
        INSERT INTO lop (malop, tenlop)
        VALUES (?, ?)
        """

        data = (lop._malop, lop._tenlop)

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)

            conn.commit()
            return True

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return False

    # ===== UPDATE =====
    @staticmethod
    def update(lop: Lop):
        query = """
        UPDATE lop
        SET tenlop = ?
        WHERE malop = ?
        """

        data = (lop._tenlop, lop._malop)

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)

            conn.commit()
            return True

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return False

    # ===== DELETE =====
    @staticmethod
    def delete(id):
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM lop WHERE malop = ?", (id,))

            if cursor.rowcount > 0:
                conn.commit()
                return True

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return False

    # ===== FIND =====
    @staticmethod
    def find(key, value):
        list_data = []

        allowed_keys = ["malop", "tenlop"]
        if key not in allowed_keys:
            return []

        query = f"SELECT * FROM lop WHERE {key} LIKE ?"

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, (f"%{value}%",))

            for row in LopDAL.iter_row(cursor, 10):
                list_data.append(row)

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return list_data

    # ===== CHECK =====
    @staticmethod
    def checkTenLopTonTai(tenlop):
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT 1 FROM lop WHERE tenlop = ?",
                (tenlop,)
            )

            return cursor.fetchone() is not None

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return False