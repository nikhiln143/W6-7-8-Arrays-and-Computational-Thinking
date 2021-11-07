## Week 6,7,8 Arrays and Computational Thinking 
import random 
import math

def randArray(n): 
  newArray = [] 
  for i in range(0,n): 
    newArray.append(random.randint(0,100)) 
  return newArray 

## TASK - write randArray for a 2D list 
def rand2DArray(m,n): 
  megaArray = [] 
  for i in range(0,m):
    miniArray = [] 
    for j in range(0,n): 
      miniArray.append(random.randint(0,10))
    megaArray.append(miniArray) 
  return megaArray  

#print(rand2DArray(10,10))
 



myArray = randArray(10)



my2DArray = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#print(my2DArray)
## operations on 2D arrays 
## def printmyArray(A): 

my1DArray = [1,2,3,55,100,22]

maxvalue = my1DArray[0] 
for i in range(0,len(my1DArray)): 
  if(my1DArray[i] > maxvalue): 
    maxPos = i-1 
#print(maxPos) 



#for i in my1DArray: 
  # print(str(i))

#for i in range(0,len(my1DArray)):
  # print(my1DArray[i])



## matrix multiplication 
def matrixMult(A,B): 
  ## check dimensions 
  product = [] 
  if(len(A[0]) != len(B)):
    return None 
  else: # dimensions match up 
    for k in range(0,len(A)):
      row = [] 
      for i in range(0,len(A[0])): 
        row.append(dotProd(A[i],getCol(B,k)))
        #print(row)
      product.append(row)
  return product


A = [[1,0,0],[0,1,0],[0,0,1]] ## identity matrix 
B= [[1,2,3],[4,5,6],[7,8,9]]



## dot product 
def dotProd(a,b): 
  if (len(a) != len(b)):
    return None 
  else: 
    tot = 0
    for i in range(0,len(a)): 
      tot = tot +  a[i]*b[i]
  return tot 

def getCol(A,i): 
  ## A is a matrix, i is the column 
  col = [] 
  for j in range(len(A)): 
    col.append(A[i][j])
  return col

a = [1,2,3]
b = [4,5,6] 

#print(dotProd(a,b))

x = matrixMult(A,B)





## task 8 - separate odd and even numbers 

#print(testArray)




myList = randArray(10)

#print(myList)
for j in range(0,len(myList)):
  for i in range(0,len(myList)-(j+1)):
    if(myList[i] > myList [i+1]):
      temp = myList[i]
      myList[i] = myList[i+1]
      myList[i+1] = temp

#print(myList)

## linear search 

def linearSearch(array, num): 
  for i in range(0,len(array)):
    if(array[i] == num):
      return True 
  return False 


def findLargest(array,num):
  ## find the largest value in the array 
  largest = array[0]
  for i in range(1,len(array)):
    if(array[i] > largest):
      largest = array[i]
  return largest 

def fact(n):
  if(n==1):
    return 1
  else:
    return n * fact(n-1)

#print(fact(5))

## bubble sort 

def findSmallest(array):
  smallest = array[0]
  pos = 0
  for i in range(0,len(array)): 
    if(array[i] < smallest): 
      smallest = array[i]
      pos = i
  return [smallest,pos]


## selection sort 

## keep track of lowest postion 
def selSort(array):
  for j in range(0,len(array)): 
    lowest = array[j]
    pos = j
    for i in range(j,len(array)):
      if(array[i] < lowest):
        lowest = array[i]
        pos = i
    temp = array[j] 
    array[j] = array[pos]
    array[pos] = temp
  return array
     
myArray2 = randArray(10)
#print(myArray2)
#print(selSort(myArray2))


## find next smallesrt number 



## place it lowest position (swap)


## increment position 
  

def binarySearch(value,array):
  mx = len(array)-1
  mn = 0
  parts = 0
  while (mx >= mn): 
    mid = math.floor((mx + mn)/2)
    if(value == array[mid]):
      return True
      print(parts)
    if (value > array[mid]):
      mn = mid + 1
      parts +=1
    if (value < array[mid]):
      mx = mid -1
      parts += 1
  print(parts)
  return False


testArray = randArray(1000)
#print(testArray)
testArray = selSort(testArray)
#print(testArray)
print(binarySearch(91,testArray))






