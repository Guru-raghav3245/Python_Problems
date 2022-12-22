word = input("Input word - ")

rev = word[::-1]

if word == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")