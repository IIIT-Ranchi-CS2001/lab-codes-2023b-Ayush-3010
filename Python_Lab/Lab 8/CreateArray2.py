import numpy as np
def CreateArray(*args):
    l=len(args)
    res=np.eye(l)
    for i in range(l):
        for j in range(l):
            if res[i][j] == 1:
                res[i][j] = args[i]
    return res
    

print(CreateArray(1,2,3,4))