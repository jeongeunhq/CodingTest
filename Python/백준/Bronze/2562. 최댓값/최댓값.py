
num_list =[]
for i in range(9):
    num_list.append(int(input()))
max=max(num_list)
print(max)
print(num_list.index(max)+1)