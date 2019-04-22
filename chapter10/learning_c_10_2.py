filename = "learning_python.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

res = ''
for line in lines:
    res += line.replace('python', 'c++')

print(res)

