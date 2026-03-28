import numpy as np
print(np.__version__)

## first example##
a=np.array([1,2,3])
print(a*2)
print(a.ndim)
print(a.shape)

# 2-d array has no depth
a2=np.array(
    [[1,2,3]
     ,[4,5,6],
     [7,8,9]]
)

print(a2.ndim)
print(a2.shape)

a3=np.array(
    [[['A','B','C','D'],['E','F','G','H']]]
)
print(a3.ndim)
print(a3.shape)
print(a3)

## follow your outer braces to find depth, and inner checkfor where braces are equally closing and opening to see for num of rows and cols

#INDEXING#
a_to_z = np.array([
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], # Layer 0
    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']], # Layer 1
    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]  # Layer 2 
])

print(a_to_z[1,1,1])

#SLICING#
#   array[start:end:step]
n= np.array(
   [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
)

print(n[0:3])
print(n[:,0:3])
print(n[::-1])

#Arithmetic,vectorized#
print(a+1)
print(np.sum(a))
print(np.min(a))
print(np.argmin(a)) #************#return position
print(np.sqrt(a))
print(np.round(a)) #also floor and ceil

array1=np.array([1,2,3])
array2=np.array([4,5,6])
print(array1+array2)

#### COMPARISION operators ####
scores=np.array([91,55,100,73,82,64])
print(scores==100)

#### BROADCASTING #####
# The dimensions have same size or one of the dimensions has size 1


print(np.sum(n,axis=0)) ###axis=0 mean col vise

s=scores[scores>80]  ###filter and to preserve original shape we use 'where' function
s= np.where(scores>60,scores,0)

##### RANDOM ####
r= np.random.default_rng()
r= np.random.default_rng(seed=1) #we can set seed
print(r.integers(low=1,high=7,size=3))
print(r.integers(low=1,high=7,size=(3,2)))

#to array:
r.shuffle(scores)
r.choice(scores)  ## to choose one
r.choice(scores,size=2)  ## to choose one




