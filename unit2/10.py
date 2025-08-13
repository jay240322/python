from employee import *
basic = float(input("enter the basic salary:"))

gross = basic + da(basic) + hra(basic)
print("gross salary is:{:10.2f}".format(gross))

net = gross - pf(basic) - itax(gross)
print("net salary:{:10.2f}".format(net))