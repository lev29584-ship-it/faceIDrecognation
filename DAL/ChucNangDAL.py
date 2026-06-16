import os
import sys
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .ChucNang import ChucNang
from .ConnectDatabase import ConnectDatabase


class ChucNangDAL:

    # ======================
    # 🔁 ITER ROW
    # ======================
    @staticmethod
    def iter_row(cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    # ======================
    # 📥 GET ALL
    # ======================
    @staticmethod
    def get():
        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM chucnang")

            for row in ChucNangDAL.iter_row(cursor, 10):
                list_data.append(ChucNang(row[0], row[1]))

        except Exception as e:
            print("GET ERROR:", e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return list_data

    # ======================
    # 🆔 GENERATE ID
    # ======================
    @staticmethod
    def generateID():
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT TOP 1 machucnang
                FROM chucnang
                ORDER BY machucnang DESC
            """)

            row = cursor.fetchone()
            last_id = row[0] if row else "CN000"

            num = int(re.sub(r"\D", "", last_id)) + 1
            return f"CN{num:03}"

        except Exception as e:
            print("GEN ID ERROR:", e)
            return "CN001"

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ======================
    # ➕ ADD
    # ======================
    @staticmethod
    def add(cn: ChucNang):

        query = """
        INSERT INTO chucnang (machucnang, tenchucnang)
        VALUES (?, ?)
        """

        data = (
            cn.machucnang,
            cn.tenchucnang
        )

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)
            conn.commit()

            return True

        except Exception as e:
            print("ADD ERROR:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ======================
    # ✏️ UPDATE
    # ======================
    @staticmethod
    def update(cn: ChucNang):

        query = """
        UPDATE chucnang
        SET tenchucnang = ?
        WHERE machucnang = ?
        """

        data = (
            cn.tenchucnang,
            cn.machucnang
        )

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)
            conn.commit()

            return True

        except Exception as e:
            print("UPDATE ERROR:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ======================
    # ❌ DELETE
    # ======================
    @staticmethod
    def delete(id):

        query = "DELETE FROM chucnang WHERE machucnang = ?"

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, (id,))

            if cursor.rowcount > 0:
                conn.commit()
                return True

        except Exception as e:
            print("DELETE ERROR:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ======================
    # 🔎 FIND SAFE
    # ======================
    @staticmethod
    def find(key, value):

        list_data = []

        allowed_keys = ["machucnang", "tenchucnang"]

        if key not in allowed_keys:
            return []

        query = f"""
        SELECT *
        FROM chucnang
        WHERE {key} LIKE ?
        """

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, (f"%{value}%",))

            for row in ChucNangDAL.iter_row(cursor, 10):
                list_data.append(ChucNang(row[0], row[1]))

        except Exception as e:
            print("FIND ERROR:", e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return list_data

    # ======================
    # 🔍 CHECK EXISTS
    # ======================
    @staticmethod
    def checkTenCNTonTai(tenchucnang):

        query = """
        SELECT 1
        FROM chucnang
        WHERE tenchucnang = ?
        """

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, (tenchucnang,))
            return cursor.fetchone() is not None

        except Exception as e:
            print("CHECK ERROR:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()