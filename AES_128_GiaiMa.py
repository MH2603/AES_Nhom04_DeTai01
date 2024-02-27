import MoRongKey as KeyTool
import AES_128_MaHoa as MaHoaTool

# Gồm 4 phép:
    # - Inverse Shift Row (Step 01)
    # - Inverse Sub Bytes (Step 02)
    # - Add Round key     (Step 03)
    # - Inverse Mix Columns (Step 04)


def Inverse_Shift_Row(hex_list):

    inverse_SR_matrix = [ [0  , 4  , 8 , 12],
                          [13 , 1  , 5 , 9 ],
                          [10 , 14 , 2 , 6 ],
                          [7  , 11 , 15, 3 ]
                        ]

    hex_list_SR = [ ]
    for col in range( 4 ):
        for row in range( 4 ):
            hex_list_SR.append( hex_list[ inverse_SR_matrix[row][col] ] ) 

    hex_list_SR = KeyTool.CheckLenFour(hex_list_SR)

    return hex_list_SR


def Inverse_Sub_Byte(hex_list):

    InverseSubBytes = [
            [ 0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB ],
            [ 0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB ],
            [ 0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E ],
            [ 0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25 ],
            [ 0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92 ],
            [ 0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84 ],
            [ 0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06 ],
            [ 0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B ],
            [ 0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73 ],
            [ 0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E ],
            [ 0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B ],
            [ 0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4 ],
            [ 0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F ],
            [ 0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF ],
            [ 0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61 ],
            [ 0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D ]
        ]

    hex_list_sub = []

    for i in hex_list:
        row = list(i)[2]
        col = list(i)[3]

        row = int(row, 16)
        col = int(col, 16)

        hex_list_sub.append( hex(InverseSubBytes[row][col]) )
        #print("S Box: ", row ,"--", col ," : ", S_BOX[row][col])

    hex_list_sub = KeyTool.CheckLenFour(hex_list_sub)
    
    return hex_list_sub 


def Inverse_Mix_Columns(hex_list, last_round):
    hex_matrix = []
    hex_matrix.append( [hex_list[0], hex_list[4], hex_list[8], hex_list[12]] )
    hex_matrix.append( [hex_list[1], hex_list[5], hex_list[9], hex_list[13]] )
    hex_matrix.append( [hex_list[2], hex_list[6], hex_list[10], hex_list[14]] )
    hex_matrix.append( [hex_list[3], hex_list[7], hex_list[11], hex_list[15]] )

    # hex_matrix.append( hex_list[0:4] )
    # hex_matrix.append( hex_list[4:8] )
    # hex_matrix.append( hex_list[8:12] )
    # hex_matrix.append( hex_list[12:16] )


    MC_matrix = [   ['0x0E','0x0B','0x0D','0x09'],
                    ['0x09','0x0E','0x0B','0x0D'],
                    ['0x0D','0x09','0x0E','0x0B'],
                    ['0x0B','0x0D','0x09','0x0E'] 
                ]


    if last_round == False:
        hex_matrix_MC = MaHoaTool.PhepNhan_Hex_Matrix( MC_matrix, hex_matrix)
    else :
        hex_matrix_MC = hex_matrix

    # hex_list_MC = hex_matrix_MC[0] + hex_matrix_MC[1] + hex_matrix_MC[2] + hex_matrix_MC[3]
    hex_list_MC = []
    for col in range( 4 ) :
        for row in range( 4 ):
            hex_list_MC.append( hex_matrix_MC[row][col] )

 
    hex_list_MC = KeyTool.CheckLenFour(hex_list_MC)
    return  hex_list_MC

def GiaMa_128bit( banMat, key):
    banMat = KeyTool.Text_To_HexList(banMat)

    key_mo_rong = KeyTool.MoRongKhoa(key)

    banMat = MaHoaTool.Add_Round_Key(banMat, key_mo_rong[9] )

    for key_con in reversed(key_mo_rong) :
        if key_mo_rong.index(key_con) < 9:
            # print("\n", "---- ", key_mo_rong.index(key_con))

            banMat_SR = Inverse_Shift_Row(banMat)
            # print("Shift Row: ", KeyTool.ListHex_To_Str(banMat_SR) )

            banMat_SB = Inverse_Sub_Byte(banMat_SR)
            # print("Sub Bytes: ", KeyTool.ListHex_To_Str(banMat_SB) )

            banMat_ARK = MaHoaTool.Add_Round_Key(banMat_SB, key_con)
            # print("Add Round: ", KeyTool.ListHex_To_Str(banMat_ARK) )

            banMat_MC = Inverse_Mix_Columns(banMat_ARK, False)
            # print("Mix Column: ", KeyTool.ListHex_To_Str(banMat_MC) )

            banMat = banMat_MC

    banMat_SR = Inverse_Shift_Row(banMat)
    banMat_SB = Inverse_Sub_Byte(banMat_SR)
    banMat_ARK = MaHoaTool.Add_Round_Key( banMat_SB, KeyTool.Text_To_HexList(key)  )
    
    return banMat_ARK

def Text_To_TextList16(text):
    text_list = list(text)
    num = len(text_list) % 16
    if num != 0:
        for i in range(16 - num):
            text_list.append(" ")

    ascii_list = [ord(i) for i in text_list]
    hex_list = [hex(i) for i in ascii_list]
    hex_list = [KeyTool.FixHexLen(i, 2) for i in hex_list]

    text_hex_matrix = []
    numFor = int(len(hex_list) / 16)
    for i in range(numFor):
        text = ''.join( x[-2:] for x in hex_list[i * 16:(i + 1) * 16])
        text_hex_matrix.append(text)

    return text_hex_matrix
def GiaiMa_Text( text, key):
    text_hex_list = []
    # text_hex_list = Text_To_TextList16( text )
    text = list(text)
    text_02 = ''
    for i in text:
        text_02 += i
        if len(text_02) == 32:
            text_hex_list.append(text_02)
            text_02 = ''
    # print(text_hex_list)

    hex_list = []
    for hex_text in text_hex_list:
        hex_list += GiaMa_128bit( hex_text, key)

    hex_text = ''.join( x[-2:] for x in hex_list)
    hex_text = list(hex_text)
    hex_list = []
    for i in range(len(hex_text)):
        if i % 4 == 0:
            hex_list.append('0x' + hex_text[i] + hex_text[i+1] + hex_text[i+2] + hex_text[i+3] )
    # print( len(hex_list), "---" , hex_list)

    text_ban_ro = ""
    for i in hex_list:
        text_ban_ro += chr( int(i,16) )

    return  text_ban_ro

banMat = "ff0b844a0853bf7c6934ab4364148fb9"
key    = "0F1571C947D9E8590CB7ADD6AF7F6798"

text = "Nguyễn Minh Hải khoa công nghệ thông tin trường đại học công nghiệp hà nội"
# text = "Nguyen Minh Hai khoa cong nghe thong tin"
text_ban_ma = MaHoaTool.MaHoa_Text( text, key)
text_ban_ro = GiaiMa_Text( text_ban_ma, key)
#
# print("Text Ban Ma: ", text_ban_ma, "----", len(text_ban_ma))
# print("Text ban ro: ", text_ban_ro, "----", len(text_ban_ro))
