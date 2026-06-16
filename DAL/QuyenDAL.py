import re
from .Quyen import Quyen
from .ConnectDatabase import ConnectDatabase


class QuyenDAL:

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

            cursor.execute("SELECT * FROM quyen")

            for row in QuyenDAL.iter_row(cursor, 10):
                list_data.append(row)

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return list_data

    # ===== GENERATE ID =====
    @staticmethod
    def generateID():
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT TOP 1 maquyen
                FROM quyen
                ORDER BY maquyen DESC
            """)

            row = cursor.fetchone()
            last_id = row[0] if row else "Q000"

            num = int(re.sub(r"\D", "", last_id)) + 1
            return f"Q{num:03}"

        except Exception as e:
            print("Lỗi tăng id:", e)
            return "Q001"

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ===== ADD =====
    @staticmethod
    def add(q: Quyen):
        query = """
        INSERT INTO quyen (maquyen, tenquyen)
        VALUES (?, ?)
        """

        data = (q._maquyen, q._tenquyen)

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)

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

    # ===== UPDATE =====
    @staticmethod
    def update(q: Quyen):
        query = """
        UPDATE quyen
        SET tenquyen = ?
        WHERE maquyen = ?
        """

        data = (q._tenquyen, q._maquyen)

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)

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

    # ===== DELETE =====
    @staticmethod
    def delete(id):
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM quyen WHERE maquyen = ?",
                (id,)
            )

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

        allowed_keys = ["maquyen", "tenquyen"]
        if key not in allowed_keys:
            return []

        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                f"SELECT * FROM quyen WHERE {key} LIKE ?",
                (f"%{value}%",)
            )

            for row in QuyenDAL.iter_row(cursor, 10):
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
    def checkTenQuyenTonTai(tenquyen):

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT 1 FROM quyen WHERE tenquyen = ?",
                (tenquyen,)
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