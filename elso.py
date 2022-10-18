from hatodik2 import Option
#opt=Option("C",100,"20221215",1)
#print(opt.calcPayoff(139))
K=100
expiry="20221215"
C=Option("C",K,expiry,1)
P=Option("P",K,expiry,-1)
S=87
t=0.23
vola=0.45

print(C.calcPrice(S,t,vola)+P.calcPrice(S,t,vola)-S)