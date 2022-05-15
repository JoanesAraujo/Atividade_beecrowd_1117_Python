a=float(input())
z=[]
if 1<=a<=10:
    z=z+[a]
else: 
    print ("nota invalida")
while len(z)<2:
    a=float(input())
    if 1<=a<=10:
        z=z+[a]
    else:
        print ("nota invalida")
x=sum(z)/len(z)
print ("media = %.2f" %x)