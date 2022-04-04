# Question 2b from Laboratory Wk01
module = input("input the course code: ")
# dictionary to match module code with its respective course name
switcher = {
    'CSC1006': "Mathematics 2",
    'CSC1007': "Operating System",
    'CSC1008': "Data structures and algorithms",
    'CSC1009': "Object Oriented Programming",
    'CSC1010': "Computer networks",
}
# print module name
print(switcher[module])


