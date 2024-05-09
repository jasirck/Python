
s="a"
k=1
string=str()
sum=int()
for i in s:
    va=ord(i)-96
    string+=str(va)
    print(string,"str")
for j in range(1,k+1):
    sum=0
    for i in string:
        sum+= int(i)
        print(sum,"sum")
    string=str(sum)
print(int(string))