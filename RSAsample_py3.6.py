import random

def gcd(a, b): #유클리드 호제법 사용
    while b!=0:
        a, b = b, a%b
    return a

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext] #복호화
    return "".join(plain)

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext] #암호화
    return cipher

def public_key(phi):
    e=None
    for i in range(2,phi):  #공개키 생성
        if gcd(phi,i)==1:
            e=i
            break
    return e

def private_key(e,phi):
    d=1
    while (e*d)%phi != 1 or d == e and (e*d)<=phi: #비밀키 생성
        d+=1 
    return d

candidates=[]
qend=int(input("소수 끝 범위 수 n 입력(10~n) : "))

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False     #소수 판별
    return True 

for i in range(10,qend):
    if(is_prime(i)):
        candidates.append(i)
        
print("candidates : ",candidates)
a,b = random.sample(range(0,len(candidates)),2) 
print("index : "+str(a),str(b))
p=candidates[a]
q=candidates[b]
print("p,q : "+str(p),str(q))
print("")
plain = input("암호화할 평문 입력 : ")

n = p*q

phi = (p-1)*(q-1)
print("phi: (p-1)*(q-1)= ", str(phi))
print("")

e = public_key(phi)
print("공개키(n, e):("+str(n)+","+str(e)+")")

d = private_key(e, phi)
print("비밀키(n, d):("+str(n)+","+str(d)+")")
print("")

encrypted_msg = encrypt((e,n), plain)
print('암호화된 평문 : ', ''.join(map(lambda x: str(x), encrypted_msg)))

print('복호화된 암호문 : ', decrypt((d,n),encrypted_msg))

input()
