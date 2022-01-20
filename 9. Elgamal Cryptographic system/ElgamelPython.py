from random import randint
print("Elgamel CryptoSystem")
print()

q=int(input("Enter a prime number for q: "))
g=int(input("Enter a primitive root for g: "))
m=int(input("Enter a message value for m: "))

xa=randint(1,q-2)

ya=pow(g,xa)%q

k=randint(1,q-1)
r=pow(ya,k)%q

c1=pow(g,k)%q
c2=(r*m) % q

print()
print()
print("Cipher Text: ",c1,",",c2)

