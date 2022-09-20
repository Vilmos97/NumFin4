import numpy as np
import sys
import matplotlib.pyplot as plt

x=2
y=3

def osszead(x,y=0):
    z=x+y
    return z

print(osszead(100))


np.random.seed(112)
a_rnd_uniform=np.random.random((3,2))
print(a_rnd_uniform)
a_rnd_normal=np.random.normal([1,8.2],[1,1],(10,2))
print(a_rnd_normal)


realizacio= np.random.normal([0.05,0.1],[0.1,0.2],(100,2))
print(realizacio)
a_initial_price=np.array([[50,100]])
print(a_initial_price.shape)
a_price=a_initial_price * np.exp(realizacio)
print(a_price)


plt.hist(a_price[:,0], bins=100)
plt.hist(a_price[:,1],bins=100)
plt.figure()
plt.scatter(a_price[:,0],a_price[:,1])
#plt.show()

#list comprehension
l_uj=[x*2 for x in range (5)]
print(l_uj)
sys.exit(0)





a=np.array([[1,2],[3,4]])
b=a-2
#print(type(a))
#print(a)
#print(b)


r_eff = np.array([[0.1,0.2],[0.3,0.4],[0.5,0.6]])
ic=np.exp(r_eff)
#print(ic)

ic_2y=ic**2
r_2y = np.log(ic_2y)
#print(r_2y)

#print(r_eff.shape)

a_elso=np.array([[10,2],[2,5],[2,8]])
print(a_elso)
#atlag,osszeg, kumullas, min, max
print(np.sum(a_elso))
print(np.sum((a_elso), axis=0))
print(np.sum((a_elso), axis=1))
print(np.mean((a_elso), axis=0))
print(np.std((a_elso), axis=0))
print(np.min((a_elso), axis=0))
print(np.max((a_elso), axis=0))
print(np.diff((a_elso), axis=0))
b_diff=np.diff(a_elso, axis=1)
print(b_diff.shape)
print(b_diff)

#centralizalt tomb
c=a_elso-np.mean(a_elso)
print(c)
print(np.mean(c))
print(c.mean)

is_pos=c>0
print(c)
print(is_pos)

d=c.copy()
d[~is_pos]=d[is_pos]+100
print(d)


a_new = np.array([[2,2],[2,4],[0,4]])
print(a_new.std(axis=1))
print(a_new.std(axis=1, ddof=0))
print(a_new.std(axis=1, ddof=1))

#random numbers

a_rnd=np.random.random((3,2))
print(a_rnd)


