#takes a list of numbers and prints the sum of the square
#of those numbers. 

num_list_str = input("Give a list of numbres (separated by whitespaces): ")
num_list = num_list_str.split(sep=" ")  #separates the input into a list.


def sumofsqur(a):
    s = 0

    for i in range(len(a)):     #loops through the list,
        a[i] = float(a[i])      #turns all items to float,
        s += (a[i])**2          #gives the sum.
    
    print(f"sum of the squared numbers is {s}")


sumofsqur(num_list)
