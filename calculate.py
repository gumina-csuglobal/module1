
def add(x,y):
    print(f"{x} + {y} = {x+y}")    

def subtract(x,y):
    print(f"{x} - {y} = {x-y}")    

def multiply(x,y):
    print(f"{x} * {y} = {x*y}")    

def divide(x,y):
    print(f"{x} / {y} = {x/y}")    

def prompt_numbers():
    prompt = "Please enter a number: "
    x = float(input(prompt))
    prompt = "Please enter another number: "
    y = float(input(prompt))
    return x,y

def main():
    x,y = prompt_numbers()
    add(x,y)
    subtract(x,y)
    multiply(x,y)
    divide(x,y)
    
if __name__ == "__main__":
    main()
