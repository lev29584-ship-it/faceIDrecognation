import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .Quyen_ChucNang import Quyen_ChucNang
from .ConnectDatabase import ConnectDatabase


class Quyen_ChucNangDAL:

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

            cursor.execute("SELECT * FROM quyen_chucnang")

            for row in Quyen_ChucNangDAL.iter_row(cursor, 10):
                list_data.append(row)

        except Exception as e:
            print(e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return list_data

    # ======================
    # ADD
    # ======================
    @staticmethod
    def add(qcn: Quyen_ChucNang):

        query = """
        INSERT INTO quyen_chucnang (maquyen, machucnang)
        VALUES (?, ?)
        """

        data = (qcn._maquyen, qcn._machucnang)

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, data)
            conn.commit()

            return True

        except Exception as ex:
            print(ex)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return False

    # ======================
    # UPDATE (RBAC SAFE)
    # ======================
    @staticmethod
    def update(maquyen, old_machucnang, new_machucnang):

        query = """
        UPDATE quyen_chucnang
        SET machucnang = ?
        WHERE maquyen = ?
        AND machucnang = ?
        """

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(query, (new_machucnang, maquyen, old_machucnang))

            if cursor.rowcount > 0:
                conn.commit()
                return True

        except Exception as ex:
            print(ex)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return False

    # ======================
    # DELETE BY ROLE
    # ======================
    @staticmethod
    def delete(maquyen):

        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM quyen_chucnang WHERE maquyen = ?",
                (maquyen,)
            )

            if cursor.rowcount > 0:
                conn.commit()
                return True

        except Exception as ex:
            print(ex)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return False

    # ======================
    # GET PERMISSIONS BY ROLE
    # ======================
    @staticmethod
    def getListChucNangTheoQuyen(maquyen):

        list_permission = []
        conn = cursor = None

        try:
            conn = ConnectDatabase().Connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT machucnang FROM quyen_chucnang WHERE maquyen = ?",
                (maquyen,)
            )

            for row in Quyen_ChucNangDAL.iter_row(cursor, 10):
                list_permission.append(row[0])

        except Exception as ex:
            print(ex)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return list_permission