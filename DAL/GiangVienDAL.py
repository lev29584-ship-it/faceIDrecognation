import re
from .ConnectDatabase import ConnectDatabase
from .GiangVien import GiangVien


class GiangVienDAL:

    # ======================
    # ITER ROW
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
    # GET ALL
    # ======================
    @staticmethod
    def get():
        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM giangvien")

            for row in GiangVienDAL.iter_row(cursor):
                list_data.append(row)

        except Exception as e:
            print("GET ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return list_data

    # ======================
    # GET ONE OBJECT
    # ======================
    @staticmethod
    def getItem(value):
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM giangvien WHERE magiangvien=?",
                (value,)
            )

            row = cursor.fetchone()

            if row:
                return GiangVien(
                    row[0],
                    row[1],
                    row[2],
                    row[3]
                )

        except Exception as e:
            print("GET ITEM ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return None

    # ======================
    # GENERATE ID
    # ======================
    @staticmethod
    def generateID():
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT TOP 1 magiangvien
                FROM giangvien
                ORDER BY magiangvien DESC
            """)

            row = cursor.fetchone()
            last_id = row[0] if row else "GV000"

            num = int(re.sub(r"\D", "", last_id)) + 1
            return f"GV{num:03}"

        except Exception as e:
            print("GEN ID ERROR:", e)
            return "GV001"

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ======================
    # ADD
    # ======================
    @staticmethod
    def add(gv: GiangVien):
        query = """
        INSERT INTO giangvien
        (magiangvien, hoten, sodienthoai, mataikhoan)
        VALUES (?, ?, ?, ?)
        """

        data = (
            gv.magiangvien,
            gv.hoten,
            gv.sodienthoai,
            gv.mataikhoan
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
    # UPDATE
    # ======================
    @staticmethod
    def update(gv: GiangVien):
        query = """
        UPDATE giangvien
        SET hoten=?, sodienthoai=?, mataikhoan=?
        WHERE magiangvien=?
        """

        data = (
            gv.hoten,
            gv.sodienthoai,
            gv.mataikhoan,
            gv.magiangvien
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
    # DELETE
    # ======================
    @staticmethod
    def delete(id):
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM giangvien WHERE magiangvien=?",
                (id,)
            )

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
    # FIND
    # ======================
    @staticmethod
    def find(key, value):
        allowed = ["magiangvien", "hoten", "sodienthoai", "mataikhoan"]
        if key not in allowed:
            return []

        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                f"SELECT * FROM giangvien WHERE {key} LIKE ?",
                (f"%{value}%",)
            )

            for row in GiangVienDAL.iter_row(cursor):
                list_data.append(row)

        except Exception as e:
            print("FIND ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return list_data

    # ======================
    # CHECK EXIST
    # ======================
    @staticmethod
    def checkExistTaiKhoan(mataikhoan):
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT 1 FROM giangvien WHERE mataikhoan=?",
                (mataikhoan,)
            )

            return cursor.fetchone() is not None

        except Exception as e:
            print(e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return False

    # ======================
    # CHECK PHONE
    # ======================
    @staticmethod
    def checkSoDienThoaiTonTai(sodienthoai):
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT 1 FROM giangvien WHERE sodienthoai=?",
                (sodienthoai,)
            )

            return cursor.fetchone() is not None

        except Exception as e:
            print(e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return False