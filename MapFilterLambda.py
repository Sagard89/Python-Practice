#returns cube of x

def cube_of_number(x):

   return x ** 3



#returns boolean

def test_even_number(x):

  return x%2==0


li = [1,2,3,4,5,6,7,8,9,10]


li1 = list(map(cube_of_number,li))

print(li1)



li2 = list(filter(test_even_number,li))

print(li2)



li = [1,2,3,4,5,6,7,8,9,10]

li1 = list(map(lambda x: x ** 3,li))

print(li1)

li2 = list(filter(lambda x: x % 2,li))

print(li2)