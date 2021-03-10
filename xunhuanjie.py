# -*- coding: utf-8 -*-

CHUFAJINGDU = 2000
MAXLEN = 50
next = []
type = ['no','pure','hun']
flag = 0
def getnext(b):
    i = 0
    j = -1
    l = len(b)
    next = []
    for zz in range(0, MAXLEN):
        next.append(-1)
    while (i < l):
        if (j == -1 or b[i] == b[j]):
            i = i + 1
            j = j + 1
            next[i] = j
        else:
            j=next[j]

def hdiv(dividend, divisor, precision=0):
    """高精度计算除法，没有四舍五入
    @author: cidplp
    @param dividend:被除数
    @type dividend:int
    @param divisor:除数
    @type divisor:int
    @param precision:小数点后精度
    @type precision:int
    @return:除法结果
    @rtype:str
    """

    if isinstance(precision, int) == False or precision < 0:
        print('精度必须为非负整数')
        return

    a = dividend
    b = divisor

    #有负数的话做个标记
    if abs(a+b) == abs(a) + abs(b):
        flag = 1
    else:
        flag = -1

    #变为正数，防止取模的时候有影响
    a = abs(a)
    b = abs(b)

    quotient = a // b
    remainder = a % b

    if remainder == 0:
        return quotient

    ans = str(quotient) + '.'
    i = 0
    while i < precision:
        a = remainder * 10
        quotient = a // b
        remainder = a % b
        ans += str(quotient)
        if remainder == 0:
            break
        i += 1

    if precision == 0:
        ans = ans.replace('.', '')

    if flag == -1:
        ans = '-' + ans
    return ans

def rwh_primes1(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * int(n/2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * (int((n-i*i-1)/(2*i))+1)
    return [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]]

def get_circle(n):
    result = hdiv(1, n, 20)
    if str(result).find('.') == -1:
        return '0'
    a = str(result).split('.')
    getnext(a[1])
    print("the next is %s"%next)
    l = len(a[1])
    if(l%(l-next[l]) == 0):  #说明从开始判断到结束有循环节 
        print("%d "%(l-next[l]))    #循环节的长度 
        for i in range(0, (l-next[l])):
            print("the loop body is %s"%a[i])        #循环节的组成
        print("the loop times is %d"%(l/(l-next[l])))    #循环了几次 
    else:
        print("%d "%l)         #如果没有循环节，字符串的长度就是循环节的长度
        for i in range(0, l):
            print("the loop body is %s"%a[i])
            print("loop times is once")        #只循环一次
    return result

def get_circle2(e, n):
    result = hdiv(e, n, CHUFAJINGDU)
    global flag
    if str(result).find('.') == -1:
        flag = 0
        return str(result)
    a = str(result).split('.')
    if len(a[1]) < CHUFAJINGDU:
        flag = 0
        return a[0] + '.' + a[1]
    for i in range(0, CHUFAJINGDU):
        for looplength in range(i + 1, CHUFAJINGDU):
            if a[1].count(a[1][i:looplength]) == 1:
                flag == 2
                continue
            if a[1].count(a[1][i:looplength]) >= (CHUFAJINGDU - i)/(looplength - i):
                if ((a[1].find(a[1][i:looplength],i)+looplength-i) == (a[1].find(a[1][i:looplength], i + 1))):
                    if i == 0:
                        flag = 1
                        return a[1][i:looplength]
                    else:
                        flag = 2
                        return a[1][0:i] + '+' + a[1][i:looplength]
    return('NO Found!!!')

max = 20

prime_list = rwh_primes1(max)
#for i in range(0, len(prime_list)):
    #print("%-5d %-50s"%(prime_list[i],get_circle(prime_list[i])))



for i in range(1, max):
    loop = get_circle2(1, i)
    if (loop.find('.') != -1):
        looplen = 0
    elif (loop.find('+') != -1):
        looplen = len(loop.split('+')[1])
    else:
        looplen = len(loop)
    print("%-5d, %-5s, %-32s, %-5d, %-30s"%(i, type[flag], hdiv(1, i, 30), looplen, loop))
    #print("the loop body is : %s"%get_circle2(i))


exit()
for i in range(1, 20):
    for j in range(1, 20):
        loop = get_circle2(j, i)
        if (loop.find('.') != -1):
            looplen = 0
        elif (loop.find('+') != -1):
            looplen = len(loop.split('+')[1])
        else:
            looplen = len(loop)
        print("%-5d, %-5s, %-32s, %-5d, %-30s"%(i, type[flag], hdiv(j, i, 30), looplen, loop))