from PyQt5.QtWidgets import  *
from PyQt5 import  uic
import  RSA
import  AES_main as AES_tool

class MyGui(QMainWindow):

    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi("GUI.ui", self)
        self.show()

        self.btn_TaoKhoa.clicked.connect(self.TaoKhoa)

        self.btn_chose_BanRo.clicked.connect(self.Chon_Ban_Ro)
        self.btn_MaHoa.clicked.connect(self.Ma_Hoa)

        self.btn_chose_BanMa.clicked.connect(self.Chon_Ban_Ma)
        self.btn_GiaiMa.clicked.connect(self.Giai_Ma)

    def TaoKhoa(self):
        list_p_q = RSA.key.Chose_P_Q( 100, 200)
        print("step 01")
        p = list_p_q[0]
        q = list_p_q[1]

        list_n_phi_n = RSA.key.Find_N_Phi_N(p,q)
        n = list_n_phi_n[0]
        phi_n = list_n_phi_n[1]

        e = RSA.key.Find_E(phi_n)
        d = RSA.key.Find_d(e,phi_n)
        print("step 02")
        self.text_p.setText(str(p))
        self.text_q.setText(str(q))
        self.text_n.setText(str(n))
        self.text_phi_n.setText(str(phi_n))
        self.text_d.setText(str(d))
        self.text_e.setText(str(e))

        text_public = "( n, e) = " +  "( " +  str(n)  +  " , " +  str(e) +  " ) "
        text_private = "( n, d) = " + "( " + str(n) + " , " + str(d) + " ) "
        self.text_public_key.setText( str(text_public) )
        self.text_private_key.setText( str(text_private) )


    def Chon_Ban_Ro(self):
        text_ban_ro = AES_tool.Chose_File_Word()
        self.text_content_BanRo.setText(text_ban_ro)

    def Ma_Hoa(self):

        text_ban_ro = self.text_content_BanRo.toPlainText()
        n = int( self.text_Input_n_2.toPlainText() )
        e = int( self.text_Input_e.toPlainText() )

        text_ban_ma = RSA.MaHoa_String(text_ban_ro, n, e)
        # print(text_ban_ma)
        self.text_content_BanMa.setText( str(text_ban_ma) )

        AES_tool.Save_To_Word_File( text_ban_ma, 'BanMaCuaKey.docx' )

        mess = QMessageBox()
        mess.setText("Nội dung bản mật đã lưu vào BanMaCuaKey.docx")
        mess.exec_()

    def Chon_Ban_Ma(self):

        text_ban_ma = AES_tool.Chose_File_Word()
        self.text_content_BanMa02.setText( text_ban_ma )

    def Giai_Ma(self):

        text_ban_ma = self.text_content_BanMa02.toPlainText()
        n = int( self.text_Input_n.toPlainText() )
        d = int( self.text_Input_d.toPlainText() )

        text_ban_ro = RSA.GiaiMa_String( text_ban_ma, n , d )

        self.text_content_BanRo02.setText( text_ban_ro )

        AES_tool.Save_To_Word_File(text_ban_ro, 'Key_SauGiaiMa.docx')

        mess = QMessageBox()
        mess.setText("Nội dung bản rõ đã lưu vào Key_SauGiaiMa.docx")
        mess.exec_()

def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()

if __name__ == '__main__':
    main()


