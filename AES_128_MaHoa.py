import MoRongKey as KeyTool

#gồm n vòng lặp:
    # - Sub_Byte: như phép sub_byte của Key
    # - ShiftRows : phép đảo thứ tự trong 1 list
    # - MixCol (Tại vòng thứ N bỏ phép này) : là hàm nhân ma trận với 'phép nhân (GF8)' và 'phép cộng ( phép XOR )'
    # - AddRoundKey: là phép XOR với khóa con

def Add_Round_Key( m , key_con):
    m_ARK = KeyTool.Phep_XOR( m, key_con)

    return m_ARK

def Sub_Bytes(hex_list):
    hex_list_SB = KeyTool.Sub_Bytes(hex_list)

    return hex_list_SB

def ShiftRows(hex_list):
    if len(hex_list) != 16 :
        print("--------> Bug Shift Row: sai độ dài list")
        
    
    SR_data = [ 0,4,8,12,
                5,9,13,1,
                10,14,2,6,
                15,3,7,11
              ]

    hex_list_SR = [hex_list[i] for i in SR_data]
    hex_list_SR = KeyTool.CheckLenFour(hex_list_SR)

    return hex_list_SR

# hex_list = KeyTool.Text_To_HexList("87F24D97EC6E4C904AC346E78CD895A6")
# hex_list_SR = ShiftRows(hex_list)
# print("---> SHift Rows: ", KeyTool.ListHex_To_Str(hex_list_SR), "--- "  )


def Mu(a,x):
    num = 1
    for i in range(x):
        num *= a
    return num

def PhepNhan_GF8( soNhan, hex_value):
    if soNhan == 1:
        return int(hex_value,16)
    
    if soNhan == 2:
        hex_result = 2 * int( hex_value, 16)
        if hex_result >= Mu(2,8):
            hex_result = hex_result ^ 283

        return hex_result
    
    if soNhan == 3:
        hex_result = 2 * int( hex_value, 16)
        if hex_result >= Mu(2,8):
            hex_result = hex_result ^ 283

        hex_result = hex_result ^ int( hex_value, 16)

        return hex_result

def multiply_in_GF(a, b):
    result = 0
    while a and b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B  # Đa thức modulo x^8 + x^4 + x^3 + x + 1
        b >>= 1
    return result

def PhepNhan_Hex_Matrix(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):

                # num = PhepNhan_GF8( int(matrix1[i][k], 16), matrix2[k][j] )
                num = multiply_in_GF( int(matrix1[i][k], 16) , int(matrix2[k][j],16)  )
                result[i][j] = result[i][j] ^  num

            # Chuyển đổi kết quả về dạng hex
            result[i][j] = hex(result[i][j]) 

    return result

def MixColumns(hex_list, last_round ):

    hex_matrix = []
    # hex_matrix.append( [hex_list[0], hex_list[4], hex_list[8], hex_list[12]] )
    # hex_matrix.append( [hex_list[1], hex_list[5], hex_list[9], hex_list[13]] )
    # hex_matrix.append( [hex_list[2], hex_list[6], hex_list[10], hex_list[14]] )
    # hex_matrix.append( [hex_list[3], hex_list[7], hex_list[11], hex_list[15]] )

    hex_matrix.append( hex_list[0:4] )
    hex_matrix.append( hex_list[4:8] )
    hex_matrix.append( hex_list[8:12] )
    hex_matrix.append( hex_list[12:16] )


    MC_matrix = [   ['0x02','0x03','0x01','0x01'],
                    ['0x01','0x02','0x03','0x01'],
                    ['0x01','0x01','0x02','0x03'],
                    ['0x03','0x01','0x01','0x02'] 
                ]


    if last_round == False:
        hex_matrix_MC = PhepNhan_Hex_Matrix( MC_matrix, hex_matrix)
    else :
        hex_matrix_MC = hex_matrix

    # hex_list_MC = hex_matrix_MC[0] + hex_matrix_MC[1] + hex_matrix_MC[2] + hex_matrix_MC[3]
    hex_list_MC = []
    for col in range( 4 ) :
        for row in range( 4 ):
            hex_list_MC.append( hex_matrix_MC[row][col] )

 
    hex_list_MC = KeyTool.CheckLenFour(hex_list_MC)
    return  hex_list_MC

