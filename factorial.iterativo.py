#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

def factorial(n):
    actual = n
    fact = n 
    while actual > 0:
        fact = fact * actual 
        actual = actual - 1
    return  fact

if __name__ == "__main__":
    
    x = 3
    print (factorial(x)) #6
    x = 2
    print (factorial(x)) #2
    x = 1
    print (factorial(x)) #1
    x = 0
    print (factorial(x)) #1