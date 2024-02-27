from PyQt5.QtWidgets import  *
from PyQt5 import  uic
import  AES_main as AES_tool

class MyGui(QDialog):

    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi("GUI.ui", self)
        self.show()

        self.btn_chose_BanRo.clicked.connect(self.Chon_File_BanRo)
        self.btn_chose_Key.clicked.connect(self.Chon_File_Key)
        self.btn_MaHoa.clicked.connect(self.MaHoa)

        self.btn_chose_BanMat.clicked.connect(self.Chon_File_BanMat)
        self.btn_chose_Key_02.clicked.connect(self.Chon_File_Key_02)
        self.btn_GiaiMa.clicked.connect(self.GiaiMa)
    def Chon_File_BanRo(self):
        text = AES_tool.Chose_File_Word()
        self.text_BanRo.setText(text)

    def Chon_File_Key(self):
        key = AES_tool.Chose_File_Word()
        self.textInput_Key.setText(key)

    def MaHoa(self):

        banRo = self.text_BanRo.toPlainText()
        key   = self.textInput_Key.toPlainText()

        banMat = AES_tool.MaHoa_02( banRo, key)

        self.text_content_BanMat.setText(banMat)

        mess = QMessageBox()
        mess.setText("Nội dung bản mật đã lưu vào BanMat.docx")
        mess.exec_()

    def Chon_File_BanMat(self):
        text = AES_tool.Chose_File_Word()
        self.text_BanMat.setText(text)

    def Chon_File_Key_02(self):
        key = AES_tool.Chose_File_Word()
        self.textInput_Key_2.setText(key)

    def GiaiMa(self):

        banMat = self.text_BanMat.toPlainText()
        key    = self.textInput_Key_2.toPlainText()

        banRo = AES_tool.GiaiMa_02( banMat, key)

        self.text_content_BanRo.setText(banRo)

        # mess = QMessageBox()
        # mess.setText("Nội dung bản mật đã lưu vào BanMat.docx")
        # mess.exec_()

def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()

if __name__ == '__main__':
    main()


