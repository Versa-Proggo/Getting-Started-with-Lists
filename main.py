empty_l = []
e_L_2 = list()
print(f"{empty_l}, {e_L_2}")
num = [1,2,3,4,5]
h_l = [1,"Hello", 3.14159265, True,[1,2,3]]
fruits = ["apple","banana","cherry","orange"]
print(fruits[0])
print(fruits[-1])
num = [0,1,2,3,4,5,6,7,8,9]
print(num[2:6])
print(num[:6])
print(num[6:])
print(num[::2])
print(num[::-1])
fruits[-1] = "Dates"
print(fruits)
fruits.append('Mango')
print(fruits)
fruits.insert(2,"Jackfruit")
print(fruits)
fruits.extend(["Tomato","Cucumber",'Carrot'])
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)
fruits.remove("Jackfruit")
print(fruits)
del fruits[1]
print(fruits)
# fruits.clear()
# print(fruits)
print(len(fruits))
print(fruits.index('apple'))
