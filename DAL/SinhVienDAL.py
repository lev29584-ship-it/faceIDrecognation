import re
from .SinhVien import SinhVien
from .ConnectDatabase import ConnectDatabase


class SinhVienDAL:

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

            cursor.execute("SELECT * FROM sinhvien")

            for row in SinhVienDAL.iter_row(cursor, 10):
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

            cursor.execute("SELECT COUNT(*) FROM sinhvien")
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
                SELECT TOP 1 masinhvien
                FROM sinhvien
                ORDER BY masinhvien DESC
            """)

            row = cursor.fetchone()
            last_id = row[0] if row else "SV000"

            num = int(re.sub(r"\D", "", last_id)) + 1
            return f"SV{num:03}"

        except Exception as e:
            print("Lỗi tăng id:", e)
            return "SV001"

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # ===== ADD =====
    @staticmethod
    def add(sv: SinhVien):
        query = """
        INSERT INTO sinhvien
        (masinhvien, hoten, malop, cmnd, gioitinh, ngaysinh, email, sodienthoai, khoahoc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        data = (
            sv._masinhvien,
            sv._hoten,
            sv._malop,
            sv._cmnd,
            sv._gioitinh,
            sv._ngsinh,
            sv._email,
            sv._sodienthoai,
            sv._khoahoc
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
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return False

    # ===== UPDATE =====
    @staticmethod
    def update(sv: SinhVien):
        query = """
        UPDATE sinhvien
        SET hoten=?, malop=?, cmnd=?, gioitinh=?, ngaysinh=?, email=?, sodienthoai=?, khoahoc=?
        WHERE masinhvien=?
        """

        data = (
            sv._hoten,
            sv._malop,
            sv._cmnd,
            sv._gioitinh,
            sv._ngsinh,
            sv._email,
            sv._sodienthoai,
            sv._khoahoc,
            sv._masinhvien
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
                "DELETE FROM sinhvien WHERE masinhvien = ?",
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

        allowed_keys = [
            "masinhvien", "hoten", "malop",
            "cmnd", "email", "sodienthoai", "khoahoc"
        ]

        if key not in allowed_keys:
            return []

        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                f"SELECT * FROM sinhvien WHERE {key} LIKE ?",
                (f"%{value}%",)
            )

            for row in SinhVienDAL.iter_row(cursor, 10):
                list_data.append(row)

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return list_data

    # ===== FIND BY ID =====
    @staticmethod
    def findMaSinhVien(value):
        conn = cursor = None
        list_data = []

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM sinhvien WHERE masinhvien = ?",
                (value,)
            )

            for row in SinhVienDAL.iter_row(cursor, 10):
                list_data.append(row)

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return list_data

    # ===== CHECK TỒN TẠI =====
    @staticmethod
    def checkTonTai(key, value, exclude_id=None):

        allowed_keys = ["cmnd", "email", "sodienthoai"]
        if key not in allowed_keys:
            return False

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            query = f"SELECT 1 FROM sinhvien WHERE {key} = ?"
            params = [value]

            if exclude_id:
                query += " AND masinhvien <> ?"
                params.append(exclude_id)

            cursor.execute(query, tuple(params))

            # TRUE = đã tồn tại
            return cursor.fetchone() is not None

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return False