my_str = 'TestSlicingInPython'

print(my_str[my_str.index("test".capitalize()):my_str.index("slicing".capitalize())])
print(my_str[my_str.index("slicing".capitalize()):my_str.index("in".capitalize())])
print(my_str[my_str.index("in".capitalize()):my_str.index("python".capitalize())])
print(my_str[my_str.index("python".capitalize()):])