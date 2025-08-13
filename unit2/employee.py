# create a program name employee and implement the functions DA,HRA,PF, AND ITMAX create another program that usesthe function of employee module and calculate gross and net salaries of an employee
def da(basic):
    da = basic * 80/100
    return da

def hra(basic):
    hra = basic * 15/100
    return hra

def pf(basic):
    pf = basic * 12/100
    return pf

def itax(gross):
    tax = gross * 0.1
    return tax