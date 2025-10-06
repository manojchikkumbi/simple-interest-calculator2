p-float(input("Enter Principle amount:"))
r-float(input("Enter rate of interest:"))
t-int(input("Enter time (in years):"))
si-(p*t*r)/100
c=p*(1+r/100)**t
print("compound interest is:",ci)
print("Simple interest is:",si)
