from DAL.LopDAL import LopDAL
from DAL.Lop import Lop


class LopBUS:
    def __init__(self, permission=None):
        self.permission = permission

    # ======================
    # 🔐 CHECK PERMISSION
    # ======================
    def _check_permission(self, roles):
        if not self.permission:
            raise Exception("Chưa đăng nhập")

        if self.permission.role not in roles:
            raise Exception("Không có quyền thực hiện chức năng này")

    # ======================
    # 📥 GET
    # ======================
    def get(self):
        return LopDAL.get()

    # ======================
    # 📊 COUNT
    # ======================
    def countAll(self):
        return LopDAL.countAll()

    # ======================
    # 🆔 GENERATE ID
    # ======================
    def generateID(self):
        return LopDAL.generateID()

    # ======================
    # ➕ ADD
    # ======================
    def add(self, lop: Lop):
        self._check_permission(["ADMIN", "MANAGER"])

        if not lop:
            raise Exception("Dữ liệu lớp không hợp lệ")

        if not getattr(lop, "tenlop", None):
            raise Exception("Thiếu tên lớp")

        if self.checkTenLopTonTai(lop.tenlop):
            raise Exception("Tên lớp đã tồn tại")

        return LopDAL.add(lop)

    # ======================
    # ✏️ UPDATE
    # ======================
    def update(self, lop: Lop):
        self._check_permission(["ADMIN", "MANAGER"])

        if not lop:
            raise Exception("Dữ liệu lớp không hợp lệ")

        return LopDAL.update(lop)

    # ======================
    # ❌ DELETE
    # ======================
    def delete(self, id: int):
        self._check_permission(["ADMIN"])

        if not id:
            raise Exception("ID không hợp lệ")

        return LopDAL.delete(id)

    # ======================
    # 🔎 FIND
    # ======================
    def find(self, key, value):
        return LopDAL.find(key, value)

    # ======================
    # 🔍 CHECK DUPLICATE
    # ======================
    def checkTenLopTonTai(self, tenlop):
        return LopDAL.checkTenLopTonTai(tenlop)

    # ======================
    # 📊 DASHBOARD SUPPORT
    # ======================
    def getAllWithCount(self):
        """
        UI dashboard: lớp + số lượng sinh viên (nếu DB hỗ trợ)
        """
        return LopDAL.get()