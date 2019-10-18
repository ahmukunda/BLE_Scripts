import hmac
import hashlib
import random

random_num = random.randint(11111111,99999999)
local_macid = str(input("Enter MAC ID \n"))
combstring = str(random_num) + local_macid
keyPlusMac = bytes(combstring ,encoding="ascii")
print("Random Number: "+ str(random_num))
print('Random Number with Mac: ',end=' ')
print(keyPlusMac)
dk = hmac.new(b'oyo-mesh',msg=keyPlusMac,digestmod=hashlib.sha256)
print("Hashed Value is: ",end=' ')
print(dk.hexdigest())