# hex_list_MC = MixColumns(hex_list_SR)
# print("--> Mix Column : ", KeyTool.ListHex_To_Str(hex_list_MC), "---", len(hex_list_SR))


def MaHoa_128bit(banRo, key):
    banRo = KeyTool.Text_To_HexList(banRo)
    #key   = KeyTool.Text_To_HexList(key)

    key_mo_rong = KeyTool.MoRongKhoa(key)

    banMat = Add_Round_Key( banRo, KeyTool.Text_To_HexList(key) )
    # print("khoi tao ban ro: ", KeyTool.ListHex_To_Str(banMat) )
    
    for key_con in key_mo_rong:
        if key_mo_rong.index(key_con) < 9:
            # print("\n", "----- " , key_mo_rong.index(key_con) )

            banRo_SB = Sub_Bytes(banMat)
            # print("ban ro SubByte: ", KeyTool.ListHex_To_Str(banRo_SB))

            banRo_SR = ShiftRows(banRo_SB)
            # print("ban ro ShiftR : ", KeyTool.ListHex_To_Str(banRo_SR))

            banRo_MC = MixColumns(banRo_SR, False)
            # print("ban ro MixCol : ", KeyTool.ListHex_To_Str(banRo_MC))

            banRo_ARK = Add_Round_Key(banRo_MC, key_con)
            # print("ban ro AddRKey: ", KeyTool.ListHex_To_Str(banRo_ARK))

            banMat = banRo_ARK

        else :
            banRo_SB = Sub_Bytes(banMat)
            banRo_SR = ShiftRows(banRo_SB)
            banRo_MC = MixColumns(banRo_SR, True)
            banRo_ARK = Add_Round_Key(banRo_MC, key_con)

            banMat = banRo_ARK
        
    return banMat

def Doc_To_TextList16( text ):
    text_list = list(text)
    num = len(text_list) % 8
    if num != 0:
        for i in range(8 - num):
            text_list.append(" ")

    ascii_list = [  ord(i) for i in text_list ]
    hex_list = [ hex(i) for i in ascii_list ]
    hex_list = [ KeyTool.FixHexLen(i,4) for i in hex_list ]
    # print("step01: " , len(hex_list) , "---", hex_list)

    hex_text = ''.join(  x[-4:] for x in hex_list  )
    hex_text = list(hex_text)
    # print("step02: ", len(hex_text), "---", hex_text)

    hex_list = []
    numFor = int ( len(hex_text)/2 )
    for i in range(numFor):
        hex_list.append( hex_text[i*2] + hex_text[i*2 + 1]  )
    # print("step03: ", len(hex_list), "---", hex_list)

    text_hex_matrix = []
    numFor = int( len(hex_list)/16 )
    for i in range(numFor):
        text = ''.join( x for x in hex_list[i*16:(i+1)*16] )
        # print("Step 04: ", len(list(text)))
        text_hex_matrix.append(text)

    return  text_hex_matrix

def MaHoa_Text( text, key):
    text_hex_list = Doc_To_TextList16(text)
    # print("hex_list_ban_ro: ", text_hex_list)

    hex_list = []
    for hex_text in text_hex_list:
        hex_list += MaHoa_128bit(hex_text, key)

    # hex_text = ''.join(x[-2:] for x in hex_list)
    # hex_text = list(hex_text)
    # hex_list = []
    # for i in range(len(hex_text)):
    #     if i % 4 == 0:
    #         hex_list.append('0x' + hex_text[i] + hex_text[i+1] + hex_text[i+2]  +hex_text[i+3] )
    # print(hex_list)

    text_ma = ""
    for i in hex_list:
        # text_ma += chr( int(i,16) )
        text_ma += i[2] + i[3]
    # print(text_ma)

    return  text_ma

banRo = "0123456789ABCDEFFEDCBA9876543210"
key =   "0F1571C947D9E8590CB7ADD6AF7F6798"

# banRo = "3243f6a8885a308d313198a2e0370734"
# key =   "2b7e151628aed2a6abf7158809cf4f3c"

# banMat = MaHoa_128bit(banRo, key)
# print("Ban Ma: ", KeyTool.ListHex_To_Str(banMat) , "-----", len(banMat) )

text = "Nguyễn Minh Hải khoa công nghệ thông tin"

# textMaHoa = MaHoa_Text(text, key)
# print("Text Ma Hoa: " , textMaHoa)