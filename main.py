from math import sqrt

a = float(input("Type a real number a: ")) # float: real numbers
b = float(input("Type a real number b: ")) # float: real numbers
c = float(input("Type a real number c: ")) # float: real numbers
if a==0: # Linear equation
    if b==0:
        if c==0:
            print("All solutions")
        else:
            print("No solution")
    else:
        x=-c/b
        print(f"x = {x}")
else: # Quadratic equation
    d=b**2-4*a*c
    if d>0: # Two real
        x1=(-b+sqrt(d))/(2*a)
        x2=(-b-sqrt(d))/(2*a)
        print(f"x1 = {x1}, x2 = {x2}")
    elif d==0: # One real
        x=-b/(2*a)
        print(f"x = {x}")
    else: # Two complex
        print("No real solution")
