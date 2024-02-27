import random

p = 0
q = 0
n = 0
Phi_N = 0
e = 65537
d = 0

def IsSNT(n):
    if n <= 1:
        return False
    if n == 2: 
        return True
    
    for i in range(2, n):
        if n % i == 0 : 
            return False
    
    return True

# print("So NT: ", IsSNT(13) )

def FindListSNT(min, max):
    listSNT = []
    for i in range(min, max):
        if IsSNT(i):
            listSNT.append(i)

    return listSNT


def Find_P_Q_N_Phi_N():
    min = 100
    max = 200

    listSNT = []
    listSNT = FindListSNT( min, max)
    #print("List SNT: ", listSNT)

    #index = int(len(listSNT)/2) 
    index = random.randint( 1, len(listSNT))

    global p
    global q

    p = listSNT[index]
    q = listSNT[index + 1]

    global n
    global Phi_N

    n = p*q
    Phi_N = (p-1)*(q-1)

    print(" --> Complete Find_P_Q_N_PHI_N !!!")

def Chose_P_Q( min, max):
    listSNT = FindListSNT(min, max)
    index = random.randint(1, len(listSNT))

    p = listSNT[index]
    q = listSNT[index + 1]

    p_q_list = [ p, q]

    return  p_q_list

def GCD(A,B):
    max = 0
    if A > B:
        max = B + 1
    else:
        max = A + 1
    gcd = 1
    for i in range(2,max):
        if A % i == 0 and B % i == 0 :
            gcd = i
    return gcd

def Find_N_Phi_N( q, p ):
    n = p * q
    phi_n = (p-1)*(q-1)

    list_n_Phi_N = [ n, phi_n]

    return list_n_Phi_N

def Find_E(phi_N):

    e = random.randint(2, phi_N)
    while GCD(e,phi_N) != 1:
        e = random.randint(2, phi_N)

    return  e
    
def Find_NgichDo(a,n):
    num = 0
    for i in range(1,n):
        if i * a % n == 1 :
            return i
          
    return 0

def Find_d( e, phi_n):

    d = Find_NgichDo(e, phi_n)

    return  d

# Find_P_Q_N_Phi_N()
# d = Find_NgichDo(e, Phi_N)

def PublicKey():
    
    public_key = []
    global n
    global e
    global Phi_N

    if GCD(e, Phi_N) != 1 and e < Phi_N:
        print("e và phi_n ko nguyên tố cùng nhau ???")
    else :
        print("e thoã mãn")

    public_key.append(n)
    public_key.append(e)

    return public_key

def PrivateKey():

    global n
    global d

    private_key = [ n , d]

    return private_key


print("public : ", PublicKey() )
print("private : ", PrivateKey() )



