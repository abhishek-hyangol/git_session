#tuple
#unlike list in tuple small bracket is used
#takes less memory
#empty tuple
fruits=()
print(fruits,type(fruits))

#empty tuple
fruits=tuple()
print(fruits,type(fruits))

fruits=('orange', 'lemon','grapes','apple')
print(fruits,type(fruits))

orange= fruits[0]
lemon=fruits[1]
grapes=fruits[2]

print(orange,lemon,grapes)

#slicing
summer_fruits=fruits[0:2]
print(summer_fruits)

winter_fruits=fruits[2:]
print(winter_fruits)

print(fruits[-2])

print(fruits[0:-2])

print(len(fruits))

#it is immutable but list is mutable
#error code
#fruits[0]='banana'
#print(fruits)