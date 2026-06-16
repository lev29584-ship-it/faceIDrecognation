from DAL.ThongKeDAL import ThongKeDAL


class ThongKeBUS:
    def __init__(self):
        self.dal = ThongKeDAL()

    # ======================
    # 📊 OVERVIEW COUNT
    # ======================
    def getOverview(self):
        return {
            "total_students": self.dal.getsv(),
            "total_attendance": self.dal.getdd(),
            "late": self.dal.getlate(),
            "absent": self.dal.getabsent(),
            "no_check": self.dal.getKDD()
        }

    # ======================
    # 📊 SINGLE COUNTS (optional use)
    # ======================
    def svcount(self):
        return self.dal.getsv()

    def ddcount(self):
        return self.dal.getdd()

    def latecount(self):
        return self.dal.getlate()

    def absentcount(self):
        return self.dal.getabsent()

    def kddcount(self):
        return self.dal.getKDD()

    # ======================
    # 📋 LIST REPORTS
    # ======================
    def list_di_muon(self):
        return self.dal.list_DiMuon()

    def list_vang(self):
        return self.dal.list_Vang()

    def list_kdd(self):
        return self.dal.list_KDD()

    # ======================
    # 🔎 SEARCH REPORT
    # ======================
    def find_di_muon(self, key, value):
        return self.dal.find_DiMuon(key, value)

    def find_vang(self, key, value):
        return self.dal.find_Vang(key, value)

    def find_khong_dd(self, key, value):
        return self.dal.find_KhongDD(key, value)