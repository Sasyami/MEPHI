import numpy as np
import matplotlib.pyplot as plt
import math
def f (x):
    return np.cos(x)*np.exp(-2*x)
def f_der(x):
    return np.exp(-2*x)*(-np.sin(x)-2*np.cos(x))
def f_der2(x):
    return np.exp(-2*x)*(4*np.sin(x)+3*np.cos(x))
#def f_central(x,i,x_array,y_array):
#    return (2*x-(x_array[i]+x_array[i+1]))*y_array[i-1]/((x_array[i-1]-x_array[i])*(x_array[i-1]-x_array[i+1])) +\
#    (2*x - (x_array[i-1]+x_array[i+1]))*y_array[i]/((x_array[i]-x_array[i-1])*(x_array[i]-x_array[i+1])) +\
#    (2*x - ( x_array[i-1] + x_array[i]))*y_array[i+1]/((x_array[i+1]-x_array[i-1]) * (x_array[i+1]-x_array[i]))
def f_right(i,h,y_array):
    return (-3*y_array[i]+4*y_array[i+1]-y_array[i+2])/(2*h)
def f_central_x2(i,h,y_array):
    return  (y_array[i+1]-y_array[i-1])/(2*h)
def f_central_x4(i,h,y_array):
    return (y_array[i-2]-8*y_array[i-1]+8*y_array[i+1]-y_array[i+2])/(12*h)
def f_central2_x4(i,h,y_array):
    return (-y_array[i+2]+16*y_array[i+1]-30*y_array[i]+16*y_array[i-1]-y_array[i-2])/(12*h*h)
def f_central2_x2(i,h,y_array):
    return (2*y_array[i+1]+2*y_array[i-1]-4*y_array[i])/(2*h*h)
n = int((input()))
left = -0.8
right = 0.8
x_array = np.array([left + (right-left)*k/n for k in range (0,n+1)])
y_array = f(x_array)
y_der_central_array=np.array([f_central_x2(i,(right-left)/n,y_array) for i in range(1,n)])
y_der_central_x4_array=np.array([f_central_x4(i,(right-left)/n,y_array) for i in range(2,n-1)])
y_der_right_array=np.array([f_right(i,(right-left)/n,y_array) for i in range(0,n-1)])
y_der_check = f_der(x_array)
y_der2_central_x4_array = np.array([f_central2_x4(i,(right-left)/n,y_array) for i in range(2,n-1)])
y_der2_central_x2_array = np.array([f_central2_x2(i,(right-left)/n,y_array) for i in range(2,n-1)])
#y_der2_central_x4_array = np.array([f_central_x4(i,(right-left)/n,y_der_central_x4_array) for i in range(2,n-6)])
y_der2_check = f_der2(x_array)
yerr_der=np.sort(np.abs(y_der_right_array-y_der_check[:-2]))
yerr_der2=np.sort(np.abs(y_der2_central_x2_array-y_der2_check[2:-2]))
print(yerr_der[-1],"2 por 1 der")
print(yerr_der2[-1],"2 por 2 der")
yerr_der2=np.sort(np.abs(y_der2_central_x4_array-y_der2_check[2:-2]))
yerr_der=np.sort(np.abs(y_der_central_x4_array-y_der_check[:-4]))
print(yerr_der[-1],"4 por 1 der")

print(yerr_der2[-1],"4 por 2 der")
plt.figure(1)
plt.plot(x_array[2:-2],y_der_check[2:-2],label='5',marker='.',linestyle='-')
plt.plot(x_array[2:-2],y_der_right_array[2:],label='1',marker='x',linestyle='-')
plt.plot(x_array[2:-2],y_der_central_array[1:-1],label='2',marker='.',linestyle='-')
plt.plot(x_array[2:-2],y_der_central_x4_array,label='3',marker='.',linestyle='-')
plt.figure(2)
plt.plot(x_array[2:-2],y_der2_central_x4_array,label='3',marker='o',linestyle='-')
plt.plot(x_array[2:-2],y_der2_central_x2_array,label='9',marker='o',linestyle='-')

#plt.plot(x_array[2:-7],y_der2_central_x4_array,label='6', marker='o',linestyle='--')
plt.plot(x_array[2:-2],y_der2_check[2:-2],label='8',marker='v',linestyle='--')

#plt.plot(x_array[2:-7],y_der2_check[2:-7],label='7', marker='v',linestyle='--')

plt.show()
