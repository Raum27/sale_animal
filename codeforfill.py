import numpy as np 

# index =np.arange(10,310,10)
# index[0]=0
# index = np.arange(3570,357010,3570)
# index[2:5] =0
# index[55:57] =0
# index[45]=0
# index[87]=0
# index[89:98]=0
# index[0:-1]=0
# print(index[:],"\n")
# # index[50:60] = 0
# # index[0:40:2] =0
# # index[83:95] =0
# # print(index[:],"\n")
# index =[333084,591661,849890,1230473,0,1316967,1627708,1933652,2141126,2234480,2585038,2762350,2998650,3267625,3512830,3691101,3867687,4125700,4324132,4541777,4816071,5096523,5299872,5471397,5736852,5934216,6218015,6455952,6795267,7129754,0, 14389]
# print(index[:])
count_sub = 1 # count index[i] each value is 0 and bring it plot index or divide
dis_sub = 0  # find distance of value for example 10 _ _ _ 40 --> 40 - 10 = 30 = dis_sub
dist = 0  # dist = dis_sub/count_sub
index = np.arange(0,29)
index[:]=0
index[9]=1079
print(index[:])
for i in range(len(index)):
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
    elif index[i] != 0 :
        # if it have a value in final day [0 0 0 0 0 0 0 0 0 100]
        if count_sub == len(index):
            # print("comeeee index =",index[i])
            dist = int(index[i]/(count_sub))
            for j in reversed(range(count_sub)):
                if index[j-1] ==0:
                    index[j-1] = index[j]-dist
            count_sub = 1
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
print(index[:])
# print(index[:])
#      29 27 30 29 30
# sum = []
# arr = [31,28,31,30,31]
# index_start =0
# index_stop =0
# for i in range(len(arr)):
#     if i ==0:
#         for j in range(0,arr[i]):
#             sum.append(j)
#             pass
#         index_stop += arr[i]
#     else:
#         index_start +=arr[i-1]
#         index_stop +=arr[i] 
#         for j in range(index_start,index_stop):
#             sum.append(j)
#             pass
#         pass

# print(sum)
# print(len(sum))
# def FILL_CUMSALES(info):
#     print(type(info))
#     print(len(info))
#     print(info)
#     for i in range(len(info)):
#         info[i]=300

#     return info

# arr = [31,28,3,5,6,7,45,5134,1111,4222,14,122,2333,132,3551,2663,1772,3534,6]
# br = arr[3:9]

# arr[:5] = FILL_CUMSALES(br)
# print(arr)
     
# size_info = index_stop-index_start
#     print("index_start = ",index_start," index_stop= ",index_stop,"size_info = ",size_info)
#     print("start day :",info[index_start,0]," stop day:",info[index_stop,0])
#     for i in range(index_start,index_stop):
#         if info[i,1] == 0:
#             count_sub += 1
#             # if it have a value in start day [10 0 0 0 0 0 0 0 0 0]
#             if info[index_start,1] != 0 and count_sub == size_info:
#                 dist = info[i,1]
#                 for j in range(count_sub-1):
#                     if info[j+1,1]==0:
#                        info[j+1,1] = float(info[j,1]+dist)
#                 count_sub = 1
#             elif i+1 ==  index_stop: #  [0  0  0  0  50  0  0  0  0], [ 0  0  0  0 50  0  0  0  0  0] 
#                 if count_sub %2 !=0:
#                     dist = int(info[i-count_sub+1,1]/count_sub) 
#                 else:
#                     dist = int(info[i-count_sub+1,1]/(count_sub-1))
#                     if info[i-1,1] !=0:
#                         info[i,1] = float(int((info[i-1,1]*2)-((info[i-1,1]*2)*40)/100)) ;"""decrease when value in last day over """
#                         break
#                 for j in reversed(range(count_sub)):
#                     # pass
#                     if info[i-j,1] ==0:
#                         info[i-j,1] = float(info[i-j-1,1]+dist)
#                 count_sub = 1
#         elif info[i,1] != 0 :
#             # if it have a value in final day [0 0 0 0 0 0 0 0 0 100]
#             if count_sub == size_info:
#                 dist = int(info[i,1]/(count_sub))
#                 for j in reversed(range(count_sub)):
#                     if info[j-1,1] ==0:
#                         info[j-1,1] = float(info[j,1]-dist)
#                 count_sub = 1
#             # if it have a value in start and final day [10 0 0 0 0 0 0 0 0 100] OR [7,0,0,10,0,15,0,0,30] OR [0 20 0 40 0 60 0 80 0 100]
#             elif count_sub != 1:
#                 dis_sub = info[i,1] if count_sub>i else info[i,1]-info[i-count_sub,1]
#                 dist = int(dis_sub/count_sub)
#                 for j in range(count_sub):
#                     if info[i-j-1,1] ==0:
#                         info[i-j-1,1] = float(info[i-j,1]-dist)
#                 count_sub = 1