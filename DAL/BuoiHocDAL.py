import re
from .ConnectDatabase import ConnectDatabase
from .BuoiHoc import BuoiHoc


class BuoiHocDAL:

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
        data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM buoihoc")

            for row in BuoiHocDAL.iter_row(cursor, 10):
                data.append(row)

        except Exception as e:
            print("GET ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return data

    # ======================
    # 📊 COUNT
    # ======================
    @staticmethod
    def countAll():
        conn = cursor = None
        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM buoihoc")
            row = cursor.fetchone()

            return row[0] if row else 0

        except Exception as e:
            print("COUNT ERROR:", e)
            return 0

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

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
                SELECT TOP 1 mabuoihoc
                FROM buoihoc
                ORDER BY mabuoihoc DESC
            """)

            row = cursor.fetchone()
            last_id = row[0] if row else "BH000"

            num = int(re.sub(r"\D", "", last_id)) + 1
            return f"BH{num:03}"

        except Exception as e:
            print("GEN ID ERROR:", e)
            return "BH001"

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ======================
    # ➕ ADD
    # ======================
    @staticmethod
    def add(bh: BuoiHoc):
        query = """
        INSERT INTO buoihoc
        (mabuoihoc, giobatdau, gioketthuc, ngay, malop, magiangvien)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        data = (
            bh.mabuoihoc,
            bh.giobatdau,
            bh.gioketthuc,
            bh.ngay,
            bh.malop,
            bh.magiangvien
        )

        conn = cursor = None
        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)
            conn.commit()

            return cursor.rowcount > 0

        except Exception as e:
            print("ADD ERROR:", e)
            return False

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ======================
    # ✏️ UPDATE
    # ======================
    @staticmethod
    def update(bh: BuoiHoc):
        query = """
        UPDATE buoihoc
        SET giobatdau=?,
            gioketthuc=?,
            ngay=?,
            malop=?,
            magiangvien=?
        WHERE mabuoihoc=?
        """

        data = (
            bh.giobatdau,
            bh.gioketthuc,
            bh.ngay,
            bh.malop,
            bh.magiangvien,
            bh.mabuoihoc
        )

        conn = cursor = None
        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)
            conn.commit()

            return cursor.rowcount > 0

        except Exception as e:
            print("UPDATE ERROR:", e)
            return False

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ======================
    # ❌ DELETE
    # ======================
    @staticmethod
    def delete(id):
        query = "DELETE FROM buoihoc WHERE mabuoihoc=?"

        conn = cursor = None
        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, (id,))
            conn.commit()

            return cursor.rowcount > 0

        except Exception as e:
            print("DELETE ERROR:", e)
            return False

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ======================
    # 🔎 FIND SAFE
    # ======================
    @staticmethod
    def find(key, value):
        allowed = ["mabuoihoc", "malop", "magiangvien", "ngay"]

        if key not in allowed:
            return []

        query = f"SELECT * FROM buoihoc WHERE {key} LIKE ?"

        conn = cursor = None
        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, (f"%{value}%",))

            return list(BuoiHocDAL.iter_row(cursor, 10))

        except Exception as e:
            print("FIND ERROR:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ======================
    # 🔎 FIND BY ID
    # ======================
    @staticmethod
    def findMaBuoiHoc(value):
        query = "SELECT * FROM buoihoc WHERE mabuoihoc=?"

        conn = cursor = None
        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, (value,))
            return list(BuoiHocDAL.iter_row(cursor, 10))

        except Exception as e:
            print("FIND ID ERROR:", e)
            return []

        finally:
            if cursor: cursor.close()
            if conn: conn.close()