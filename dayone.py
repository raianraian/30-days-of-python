#python basics 
#using the 30 days of code challenge found at https://github.com/Asabeneh/30-Days-Of-Python along with my own knowledge

#basic print
print('Hi there')

#datetime
import datetime
x = datetime.datetime.now()
print(x)

#maths
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 % 3)
print(2 ** 3)
print(2 // 3)

#data type checking 
print(type(10)) #should return int
print(type(3.14)) #should return float
print(type(1 +3j)) #should return complex
print(type('RayRay')) #should return string
print(type([1, 2, 3])) #should return list
print(type({'name': 'RayRay'})) #should return dictionary
print(type({9.8, 3.14, 2.7})) #should return set