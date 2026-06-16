from .ConnectDatabase import ConnectDatabase


class ThongKeDAL:

    def _connect(self):
        return ConnectDatabase().Connect()

    def getsv(self):
        try:
            conn = self._connect()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM sinhvien")
            return cursor.fetchone()[0]

        except Exception as e:
            print(e)
            return 0

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    # =========================
    def getdd(self):
        try:
            conn = self._connect()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM diemdanh")
            return cursor.fetchone()[0]

        except Exception as e:
            print(e)
            return 0

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    # =========================
    def getlate(self):
        try:
            conn = self._connect()
            cursor = conn.cursor()

            query = """
            SELECT COUNT(madiemdanh)
            FROM diemdanh dd
            JOIN buoihoc bh ON dd.mabuoihoc = bh.mabuoihoc
            WHERE (
                dd.giovao > bh.giobatdau
                OR dd.giovao = '00:00:00'
            )
            AND dd.giora != '00:00:00'
            """

            cursor.execute(query)
            return cursor.fetchone()[0]

        except Exception as e:
            print(e)
            return 0

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    # =========================
    def getabsent(self):
        try:
            conn = self._connect()
            cursor = conn.cursor()

            query = """
            SELECT COUNT(*)
            FROM (
                SELECT sv.masinhvien, bh.mabuoihoc
                FROM sinhvien sv
                JOIN lop l ON sv.malop = l.malop
                JOIN buoihoc bh ON l.malop = bh.malop
            ) a
            LEFT JOIN diemdanh dd
            ON a.masinhvien = dd.masinhvien
            AND a.mabuoihoc = dd.mabuoihoc
            WHERE dd.madiemdanh IS NULL
            """

            cursor.execute(query)
            return cursor.fetchone()[0]

        except Exception as e:
            print(e)
            return 0

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    # =========================
    def getKDD(self):
        try:
            conn = self._connect()
            cursor = conn.cursor()

            query = """
            SELECT COUNT(*)
            FROM diemdanh dd
            JOIN buoihoc bh ON dd.mabuoihoc = bh.mabuoihoc
            WHERE dd.giora = '00:00:00'
               OR dd.giovao = '00:00:00'
            """

            cursor.execute(query)
            return cursor.fetchone()[0]

        except Exception as e:
            print(e)
            return 0

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    # =========================
    def list_DiMuon(self):
        try:
            conn = self._connect()
            cursor = conn.cursor()

            query = """
            SELECT dd.masinhvien, sv.hoten, sv.malop, bh.ngay, dd.mabuoihoc
            FROM sinhvien sv
            JOIN diemdanh dd ON dd.masinhvien = sv.masinhvien
            JOIN buoihoc bh ON dd.mabuoihoc = bh.mabuoihoc
            WHERE (
                dd.giovao > bh.giobatdau
                OR dd.giovao = '00:00:00'
            )
            AND dd.giora != '00:00:00'
            """

            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(e)
            return []

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    # =========================
    def list_Vang(self):
        try:
            conn = self._connect()
            cursor = conn.cursor()

            query = """
            SELECT a.masinhvien, a.hoten, a.malop, a.ngay, a.mabuoihoc
            FROM (
                SELECT sv.masinhvien, sv.hoten, sv.malop, bh.ngay, bh.mabuoihoc
                FROM sinhvien sv
                JOIN lop l ON sv.malop = l.malop
                JOIN buoihoc bh ON l.malop = bh.malop
            ) a
            LEFT JOIN diemdanh dd
            ON a.masinhvien = dd.masinhvien
            AND a.mabuoihoc = dd.mabuoihoc
            WHERE dd.madiemdanh IS NULL
            """

            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(e)
            return []

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    # =========================
    def list_KDD(self):
        try:
            conn = self._connect()
            cursor = conn.cursor()

            query = """
            SELECT dd.masinhvien, sv.hoten, sv.malop, bh.ngay, dd.mabuoihoc
            FROM sinhvien sv
            JOIN diemdanh dd ON dd.masinhvien = sv.masinhvien
            JOIN buoihoc bh ON dd.mabuoihoc = bh.mabuoihoc
            WHERE dd.giora = '00:00:00'
               OR dd.giovao = '00:00:00'
            """

            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(e)
            return []

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass