size = int(input())
elements = []

max_matrix = [[] for _ in range(size)]


for _ in range(size):
    elements.append(list(map(int, input().split())))
    
for i in range(size-1, -1, -1):
    for j in range(len(elements[i])):
        if i == size-1:
            max_matrix[i].append(elements[i][j])
        else:
            max_matrix[i].append(elements[i][j] + 
                              max(max_matrix[i+1][j], max_matrix[i+1][j+1]))
            
print(max_matrix[0][0])
            
            