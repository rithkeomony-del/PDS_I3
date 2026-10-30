def digit_sum(n):
    n = abs(n)
    total = 0
    while n > 0 :
        total += n%10
        n //= 10
    return total
def reverse_number(n):
    reverse_num = 0
    while n>0:
        digit = n%10
        reverse_num = reverse_num*10 + digit
        n //= 10
    return reverse_num
def is_palindrome(n):
    return n == reverse_number(n)

# a.Testing with 2026 12321 9875
List = [2026, 12321, 9875]

for num in List:
    print(f"{num:6} : {digit_sum(num):3} | {num:6} : {reverse_number(num):6} | {num:6} : ",is_palindrome(num))

# b. Count how many palindromes there are from 10 to 999.
count = 0
num = 10
while num<1000:
    if is_palindrome(num):
        count += 1
    num += 1
print(f"Palindromes from 10 to 999: {count}")