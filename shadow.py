num_array = list()
num = input("Enter how many elements you want:")
print ('Enter numbers in array: ')
for i in range(int(num)):
    n = input("num :")
    num_array.append(int(n))
for i in range(int(num)):
    print (num_array[i])
print('Arrays')