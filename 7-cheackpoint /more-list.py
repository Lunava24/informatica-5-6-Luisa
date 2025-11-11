# list with strings
# names = ["Bob", "Stuart", "Kevin"]
# names.append("Joseph")

# for name in sorted(names):
#     print(name)

# Lits with floats
# measurements = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]
# mean = sum(measurements) / len(measurements)
# print("The mean is: ", mean) 

# List within list
# super_list = [[5,2,3],[4,1],[2,2,5,1]]
# print(super_list[1][0])
#Example (List within list)
# grades = [["Shakira", 8, "D"], ["Melissa", 0, "C"], ["Shensi", 10, "A"]]
# for student in grades:
#     name = student[0]
#     grade = student[1]
#     group = student[2]
#     print(f"{name} got a {group} got a {grade}.")

# Matrices 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Print rows
for row in matrix:
    print(row)

print("\n")

i = 0
while i < 3:
    matrix_plus = []
    for row in matrix:
        matrix_plus.append(row[i])
    i += 1
    print(matrix_plus)    
