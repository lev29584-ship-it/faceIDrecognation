from DAL.HinhAnhSVDAL import HinhAnhSVDAL
from DAL.HinhAnhSV import HinhAnhSV


class HinhAnhSVBUS:
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
        return HinhAnhSVDAL.get()

    # ======================
    # ➕ ADD
    # ======================
    def add(self, ha_sv: HinhAnhSV):
        self._check_permission(["ADMIN", "TEACHER"])

        if not ha_sv:
            raise Exception("Dữ liệu hình ảnh không hợp lệ")

        if not getattr(ha_sv, "duongdan", None):
            raise Exception("Thiếu đường dẫn hình ảnh")

        return HinhAnhSVDAL.add(ha_sv)

    # ======================
    # ❌ DELETE
    # ======================
    def delete(self, id: int):
        self._check_permission(["ADMIN", "TEACHER"])

        if not id:
            raise Exception("ID không hợp lệ")

        return HinhAnhSVDAL.delete(id)

    # ======================
    # 🔎 FIND
    # ======================
    def find(self, value):
        return HinhAnhSVDAL.find(value)

    # ======================
    # 👤 GET BY STUDENT
    # ======================
    def getByStudent(self, masv):
        if not masv:
            return []

        return HinhAnhSVDAL.find(masv)