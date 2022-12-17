Input = [(20, 'p1'), (31, 'p1'), (1, 'p2'), (88, 'p2'), (27, 'p2')]
  
Output = {}
for x, y in Input:
    if y in Output:
        Output[y].append((x, y))
    else:
        Output[y] = [(x, y)]
  
# Printing Output
print(Output)