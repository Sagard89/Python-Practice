#Creating list of even numbers from 0 to 20
list1 = [x for x in range(21) if (x%2 == 0)]
print(list1)

#Creating list of squares of numbers from 0 to 20
list2 = [x**2 for x in range(0,21)]
print(list2)

#Concatenation of list
list3 = list1 + list2
print(list3)

#Creating list of 4 elements of value 1
list4 = [1] * 4
print(list4)

#Checking whether 49 is a member of list list2
isTrue = 49 in list2
print(isTrue)

#Length of list list2
lenList2  = len(list2)
print(lenList2)

#returns element with maximum value from list1
a = max(list1)
print(a)

#In Python3.x following gives error
b = [ 1, "Abc", 3]
#a = max(b)
#print(a)

#Convert tuple into list
tu = (1,"A",2,3)
b = list(tu)
print(b)

#Append element to the end of the list
list1.append(1)
print(list1)

#Find the number of occurences of 1 in list4
a = list4.count(1)
print(a)

#Find the lowest index of 4 in list3
a = list3.index(4)
print(a)

#Insert an element at index 2 of list4
list4.insert(2,8)
print(list4)

#Remove the first occurrence of 8 in list4 
list4.remove(8)
print(list4)

#Delete the element at index 1 of list b
del b[1]

#return the removed element from the index 1 from list b
a = b.pop(1)
print(a)

#Reverse a list
list2.reverse()
print(list2)

#Sort a list in ascending order
list3.sort()
print(list3)

#Sort a list in descending order
list3.sort(reverse=True)
print(list3)

#Sort a list having mixed types gives error in Python3.x
b = [ 3, "Abc", 1]
b.sort()
print(b)
