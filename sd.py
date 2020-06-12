def reverse(s):
    return s[:: -1]
def palindrome(s):
    rev = reverse(s)
    if ( s == rev):
        return True
    return False
s = input("enter string to reverse:")
s = reverse(s)
ans = palindrome(s)
if ans == 1:
    print("your palindrome is:", s)
else:
    print("not palindrome:", s)
