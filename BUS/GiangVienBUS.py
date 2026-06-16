from DAL.GiangVienDAL import GiangVienDAL
from DAL.GiangVien import GiangVien


class GiangVienBUS:
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
        return GiangVienDAL.get()

    # ======================
    # 🔎 GET ITEM
    # ======================
    def getItem(self, value):
        return GiangVienDAL.getItem(value)

    # ======================
    # 🆔 GENERATE ID
    # ======================
    def generateID(self):
        return GiangVienDAL.generateID()

    # ======================
    # ➕ ADD
    # ======================
    def add(self, gv: GiangVien):
        self._check_permission(["ADMIN"])

        if not gv:
            raise Exception("Dữ liệu không hợp lệ")

        if self.checkSoDienThoaiTonTai(gv.sodienthoai):
            raise Exception("Số điện thoại đã tồn tại")

        if self.checkExistTaiKhoan(gv.mataikhoan):
            raise Exception("Tài khoản đã được liên kết")

        return GiangVienDAL.add(gv)

    # ======================
    # ✏️ UPDATE
    # ======================
    def update(self, gv: GiangVien):
        self._check_permission(["ADMIN", "MANAGER"])

        if not gv:
            raise Exception("Dữ liệu không hợp lệ")

        return GiangVienDAL.update(gv)

    # ======================
    # ❌ DELETE
    # ======================
    def delete(self, id: int):
        self._check_permission(["ADMIN"])

        if not id:
            raise Exception("ID không hợp lệ")

        return GiangVienDAL.delete(id)

    # ======================
    # 🔎 FIND
    # ======================
    def find(self, key, value):
        return GiangVienDAL.find(key, value)

    # ======================
    # 🔍 CHECK EXIST
    # ======================
    def checkExistTaiKhoan(self, mataikhoan):
        return GiangVienDAL.checkExistTaiKhoan(mataikhoan)

    def checkSoDienThoaiTonTai(self, sodienthoai):
        return GiangVienDAL.checkSoDienThoaiTonTai(sodienthoai)

    # ======================
    # 👤 GET BY ACCOUNT
    # ======================
    def getByTaiKhoan(self, mataikhoan):
        return GiangVienDAL.find("mataikhoan", mataikhoan)