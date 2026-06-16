from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from BUS.ChucNangBUS import ChucNangBUS
from BUS.Quyen_ChucNangBUS import Quyen_ChucNangBUS


class Ui_Dialog(object):

    def __init__(self, maquyen):
        self.maquyen = maquyen
        self.list_ckb_cn = []

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 380)

        # ===== MAIN LAYOUT =====
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)

        # ===== TITLE =====
        self.label = QtWidgets.QLabel(
            "DANH SÁCH CHỨC NĂNG"
        )

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)

        self.label.setFont(font)
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.verticalLayout.addWidget(
            self.label
        )

        # ===== LIST =====
        self.listWidget = QtWidgets.QListWidget()

        self.listWidget.setSpacing(3)

        self.verticalLayout.addWidget(
            self.listWidget
        )

        # ===== BUTTON =====
        self.buttonBox = QtWidgets.QDialogButtonBox()

        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Ok
            |
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
        )

        self.verticalLayout.addWidget(
            self.buttonBox
        )

        # load data
        self.openDialogListChucNang()

        self.retranslateUi(Dialog)

        self.buttonBox.accepted.connect(
            Dialog.accept
        )

        self.buttonBox.rejected.connect(
            Dialog.reject
        )

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        Dialog.setWindowTitle(
            _translate(
                "Dialog",
                "Chọn chức năng"
            )
        )

    # ==========================
    # LOAD DANH SÁCH CHỨC NĂNG
    # ==========================
    def openDialogListChucNang(self):

        self.list_ckb_cn.clear()
        self.listWidget.clear()

        try:
            qcnBUS = Quyen_ChucNangBUS()

            list_qcn = qcnBUS.getListChucNangTheoQuyen(
                self.maquyen
            )

            cnBUS = ChucNangBUS()

            ds_chuc_nang = cnBUS.get()

            for cn in ds_chuc_nang:

                ma_cn = cn[0]
                ten_cn = cn[1]

                ckb = QtWidgets.QCheckBox(
                    ten_cn
                )

                ckb.setObjectName(ma_cn)

                # check quyền có sẵn
                if ma_cn in list_qcn:
                    ckb.setChecked(True)

                self.list_ckb_cn.append(
                    ckb
                )

                item = QtWidgets.QListWidgetItem()

                item.setSizeHint(
                    QtCore.QSize(0, 40)
                )

                self.listWidget.addItem(
                    item
                )

                self.listWidget.setItemWidget(
                    item,
                    ckb
                )

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                None,
                "Lỗi",
                str(e)
            )

    # ==========================
    # GET CHECKED FUNCTION
    # ==========================
    def getListChucNangChecked(self):

        list_cn_checked = []

        for ckb in self.list_ckb_cn:

            if ckb.isChecked():

                list_cn_checked.append(
                    ckb.objectName()
                )

        return list_cn_checked


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    Dialog = QtWidgets.QDialog()

    ui = Ui_Dialog("Q001")

    ui.setupUi(Dialog)

    Dialog.show()

    sys.exit(app.exec())