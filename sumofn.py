#write a program that takes n and gives the sum of 1 to n

print("Gets any number n and prints it's sum.\n")

n = float(input("Give a number: "))

def sumofn(a):
    i = a * (a+1)/2
    print(f"sum of 1 to {a} is {i}")

    
sumofn(n)



    