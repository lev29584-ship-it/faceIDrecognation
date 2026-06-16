from DTO.DiemDanh import DiemDanh
class DiemDanhBUS:
    def __init__(self, user=None):
        self.user = user  # role + id + class_id

    # ======================
    # 📥 GET (RBAC)
    # ======================
    def get(self):
        data = DiemDanhDAL.get()

        if not self.user:
            return []

        role = getattr(self.user, "role", None)

        # ======================
        # ADMIN → full access
        # ======================
        if role == "ADMIN":
            return data

        # ======================
        # TEACHER / MANAGER → theo lớp
        # ======================
        if role == "TEACHER":
            class_id = getattr(self.user, "class_id", None)

            return [
                x for x in data
                if getattr(x, "class_id", None) == class_id
            ]

        # ======================
        # STUDENT → chỉ dữ liệu của mình
        # ======================
        if role == "STUDENT":
            user_id = getattr(self.user, "id", None)

            return [
                x for x in data
                if getattr(x, "user_id", None) == user_id
            ]

        return []

    # ======================
    # 🆔 GENERATE ID
    # ======================
    def generateID(self):
        return DiemDanhDAL.generateID()

    # ======================
    # ➕ ADD
    # ======================
    def add(self, dd: DiemDanh):
        if not dd:
            raise Exception("Dữ liệu điểm danh không hợp lệ")

        return DiemDanhDAL.add(dd)

    # ======================
    # ✏️ UPDATE
    # ======================
    def update(self, dd: DiemDanh):
        if not dd:
            raise Exception("Dữ liệu điểm danh không hợp lệ")

        return DiemDanhDAL.update(dd)

    # ======================
    # ❌ DELETE ALL
    # ======================
    def deleteAll(self):
        self._check_admin()
        return DiemDanhDAL.deleteAll()

    # ======================
    # ❌ DELETE BY ID
    # ======================
    def delete(self, id):
        if not id:
            raise Exception("ID không hợp lệ")

        return DiemDanhDAL.delete(id)

    # ======================
    # 🔎 FIND
    # ======================
    def find(self, key, value):
        return DiemDanhDAL.find(key, value)

    def findMaDiemDanh(self, value):
        return DiemDanhDAL.findMaDiemDanh(value)

    # ======================
    # ⏱ UPDATE GIỜ RA
    # ======================
    def updateGioRa(self, masinhvien, mabuoihoc, giora):
        if not masinhvien or not mabuoihoc:
            raise Exception("Thiếu thông tin")

        return DiemDanhDAL.updateGioRa(masinhvien, mabuoihoc, giora)

    # ======================
    # 🔐 CHECK ADMIN
    # ======================
    def _check_admin(self):
        if not self.user or getattr(self.user, "role", None) != "ADMIN":
            raise Exception("Chỉ ADMIN được phép thực hiện")