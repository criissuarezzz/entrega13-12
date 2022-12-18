#secuencia de fibonacci con memoria caché privada
import sys
sys.set_int_max_str_digits(2000000)
n= int(input("ingrese un numero: "))
def fib(n):
    if n in fib.cache:
        return fib.cache[n]
    if n == 0:
        fib.cache[0] = 0
        return 0
    elif n == 1:
        fib.cache[1] = 1
        return 1
    else:
        fib.cache[n] = fib(n-1) + fib(n-2)
        return fib.cache[n]
fib.cache = {}
if __name__=="__main__":
    print(fib(n))   
