#print numbers from 1 to 30.
#for each multiple of three, write Fizz. For five write Buzz.
#for both, write FizzBuzz * SUCCESS *

txt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
       21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
list_str = []
separator = " "

def fizzBuzz(a):
    for i in range(len(a)): #easier to iterate
        if a[i] % 3 == 0 and a[i] % 5 != 0:
           a[i] = "Fizz"  #use the [i] to refer back to a list index  
           list_str.append(str(a[i]))    
        elif a[i] % 5 == 0 and a[i] % 3 != 0:
            a[i] = "Buzz"
            list_str.append(str(a[i]))  
        elif a[i] % 5 == 0 and a[i] % 3 == 0:
            a[i] = "FizzBuzz"
            list_str.append(str(a[i]))  #appends a[i] (now string) into a different list.
        else:
            list_str.append(str(a[i]))  
        
            
    print(separator.join(list_str)) #cool built-in funct that turns a list into a string! (only accepts str tho)


fizzBuzz(txt)
