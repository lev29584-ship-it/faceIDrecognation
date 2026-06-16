import re
from .ConnectDatabase import ConnectDatabase
from .DiemDanh import DiemDanh


class DiemDanhDAL:

    @staticmethod
    def iter_row(cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    # ======================
    # 📥 GET
    # ======================
    @staticmethod
    def get():
        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    dd.madiemdanh,
                    dd.masinhvien,
                    sv.hoten,
                    l.tenlop,
                    dd.giovao,
                    dd.giora,
                    dd.mabuoihoc,
                    dd.hinhanh
                FROM diemdanh dd
                JOIN sinhvien sv ON dd.masinhvien = sv.masinhvien
                JOIN lop l ON l.malop = sv.malop
            """)

            for row in DiemDanhDAL.iter_row(cursor):
                list_data.append(row)

        except Exception as e:
            print("GET ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

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
                SELECT TOP 1 madiemdanh
                FROM diemdanh
                ORDER BY madiemdanh DESC
            """)

            row = cursor.fetchone()
            last_id = row[0] if row else "DD000"

            num = int(re.sub(r"\D", "", last_id)) + 1
            return f"DD{num:03}"

        except Exception as e:
            print("GEN ID ERROR:", e)
            return "DD001"

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ======================
    # ➕ ADD
    # ======================
    @staticmethod
    def add(dd: DiemDanh):
        query = """
        INSERT INTO diemdanh
        (madiemdanh, masinhvien, giovao, mabuoihoc, hinhanh)
        VALUES (?, ?, ?, ?, ?)
        """

        data = (
            dd.madiemdanh,
            dd.masinhvien,
            dd.giovao,
            dd.mabuoihoc,
            dd.hinhanh
        )

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)

            if cursor.rowcount > 0:
                conn.commit()
                return True

        except Exception as e:
            print("ADD ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return False

    # ======================
    # ✏️ UPDATE
    # ======================
    @staticmethod
    def update(dd: DiemDanh):
        query = """
        UPDATE diemdanh
        SET masinhvien=?, giovao=?, giora=?
        WHERE madiemdanh=?
        """

        data = (
            dd.masinhvien,
            dd.giovao,
            dd.giora,
            dd.madiemdanh
        )

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)

            if cursor.rowcount > 0:
                conn.commit()
                return True

        except Exception as e:
            print("UPDATE ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return False

    # ======================
    # ⏱ UPDATE GIỜ RA
    # ======================
    @staticmethod
    def updateGioRa(masinhvien, mabuoihoc, giora):
        query = """
        UPDATE diemdanh
        SET giora=?
        WHERE masinhvien=? AND mabuoihoc=?
        """

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, (giora, masinhvien, mabuoihoc))

            if cursor.rowcount > 0:
                conn.commit()
                return True

        except Exception as e:
            print("UPDATE GIỜ RA ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return False

    # ======================
    # ❌ DELETE
    # ======================
    @staticmethod
    def delete(id):
        query = "DELETE FROM diemdanh WHERE madiemdanh=?"

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

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return False

    # ======================
    # 🔎 FIND
    # ======================
    @staticmethod
    def find(key, value):
        allowed = ["madiemdanh", "masinhvien", "mabuoihoc"]
        if key not in allowed:
            return []

        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(f"""
                SELECT *
                FROM diemdanh
                WHERE {key} LIKE ?
            """, (f"%{value}%",))

            for row in DiemDanhDAL.iter_row(cursor):
                list_data.append(row)

        except Exception as e:
            print("FIND ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return list_data

    # ======================
    # 📸 FIND IMAGE
    # ======================
    @staticmethod
    def findMaDiemDanh(value):
        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT hinhanh
                FROM diemdanh
                WHERE madiemdanh=?
            """, (value,))

            for row in DiemDanhDAL.iter_row(cursor):
                list_data.append(row)

        except Exception as e:
            print("FIND IMAGE ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return list_data