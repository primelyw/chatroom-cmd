def tobits(a):
    a = bytes(a,'utf-8')
    ans = ''
    for i in a:
        d = bin(i)[2:].zfill(8)
        print('%x : %s'%(i,d))
        ans += d
    ans2 = ''
    for i in ans:
        if i=='0':
            ans2 += '\x00'
        else:
            ans2 += '\x01'
    ans2 = bytes(ans2,'utf-8')
    return ans2

def get_msg(a):
    n = len(a)//8
    ans = b''
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

    
