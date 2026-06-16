from DAL.Quyen_ChucNangDAL import Quyen_ChucNangDAL


class PermissionBUS:
    _cache = {}

    def __init__(self, maquyen):
        self.maquyen = maquyen

    # ======================
    # 📥 LOAD PERMISSIONS
    # ======================
    def _load(self):
        if not self.maquyen:
            return set()

        data = Quyen_ChucNangDAL.getListChucNangTheoQuyen(self.maquyen)

        if not data:
            return set()

        return set(data)

    # ======================
    # 🔐 CHECK PERMISSION
    # ======================
    def has(self, machucnang):
        if not self.maquyen:
            return False

        if self.maquyen not in PermissionBUS._cache:
            PermissionBUS._cache[self.maquyen] = self._load()

        return machucnang in PermissionBUS._cache[self.maquyen]

    # ======================
    # 🔄 REFRESH CACHE
    # ======================
    def refresh(self):
        if not self.maquyen:
            return

        PermissionBUS._cache[self.maquyen] = self._load()

    # ======================
    # 🧠 GET ALL PERMISSIONS
    # ======================
    def getAll(self):
        if self.maquyen not in PermissionBUS._cache:
            PermissionBUS._cache[self.maquyen] = self._load()

        return PermissionBUS._cache[self.maquyen]