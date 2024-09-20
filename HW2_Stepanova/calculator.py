def  get_numbers():
    exp =input("Введите выражение: ")
    return exp
def operation(expression):
    a,oper,b=expression.split()
    a=float(a)
    b=float(b)
    return(a,b,oper)




