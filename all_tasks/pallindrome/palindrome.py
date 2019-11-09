#Function for checking palindrome
def is_palindrome(string):
    string = string.lower()
    reverse_string = string[::-1]
    if reverse_string == string:
        print("Palindrome")
    elif reverse_string != string:
        print("Not Palindrome")
    else:
        print("Incorrect Input")

#taking string as an input
string = input("enter the string: ")


#calling the is_palindrome function
is_palindrome(string)
