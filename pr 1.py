#problema 1 din olimpuida de clasa 9a 
p=int(input("Introdu nr total de pasari:"))
print(p,"păsări")
if  p%2==0:
    g=p/2
    print(g,"gaini")
else:
    g=int(p/2)
if g%4==0:
    r=g/4
    print(r,"rate")
else:
    r=int(g/4)
c=p-g-r
print(c,"gaste")