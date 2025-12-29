n = int(input("Enter Any Number that You Want To find palindrome ------> "))
temp = n
rev = 0

while n > 0:
    sum = n % 10
    rev = rev * 10 + sum
    n = n // 10

if temp == rev:
    print("Palindrome --->", rev)
else:
    print("Not Palindrome --->", rev)
