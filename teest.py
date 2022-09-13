
import numpy as np

"""
ตัวแรกเป็นหลัก 10 (ตัวหากต้องให้10ตัวต้องเป็น110) ตัวหลัง 10
10 = 110
(N = W*N+N)
"""

index = np.arange(10, 110, 10)
# print("original = ", index[:], "\n")
""" case 1 [10  0  0  0  0  0  0  0  0  0] """
# index[1:] = 0
"""case 2 [  0   0   0   0   0   0   0   0   0 100] """
index[:-1] =0
"""case 3 [ 0  0  0  0 50  0  0  0  0  0],"""
# index[:] =0
# index[4] =50
"""case 4 [ 10   0   0   0   50   0   0   0   0 100] """
# index[:]=0
# index[0]=10
# index[4]=50
# index[-1]=90
"""case 5  [  0  20   0  40   0  60   0  80   0 100] """
# index[0:10:2]=0
"""special case """
index= [7,0,0,10,0,15,0,0,30]
# index= [7,0,0,10,0,15,0,0,30,300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# index= [7,0,0,10,0,15,0,0,30,50,60,100,0,0,0,200,300,333,0,350,0]

print("before = ", index[:], "\n")
print("len = ", len(index), "\n")


count_sub = 1 # count index[i] each value is 0 and bring it plot index or divide
dis_sub = 0  # find distance of value for example 10 _ _ _ 40 --> 40 - 10 = 30 = dis_sub
dist = 0  # dist = dis_sub/count_sub

for i in range(len(index)):
    # print(i)
    # print("comeeee index =",index[i])
    if index[i] == 0:
        count_sub += 1
        # print(i,"if 1 countsub",count_sub,"index =",index[i],"index = 13",index[13])
        # if it have a value in start day [10 0 0 0 0 0 0 0 0 0]
        if index[0] != 0 and count_sub == len(index):
            dist = index[0]
            for j in range(count_sub-1):
                if index[j+1] ==0:
                    index[j+1] = index[j]+dist
            count_sub = 1
            dist = 0
        elif i+1 == len(index): #  [0  0  0  0  50  0  0  0  0], [ 0  0  0  0 50  0  0  0  0  0] 
            #[7, 0, 0, 10, 0, 15, 0, 0, 30, 50, 60, 100, 0, 0, 0, 200, 300, 333, 0, 350, 0]
            if count_sub %2 !=0:
                dist = int(index[i-count_sub+1]/count_sub) 
            else:
                dist = int(index[i-count_sub+1]/(count_sub-1))
                if index[i-1] !=0:
                    index[i] = int((index[i-1]*2)-((index[i-1]*2)*40)/100) ;"""decrease when value in last day over """
                    break
            for j in reversed(range(count_sub)):
                # pass
                if index[i-j] ==0:
                    index[i-j] = index[i-j-1]+dist
            
            count_sub = 1
            dis_sub =0
            dist = 0
    elif index[i] != 0 :
        # if it have a value in final day [0 0 0 0 0 0 0 0 0 100]
        if count_sub == len(index):
            # print("comeeee index =",index[i])
            dist = int(index[i]/(count_sub))
            for j in reversed(range(count_sub)):
                if index[j-1] ==0:
                    index[j-1] = index[j]-dist
            count_sub = 1
            dist = 0
        # if it have a value in start and final day [ 10   0   0   0   0   0   0   0   0 100]
        # OR [7,0,0,10,0,15,0,0,30] OR [  0  20   0  40   0  60   0  80   0 100]
        elif count_sub != 1:
            # print(i,"if 2 countsub",count_sub,"index =",index[i],"index = 15",index[15])
            dis_sub = index[i] if count_sub>i else index[i]-index[i-count_sub]
            dist = int(dis_sub/count_sub)
            for j in range(count_sub):
                if index[i-j-1] ==0:
                    index[i-j-1] = index[i-j]-dist
            count_sub = 1
            dis_sub =0
            dist = 0

print("after = ", index[:], "\n")


def find_time(str,str2,str3):
    
    return
    pass

