
c = '99.99'
a = '1947389'



#print(len(c))
try:
    d = float(c)
    if a.isdigit() and (d>=0 and d<=100):
        print("%s %.2ef"%(a,d))
    else:
        print("error")
except:
    print("Ingrese solo numeros")