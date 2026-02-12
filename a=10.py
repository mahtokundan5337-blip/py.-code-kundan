'''a=10
b=20
print(a+b) '''
'''a=10
b=3.14
c="python"
d=True

print(type(a))
print(type(b))
print(type(c))
print(type(d))'''
"""num = int(input("Enter number:"))

if num % 2 == 0:
    print("Even")
elsr:
    print("Odd")  """
'''a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)'''
#list
'''n=[10,20,30,40,50,]
print(n)
print ("first:"n=[0])

print ("last"n=[-1])'''
'''n=[1,2,3]
n.append(4)
print(n)'''
'''n=[1,2,3,4,5,6 ,7,8,9,10,11,12,13,14,15]
for n in n:
    if n %2==1:#odd number

     print(n)'''

#dictonary
'''student={"name","kundan","marks"}
print(student)


#dict..... loop
if"marks" in Student:
    print("marks exist")'''


#set
'''S={1,2,3,4}
print(S)
S.add(5)
print(S)
S.remove(2)
print(S)'''
''''#a={1,2,3,}
b={3,4,5,}
print(a|b)#'''
#tuple
'''t=(10,20,30)
print(t)

l=list(t)
print(l)'''

'''t=(1,2,3,2,2)
print(t.count(2))'''

"""for i in range(1,11):
    print(i)"""

'''for i in range (1,11):
    if i % 2==1:
        print(i)'''
'''total = 0
for i in range (1,11):
    total+=i
print("sum=",total)'''

'''n=5
for i in range(1,11):
    print(n,"x",i,"=",n*i)'''

'''for i in range(15,0,-1):
    print(i)'''

'''for i in range (15,0,-1):#reverse 
    print("*"* i)'''

'''n=int(input("enter the value"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("not prime")'''

n=10
a=0
b=1
'''for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c'''

'''n=54
c=0

while n>0:
    n//=10
    c+=1
print("digits",c)'''
n=123
rev=0

while n> 0:
 dight=n%10
 rev=rev*10+dight
 n//=10

print("rev",rev)