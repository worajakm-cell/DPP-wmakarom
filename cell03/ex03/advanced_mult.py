import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()

num1 = 0  
while num1 <= 10:
    print(f"Table de {num1}:", end="")
    num2 = 0  
    while num2 <= 10:
        print(f" {num1 * num2}", end="")
        num2 += 1
    print() 
    num1 += 1