HEAD = b'\x00'*3+b'\x01'*2+b'\x00'*3
TAG = (b'\x00'*4+b'\x01'*4)*2
TAIL = b'\x01'*3+b'\x00'*2+b'\x01'*3
ACK0 = b'\x01\x00'*4
ACK1 = b'\x00\x01'*4
FCS = b'\x01\00'*8


def check2(s):
    fcs = b''
    gcnt = 0
    for i in range(7):
        cnt = 0
        for j in range(8):
            if(s[i*8+j] == 1):
                gcnt += 1
                cnt += 1
        if cnt%2==0:
            fcs += b'\x00'
        else:
            fcs += b'\x01'
    for i in range(8):
        cnt = 0
        for j in range(7):
            if s[j*8+i] == 1:
                cnt += 1
        if cnt%2 ==0:
            fcs += b'\x00'
        else:
            fcs+= b'\x01'
    if gcnt%2 ==1:
        fcs += b'\x01'
    else:
        fcs += b'\x00'
    print('check2: %s'%fcs)
    return fcs

    

def toframe(s,ack):
    ans = []
    if len(s)%48 !=0:
        s += b'\x01'*(48-len(s)%48)
    n = len(s)//48
    for i in range(n):
        ff = ''
        if(ack == 1):
            ele = ACK1+s[i*48:i*48+48]
            fcs = check2(ele)
            ff = TAG+ele+fcs+TAG
        else:
            ele = ACK0+s[i*48:i*48+48]
            fcs = check2(ele)
            ff = TAG+ele+fcs+TAG
        ans.append(ff)

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
    s = tobits(input().encode())
    s = toframe(s,0)
    print(s)

    
    
    
