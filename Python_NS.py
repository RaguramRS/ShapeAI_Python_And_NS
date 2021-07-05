import hashlib
st=input("Enter Input String:\t").encode()
res=hashlib.md5(st)
print("md5 Encryption       : {}".format(res.hexdigest()))
res=hashlib.sha1(st)
print("sha1 Encryption      : {}".format(res.hexdigest()))
res=hashlib.sha224(st)
print("sha224 Encryption    : {}".format(res.hexdigest()))
res=hashlib.blake2b(st)
print("blake2b Encryption   : {}".format(res.hexdigest()))

