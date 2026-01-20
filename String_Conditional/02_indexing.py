# Indexing starts from 0
#
# Index : 0 1 2 3 4 5 6 7 8 9
# String: C O L A G E _ Y o u
#
# str[0] = C (output)
# str[6] = _ (output)

str = "meaw_haha"
print(str[4])    #output = _

str = "yoyo_blo"
str[4] = @
print(str[4])   #output = error(str dosent support item assignment)


