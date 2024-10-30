#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

#from factorialIterativo import factorial 
from factorialRecursivo import factorial

def factorial(n):
    """Factorial recursivo"""
    if n == 0: return 1 
    if n == 1: return 1 
    return n * factorial (n-1)
     

if __name__ == "__main__":
    
    for i in range(500):
     print(i, factorial(i))
     print() #salto de linea
