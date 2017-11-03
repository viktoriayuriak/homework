str1 = '((((((((((((((2,3))))))))))))))'
str2 = '('
str3 = ')'
result1 = str1.count(str2, 0, len(str1))
result2 = str1.count(str2, 0, len(str1))

def is_greater(x, y):
    if x > y:
       return True
    else:
       return False

print (is_greater(result1, result2))
