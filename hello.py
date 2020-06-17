from pickle import loads
from base64 import b64decode
from hashlib import sha1
from gzip import decompress
from typing import Callable
string = "08172146282106287"

print(string[1::2])

def checkType(targetType: object, obj: object) -> object:
    if not isinstance(obj, targetType):
        raise TypeError(f'Expected type {targetType} for {repr(obj)}"')
    return obj

def encrypt(number: int) -> int: return checkType(int, number) >> 23 ^ 2333

def solve(token: str) -> str:  
    print("-------")
    #print(token)
    #print(lock.tcdict )       
    a=int(token)
    tk=int(token)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    c1 = 0 
    c2 = 0
    for i in range(len(token)-1):
        b=a%10
        a=a//10
        sum1 = sum1+b
        if i == 1 :
            c1 = b 
        if i == len(token)-1:
            c2 = b 
    sum2 = c1 + c2      
    sum3 = sum1+sum2+encrypt(tk)
    if (sum3 < 674361) :
        return str(sum3)
    else:
        return str(sum3-78763)


print(solve('846843843840698406984039840698438436987698716698164515'))

# res='674359'

# print(sha1(res.encode('utf-8')).hexdigest())

a = 4
if a <=  4:
    print("ok")





