def check_fermat_theorem(a,b,c,n):
    if n > 2 and a**n + b**n == c**n:
        print("holy smokes,fermat was wrong!")
    else:
        print("no,that dosen't work")

def checking():
    a = input("enter a value of a:")
    b = input("enter a value of b:")
    c = input("enter a value of c:")
    n = input("enter a value of n:")

    check_fermat_theorem(int(a),int(b),int(c),int(n))

checking()
