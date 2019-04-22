filename = "learning_python.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

python_learned = ''
for line in lines:
   python_learned += line

print(python_learned)
print(len(python_learned))


print("=================")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
