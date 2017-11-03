list1 = [1, [2,3], 4, [[6,7]]]
 	list2= [list1[0], list1[1][0], list1[1][1], list1[2], list1[3][0][0], list1[3][0][1]]
 	print(list2)


list1 = [1, [2,3], 4, [[6,7]]]
str1 = str(list1)
str2 = str1.replace('[', '').replace(']','')
 