class Quyen:
    def __init__(self, maquyen, tenquyen):
        self._maquyen = maquyen
        self._tenquyen = tenquyen

    # ===== GET =====
    def getMaQuyen(self):
        return self._maquyen

    def getTenQuyen(self):
        return self._tenquyen

    # ===== SET =====
    def setMaQuyen(self, maquyen):
        self._maquyen = maquyen

    def setTenQuyen(self, tenquyen):
        self._tenquyen = tenquyen