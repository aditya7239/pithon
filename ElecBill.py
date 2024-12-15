a=int(input("Enter Electricity Units consumed: "))
if(a<=50):
    b=(0.5*a)
elif(a>50 and a<=150):
    b=((0.5*50)+ 0.75*(a-50))
elif(a>150 and a<=250):
    b=(((0.5*50)+ 0.75*(150-50)))+ (1.2*(a-150))
else:
    b=(((0.5*50)+ 0.75*(150-50)+1.2*(150)))+ (1.5*(a-250))
c= ((1/5)*b)+b
print("Base Bill =", b)
print("Total Bill (Including Taxes) = ", c)