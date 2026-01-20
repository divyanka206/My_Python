# Slicing in strings:
#
# | Code      | Meaning                 |
# | --------- | ----------------------- |
# | s[a:b]    | from index `a` to `b-1` |
# | s[:b]     | from start to `b-1`     |
# | s[a:]     | from `a` to end         |
# | s[::-1]   | reverse string          |
# | s[::n]    | every `n`th character   |

#Negative Index:
# Index = -5 -4 -3 -2 -1
# String = A  P  P  L  E
# -ve index starts with -1


name = "Saumya@heh"
print(name[0:6])
#output = Saumya

email = "meaw@gmail.com"
print(email[:10])
#output = meaw@gmail

address = "mars_basoomcolony"
print(address[0:])
#output = "mars_basoomcolony"

str1 = "palindrome"
print(str1[::-1])
#output = emordnilap

str2 = "PYTHON"
print(str2[::2])
#output = PTO

str3 = "i am a coder"
print(str3[-7:-1])
#output = a code

