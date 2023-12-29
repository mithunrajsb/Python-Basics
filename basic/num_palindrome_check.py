
def reverse_num(num):
    reverse = 0

    while num > 0:
        digit = num%10
        reverse = reverse * 10 + digit
        num//=10
    return reverse


n = int(input("Enter an integer: "))

if n == reverse_num(n):
    print("It is a palindrome")
else:
    print("The number is not a palindrome")