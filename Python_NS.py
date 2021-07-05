import hashlib
st=input("Enter Input String:\t")
result=hashlib.md5(st.encode())
print("md5 Encryption       : {}".format(result.hexdigest()))
result=hashlib.sha1(st.encode())
print("sha1 Encryption      : {}".format(result.hexdigest()))
result=hashlib.sha224(st.encode())
print("sha224 Encryption    : {}".format(result.hexdigest()))
result=hashlib.blake2b(st.encode())
print("blake2b Encryption   : {}".format(result.hexdigest()))

