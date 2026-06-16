from .TaiKhoan import TaiKhoan
from .ConnectDatabase import ConnectDatabase
import re


class TaiKhoanDAL:

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

            cursor.execute("SELECT * FROM taikhoan")

            for row in TaiKhoanDAL.iter_row(cursor, 10):
                list_data.append(row)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return list_data

    # ===== GENERATE ID =====
    @staticmethod
    def generateID():
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT TOP 1 mataikhoan
                FROM taikhoan
                ORDER BY mataikhoan DESC
            """)

            row = cursor.fetchone()
            last_id = row[0] if row else "TK000"

            num = int(re.sub(r"\D", "", last_id)) + 1
            return f"TK{num:03}"

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ===== ADD =====
    @staticmethod
    def add(tk: TaiKhoan):

        query = """
        INSERT INTO taikhoan (mataikhoan, email, matkhau, maquyen)
        VALUES (?, ?, ?, ?)
        """

        data = (
            tk._mataikhoan,
            tk._email,
            tk._matkhau,
            tk._maquyen
        )

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)
            conn.commit()

            return cursor.rowcount > 0

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ===== UPDATE =====
    @staticmethod
    def update(tk: TaiKhoan):

        query = """
        UPDATE taikhoan
        SET email = ?, maquyen = ?
        WHERE mataikhoan = ?
        """

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, (
                tk._email,
                tk._maquyen,
                tk._mataikhoan
            ))

            conn.commit()
            return cursor.rowcount > 0

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ===== DELETE =====
    @staticmethod
    def delete(id):

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM taikhoan WHERE mataikhoan = ?",
                (id,)
            )

            conn.commit()
            return cursor.rowcount > 0

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ===== FIND =====
    @staticmethod
    def find(key, value):

        allowed_keys = ["mataikhoan", "email", "maquyen"]
        if key not in allowed_keys:
            return []

        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                f"SELECT * FROM taikhoan WHERE {key} LIKE ?",
                (f"%{value}%",)
            )

            for row in TaiKhoanDAL.iter_row(cursor, 10):
                list_data.append(row)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return list_data

    # ===== LOGIN =====
    @staticmethod
    def checkLogin(email, password):

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT mataikhoan, email, maquyen
                FROM taikhoan
                WHERE email = ? AND matkhau = ?
            """, (email, password))

            return cursor.fetchone()

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ===== PASSWORD =====
    @staticmethod
    def changePassword(email, mkmoi):

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE taikhoan
                SET matkhau = ?
                WHERE email = ?
            """, (mkmoi, email))

            conn.commit()
            return cursor.rowcount > 0

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ===== CHECK ADMIN =====
    @staticmethod
    def checkNotTaiKhoanAmin(mataikhoan):

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT 1 FROM taikhoan
                WHERE mataikhoan = ? AND maquyen = 'Q001'
            """, (mataikhoan,))

            return cursor.fetchone() is None

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    # ===== CHECK EMAIL =====
    @staticmethod
    def checkEmailTonTai(email):

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT 1 FROM taikhoan WHERE email = ?",
                (email,)
            )

            return cursor.fetchone() is not None

        finally:
            if cursor: cursor.close()
            if conn: conn.close()