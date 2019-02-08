import math
from random import randint
import random

import numpy as np
from numpy import *





#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code
def hammingGeneratorMatrix(r):
    n = 2**r-1
    
    #construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)

    #construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))

    #construct H'
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))

    #construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))

    #apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    #transpose    
    G = [list(i) for i in zip(*G)]

    return G
#print(hammingGeneratorMatrix(3))


#function decimalToVector
#input: numbers n and r (0 <= n<2**r)
#output: a string v of r bits representing n
def decimalToVector(n,r): 
    v = []
    for s in range(r):
        v.insert(0,n%2)
        n //= 2
    return v



'''inputa = [1,1,1,1,0,1]
def zero():
    c=[]
    num=len(decimalToVector(len(inputa),4)+inputa)
    num1=11-num
    for i in range(num1):
        c.insert(0,0)
    return c
    

print(decimalToVector(len(inputa),4)+inputa+zero())
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print('10!=',factorial(10))

a=[0,1,1,0]
r=2
k=2**r-r-1
l=len(a)



while l>k-r:
    r=r+1
    k=2**r-r-1
print(r)'''

def message(a):
    r=2
    k=2**r-r-1
    l=len(a)
    while l>k-r:
        r=r+1
        k=2**r-r-1
    r=r
    def zero():
        c=[]
        num=len(decimalToVector(len(a),r)+a)
        num1=11-num
        for i in range(num1):
            #c.insert(0,0)
            c.append(0)
        return c
    return(decimalToVector(len(a),r)+a+zero())

'''a=[0,1,1,0,1]
m=message(a)
print(m)'''

def hammingEncoder(m):
    r=2
    k=2**r-r-1
    l=len(m)
    c=[]
    while l!=k:
        if l<k:
            return c
        else:
            r+=1
            k=2**r-r-1
    #processing to next process ,when in case of vaild length of input
    #from numpy import *
    Gmatrix = hammingGeneratorMatrix(r)
    Gmatrix = np.array(Gmatrix) 
    m=np.array(m)
    #mm=m.T
    d=m.dot(Gmatrix)
    for i in d:
        if d[i]%2==0:
            d[i]=0
        else:
            d[i]=1
 
            
    return d

l=[1,1,0,0]
#print(hammingEncoder(l))

def hammingDecoder(v):
    #when r=2, is repetition code, so we begin from 
    #r=3
    r=3
    k=2**r-1
    l=len(v)
    c=[]
    while l!=k:
        if l<k:
            return c
        else:
            r+=1
            k=2**r-1

            
            
    #processing to next process, when in case of vaild 
    #length of given vector
    #create Hmatrix
    def D(r,l):

        h=[]
        for i in range(1,2**r):
            h.append(decimalToVector(i,r))
        h=np.matrix(h)
        h=np.transpose(h)

        #print(h)

    #l=[0,1,1,0,0,0,0]
        l=np.matrix(l)
        l=np.transpose(l)
        #print(l)

        d=h*l%2
        #print(d)
        return d
    d=D(r,v)
    d=d.tolist()
    #print(d)
    #transfer the listinlist to list
    e = []
    for i in d:
        e.append(i[0])
    #print(e)
    
    
    number=0
    
    for bit in e:
        if bit==0:
            number+=1
    if number==len(e):
        return v
    else:
        power=len(e)-1
        summ=0
        for bit in e:
            if bit==1:
                summ+=pow(2,power)
            else:
                summ=summ
            power-=1
        position=summ
        #print(position)
        positioninlist=position-1
        #print(v[positioninlist])
        if v[positioninlist]==1:
            v[positioninlist]=0
        else:
            v[positioninlist]=1
        return v
        
        
    

                    
    
    



    #vector to mum
    

   
#u=[1,1,0,0,0,1,1]
u=[0,0,0,0,0,0,0]
#u=[1,1,0,1,0,1,0]
#u=[0,1,1,1,0,1,0]
#print(hammingDecoder(u))
#0101011 0101010 d 111
#0101010 0101010 d 000
#1101010 0101010 d 001

def messageFromCodeword(c):
    #when r=2, is repetition code, so we begin from 
    #r=3
    r=3
    k=2**r-1
    l=len(c)
    f=[]
    while l!=k:
        if l<k:
            return f
        else:
            r+=1
            k=2**r-1
            
    #print(r)
    highest_power=r-1
    new=[]
    for u in range(r):
        new.append(2**u)
    new.reverse()
    #print(new)
    for i in new:
        del c[i-1]
    
    return c

i=[1,1,1,0,0,0,0]
#print(messageFromCodeword(i))


def dataFromMessage(m):
    r=2
    k=2**r-r-1
    l=len(m)
    c=[]
    while l!=k:
        if l<k:
            return c
        else:
            r+=1
            k=2**r-r-1
    
    find_l = c[0:r+1:1]
    print(find_l)
    return m
p=[0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]
print(dataFromMessage(p))



def repetitionEncoder(m,n):
    o=[]
    for i in range(n):
        o.append(m[0])
        
    return o
m=[0]
n=4
c=repetitionEncoder(m,n)
#print(c)


def repetitionDecoder(v):
    k=[]
    j=[0]
    m=[1]
    counter=0
    for i in v:
        if v[i]==1:
            counter+=1
        else:
            counter-=1
    counter = counter
    if counter==0:
        return k
    elif counter<0:
        return j
    else:
        return m

        
        
    
    

    
    
    
    
    
 
  







    
            
        
        
    

    
           
    
    
    
        
            
    





    
    
    
    


        
    