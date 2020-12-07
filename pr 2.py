#problema 2 din olimpiada de clasa 9a 
a=int(input("introduceti numarul de alune:"))
if a%3==0:
    n=a/3
    print("fiecare purcel are",n,"alune")
else:
    n=a//3
    x=a-3*n
    print("fiecare purcel are",n,"alune")
    print("Rita are",x,"alune")