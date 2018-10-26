def findAll(s,t):
    """returns all indices where substring t occurs in string s"""
    indices = []
    i = s.find(t)
    while i > -1:
        indices.append(i)
        i = s.find(t,i+1)
    return indices

indices  = findAll("The cat in the hat","at")
print(indices)