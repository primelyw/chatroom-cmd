HEAD = b'\x00'*3+b'\x01'*2+b'\x00'*3
TAG = (b'\x00'*4+b'\x01'*4)*2
TAIL = b'\x01'*3+b'\x00'*2+b'\x01'*3
CRT = b'\x01\x00'*4
FCS = b'\x01\00'*8

def toframe(s):
    ans = []
    if len(s)%48 !=0:
        s += b'\x01'*(48-len(s)%48)
    n = len(s)//48
    for i in range(n):
        ans.append(TAG+CRT+s[i*48:i*48+48]+FCS+TAG)
    '''
    for i in ans:
        print(i)
    '''
    return ans

def tobits(a):
    #a = bytes(a,'utf-8')
    ans = ''
    for i in a:
        d = bin(i)[2:].zfill(8)
       # print('%x : %s'%(i,d))
        ans += d
    ans2 = ''
    for i in ans:
        if i=='0':
            ans2 += '\x00'
        else:
            ans2 += '\x01'
    ans2 = bytes(ans2,'utf-8')
    return ans2

def unframe(s):
    ac = b''
    for i in range(6):
        ok = True
        for j in range(8):
            if s[i*8+j] == 0:
                ok = False
        if ok == True:
            return ac
        else:
            ac += s[i*8:i*8+8]
    return ac
def get_msg(a):
    n = len(a)//8
    ans = b''
    ans2 = b''
    for i in range(n):
        sub = b''
        for j in range(8):
            if(a[i*8+j]==1):
                sub += b'1'
            else:
                sub += b'0'
        #print('subint: %d'%int(sub,2))
        sub = int(sub,2).to_bytes(1,'big')
        ans += sub
    ans = ans.decode('utf-8')
    return ans

def match(hd,tl,lim):
    ans = []
    for i in tl:
        for j in hd:
            if i-j == lim+8:
                ans.append((i,j))
    return ans
    

def find_sub(a,b):
    lena = len(a)
    lenb = len(b)
    ac = []
    for i in range(lena-len(b)):
        #print(a[i:i+lenb],b)
        if(a[i:i+lenb]==b):
           #print('shot!')
            ac.append(i)
    
    return ac
    

if __name__ == '__main__':
    s = input()
    s = tobits(s)
   # print(s)
    s = get_msg(s)
    print(s)
    
    
