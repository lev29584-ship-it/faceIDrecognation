from DAL.SinhVienDAL import SinhVienDAL
from DAL.SinhVien import SinhVien


class SinhVienBUS:
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
        return SinhVienDAL.get()

    # ======================
    # 📊 COUNT
    # ======================
    def countAll(self):
        return SinhVienDAL.countAll()

    # ======================
    # 🆔 GENERATE ID
    # ======================
    def generateID(self):
        return SinhVienDAL.generateID()

    # ======================
    # ➕ ADD
    # ======================
    def add(self, sv: SinhVien):
        self._check_permission(["ADMIN", "TEACHER"])

        if not sv:
            raise Exception("Dữ liệu sinh viên không hợp lệ")

        # check MSSV
        if self.checkTonTai("masinhvien", sv.masinhvien):
            raise Exception("Mã sinh viên đã tồn tại")

        # check email nếu có
        if getattr(sv, "email", None) and self.checkTonTai("email", sv.email):
            raise Exception("Email đã tồn tại")

        # check phone nếu có
        if getattr(sv, "sodienthoai", None) and self.checkTonTai("sodienthoai", sv.sodienthoai):
            raise Exception("Số điện thoại đã tồn tại")

        return SinhVienDAL.add(sv)

    # ======================
    # ✏️ UPDATE
    # ======================
    def update(self, sv: SinhVien):
        self._check_permission(["ADMIN", "TEACHER"])

        if not sv:
            raise Exception("Dữ liệu sinh viên không hợp lệ")

        return SinhVienDAL.update(sv)

    # ======================
    # ❌ DELETE
    # ======================
    def delete(self, id: int):
        self._check_permission(["ADMIN"])

        if not id:
            raise Exception("ID không hợp lệ")

        return SinhVienDAL.delete(id)

    # ======================
    # 🔎 FIND
    # ======================
    def find(self, key, value):
        return SinhVienDAL.find(key, value)

    # ======================
    # 🔎 FIND BY MSSV
    # ======================
    def findMaSinhVien(self, value):
        return SinhVienDAL.findMaSinhVien(value)

    # ======================
    # 🔍 CHECK EXIST
    # ======================
    def checkTonTai(self, key, value):
        return SinhVienDAL.checkTonTai(key, value)

    # ======================
    # 👤 SUPPORT FACE RECOGNITION
    # ======================
    def getById(self, masinhvien):
        if not masinhvien:
            return None

        return self.findMaSinhVien(masinhvien)