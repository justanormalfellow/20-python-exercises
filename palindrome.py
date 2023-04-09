#a program that checks if a given string is a palindrome or not.

word = input("Write a word: ")

def palindromecheck(a):
    display = a

    if " " in a:        #removes any whitespace
        a = a.replace(" ", "")

    reverse_word = ""

    for i in range(len(a) - 1, -1, -1): #Loops through our word backwards
        reverse_word += a[i]            

    if a == reverse_word:
        print(f"\n\"{display}\" is a palindrome!")
    else:
        print(f"\n\"{display}\" is  not a palindrome.")

    
palindromecheck(word)