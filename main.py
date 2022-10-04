
# ******************************
# Make your Code
# ******************************
import random
list=[]
nums=0
while nums<10:
    list.append(random.randint(0,100))
    nums=nums+1
smallestNum=min(list)
smallestIn=list.index(smallestNum)
print("Min Val:"+str(smallestNum)+" Index:"+str(smallestIn))