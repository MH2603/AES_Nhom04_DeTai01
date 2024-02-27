import Key_RSA as key
import AES_main as AES_tool
import  MoRongKey as Key_AES_tool

# public_key = key.PublicKey()
# private_key = key.PrivateKey()

def Find_NghichDao(a,n):

    for i in range(1,n):
        if i * a % n == 1 :
            return i
        
    return 0

def Abs(a,n):
    num = 1
    for i in range(n):
        num *= a
    return num

print("Mu: " , Abs(2, 3))

def MaHoa( M, n, e):

    c = Abs(M, e) % n

    return c

def GiaiMa( c, n, d):
    m = Abs(c,d) % n

    return m

def MaHoa_String(banRo, n , e):
    
    banRo = [ord(char) for char in banRo]
    # print(" Index Ban RO: ", banRo)

    index_banMa = []
    for i in banRo:
        int_MaHoa = MaHoa(i, n, e)
        text_hex = Key_AES_tool.FixHexLen( hex(int_MaHoa) , 4)
        index_banMa.append( text_hex )

    text_hex_banma = ""
    for i in index_banMa:
        for j in list(i)[2:]:
            text_hex_banma += j

    return text_hex_banma
    
def GiaiMa_String( banMa, n , d):
    banMat_list = []
    banMa = list(banMa)
    for i in range( len(banMa) ):
        if i % 4 == 0:
            hex_value = '0x' + banMa[i] + banMa[i + 1] + banMa[i + 2] + banMa[i + 3]
            banMat_list.append( int(hex_value,16) )

    index_banRo = []
    for i in banMat_list:
        index_banRo.append( GiaiMa(i, n, d) )
    
    # print("index ban ro: ", index_banRo)

    banRo = ''.join(chr(unicode_value) for unicode_value in index_banRo)

    return banRo

list_p_q = key.Chose_P_Q( 100, 200)
p = list_p_q[0]
q = list_p_q[1]

list_n_phiN = key.Find_N_Phi_N(p,q)
n = list_n_phiN[0]
phi_n = list_n_phiN[1]

e = key.Find_E(phi_n)
d = key.Find_d(e,phi_n)


banMa = MaHoa_String("Nguyễn Minh Hải ", n , e)
print("Ban ma: ",  banMa)
print("Ban ro: ", GiaiMa_String( banMa , n, d) )
