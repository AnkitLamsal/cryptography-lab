def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a,a)
a  =  int(input("Enter the value of A:"))
b =  int(input("Enter the value of B:"))
r =  gcd(a,b)
print("Greatest Common Divisior of a and b is:"+str(r))

