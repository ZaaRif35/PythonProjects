array = []
int_array = [3,4,5,6,7,87,8]
char_array = ["s","a","l","u","t"]
float_array = [5.4,34.5,6.2]
bool_array = [True, False, False, True]
print(int_array)
print(char_array)
print(float_array)
print(bool_array)
for i in range(0,6):
    print(int_array[i])

for i in range(0, len(char_array)):
    print(char_array[i])

for i in float_array:
    print(i)

for i in bool_array:
    print(i)

test = []
l = int(input("Enter the array lenght"))

for i in range(0,l):
    test.append(int(input('Enter element with index '
                          + str(i) + '\n')))

a =  [1, 1, 2, 5, 8, 13, 22, 34, 35, 2, 3]
print(a[3])
print(a[a[3]])