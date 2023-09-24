
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.sin(np.exp(x/2)/35)
def l(i, x, n, x_array):
    sum=1
    for j in range(0,n+1):
        if (j!=i):
            sum = sum * (x-j*10/n)
            sum=sum/(i-j)
    sum = sum/((10/n)**n)
    
    return sum
def L(x,n,x_array,y_array):
    sum=0
    for i in range(0,n+1):
        
        sum+=y_array[i]*l(i,x,n,x_array)
        print(l(i,x,n,x_array),y_array[i],sum)

    return sum
        
    
n=int(input())
x_array=np.arange(0,n+1)*10/n

y_array=f(x_array)
x_star=x_array+0.25*10/n
x_star=x_star[:-1]

y_star = np.array([L(x,n,x_array,y_array) for x in x_star])
y_check = np.array([f(x) for x in x_star])
yerr=np.array(np.abs(y_check-y_star))

plt.plot(x_array,y_array,label='1',marker='o',linestyle='-')
plt.errorbar(x_star,y_star,yerr=yerr,label='2')
plt.xlabel('X')
plt.ylabel('Y')
yerr=np.sort(yerr)
print(yerr[-1])
plt.grid(True)
plt.show()