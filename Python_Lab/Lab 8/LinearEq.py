import numpy as np 
stats=np.array([[44,38,21],[32,28,15],[24,20,10]])
print(stats)
total=np.array([1412,1024,728])
res=np.linalg.solve(stats,total)
print(f"NO. OF MALES : {np.round(res[0])}")
print(f"NO. OF FEMALES : {np.round(res[1])}")
print(f"NO. OF KIDS : {np.round(res[2])}")