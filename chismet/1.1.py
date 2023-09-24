import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.sin(np.exp(x/2)/35)
def l(i, x, n, x_array):
    sum=1
    for j in range(0,n+1):
        if (x_array[i]!=x_array[j]):
            sum = sum * (x-x_array[j])/(x_array[i]-x_array[j])
            
    return sum
def L(x,n,x_array,y_array):
    sum=0
    for i in range(0,n+1):
        sum+=y_array[i]*l(i,x,n,x_array)
    return sum
        
    
n=int(input())
x_array=np.array([(0.5*(10)+0.5*(10)*np.cos((2*k-1)*np.pi/(2*(n-1)))) for k in range(1,n)])
x_array=np.append(x_array,10.0)
x_array=np.insert(x_array, 0, 0)

x_array=np.sort(x_array)
y_array=f(x_array)
x_star=np.array([x_array[k]+0.25*(x_array[k+1]-x_array[k]) for k in range(0,n)])

y_star = np.array([L(x,n,x_array,y_array) for x in x_star])
y_check = np.array([f(x) for x in x_star])
yerr=np.array(np.abs(y_check-y_star))

plt.plot(x_array,y_array,label='1',marker='o',linestyle='-')
plt.errorbar(x_star,y_star,yerr=yerr,label='2',marker='x')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
yerr=np.sort(yerr)
print(yerr[-1])
plt.show()