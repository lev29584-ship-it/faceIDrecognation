class Lop:
    def __init__(self, malop, tenlop):
        self._malop = malop
        self._tenlop = tenlop

    # ===== GET =====
    def getMalop(self):
        return self._malop

    def getTenlop(self):
        return self._tenlop

    # ===== SET =====
    def setMalop(self, malop):
        self._malop = malop

    def setTenlop(self, tenlop):
        self._tenlop = tenlop

    # ===== OPTIONAL: DEBUG =====
    def __repr__(self):
        return f"Lop(malop={self._malop}, tenlop={self._tenlop})"