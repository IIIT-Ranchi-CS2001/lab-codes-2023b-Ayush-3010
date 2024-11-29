import numpy as np

x1,y1,z1 = map(int,input("ENTER THE SHAPE OF ARRAY A1 : ").split())
x2,y2,z2 = map(int,input("ENTER THE SHAPE OF ARRAY A2 : ").split())
size1=x1*y1*z1
size2=x2*y2*z2
A1=np.random.randint(low=0,high=size1*100,size=(x1,y1,z1))
A2=np.random.randint(low=0,high=size2*100,size=(x2,y2,z2))

div5=np.array([ele for ele in np.nditer(A1) if ele%5 == 0])
div4=np.array([ele for ele in np.nditer(A2) if ele%4 == 0])

print(f'{div4}\n{div5}')
res=np.concatenate((div4,div5),axis=0)
root=int(((res.size)**(0.5))//1)
print(res)
print(root)
res=res[:root*root].reshape(root,root)
print(res)



