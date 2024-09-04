def remove_char(s, index):
    result = s[0: index ]
    return result
s = input("Enter any String ")
n = int(input("Enter any number "))
ans = remove_char(s,n)
print(ans)