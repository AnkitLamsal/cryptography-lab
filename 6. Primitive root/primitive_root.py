a = int(input("Enter first number:"))
n = int(input("Enter second number:"))
flag = 0
r = list()
for i in range(1,n):
    x = (int)((a**i )%n)
    r.append(x)
    print(" {}^{} mod ({}) = {} \t".format(a,i,n,r[i-1]))

for i in range(1,n):
    for j in range(i+1,n):
        if(r[i-1]== r[j-1]):
            flag = 1;
if(flag == 0):
    print("{} and {} are primitively root".format(a,n))
else:
    print("{} and {} are not primitively root.".format(a,n))
