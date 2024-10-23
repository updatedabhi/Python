import matplotlib as mtp
import numpy as np

'''
#Scater:
x1=np.array([0,1,5,7,8,10,12])
y1=np.array([2,6,8,5,2,12,18])
mtp.scatter(x1,y1)

x2=np.array([1,4,6,8,10,12,15])
y2=np.array([0,5,10,4,8,6,12])
mtp.scatter(x2, y2, marker="*")




x1=np.array(['A','B','C','D'])
y1=np.array([20,30,50,10])

mtp.bar(x1,y1,color="Red")
#width=0.8default

#horizontal bar
mtp.barh(x1,y1)



x1=np.array(['Apple', 'Banana','Litchi','Cherry'])
y1=np.array([100,50,40,80])
ptr.bar(x1,y1,color='Green', width=0.5)

y2=np.array([80,60,20,100])

ptr.bar(x1,y2,color='Pink',width=0.3)

l = ['Fruits', 'Quantity']
mtp.legend(l)

addlabels(x1,y2)

mtp.show()

'''

x1=np.array([35,25,40,15])
mtp.pie(x)
mtp.show()
#color
clr=np.array(['pink','yellow','black','apple'])
mtp.pic(x,color=clr)
#startriangle
mtp.pie(x,startriangle=90)

#explode

exp=[0.2,0,0,0]
mtp.pie(x,expode=exp)

#Lable

lbl=['apple','mango','litchi','cherry']
plt.pie(x,labels=lbl)

#shadow

mtp.pie(x,shadow="Ture")
#legend

plt.legend(fitle = 'fruits')



#histogram

x=[1,2,3,7,8,10,11,13,14,15]

mtp.hist(x,bins=[1,5,10,15])(#bins decided classes)

mtpshow()














