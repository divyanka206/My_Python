a = "2"
b = 4.25
sum = a+b     #TypeError: can only concatenate str (not "float") to str
print(sum)

#Therefore to fix it, we do manual conversion of data known as Casting

a = int ("2")   #converts str to int
b = 4.25
print(a+b)   #6.25 {float}


