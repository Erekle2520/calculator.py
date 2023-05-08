#x=float(input("What is x? "))
#y=float(input("What is y? "))

#z=x+y
#print(f"{z:.2f}")
def main():
    x=float(input("What is x? "))
    print(square(x))

def square(n):
    result=n*n
    return round(result,2)

main()
