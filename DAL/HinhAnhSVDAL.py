from .HinhAnhSV import HinhAnhSV
from .ConnectDatabase import ConnectDatabase


class HinhAnhSVDAL:

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

            cursor.execute("SELECT * FROM hinhanh_sinhvien")

            for row in HinhAnhSVDAL.iter_row(cursor):
                list_data.append(row)

        except Exception as e:
            print("GET ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return list_data

    # ======================
    # ADD IMAGE
    # ======================
    @staticmethod
    def add(ha: HinhAnhSV):
        query = """
        INSERT INTO hinhanh_sinhvien
        (masinhvien, hinhanh)
        VALUES (?, ?)
        """

        data = (
            ha.masinhvien,
            ha.duongdan if hasattr(ha, "duongdan") else ha.hinhanh
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
    # DELETE ALL BY STUDENT
    # ======================
    @staticmethod
    def delete(masinhvien):
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM hinhanh_sinhvien WHERE masinhvien=?",
                (masinhvien,)
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
    # GET IMAGES BY STUDENT
    # ======================
    @staticmethod
    def find(masinhvien):
        list_data = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT masinhvien, hinhanh
                FROM hinhanh_sinhvien
                WHERE masinhvien=?
            """, (masinhvien,))

            for row in HinhAnhSVDAL.iter_row(cursor):
                list_data.append(row)

        except Exception as e:
            print("FIND ERROR:", e)

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

        return list_data