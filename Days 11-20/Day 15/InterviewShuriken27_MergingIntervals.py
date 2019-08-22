#-------------------------------------------------------#
#            Time Complexity is O(n²)                   #
#-------------------------------------------------------#

# no_of_time_intervals = int(input())

# listz = []

# for i in range(no_of_time_intervals):
#     if no_of_time_intervals in range(1,100000):
#         a, b = [int(x) for x in input().split()]
#         if a in range(1,1000) and b in range(1,1000) and a < b:
#             listz.append([int(a),int(b)])

# print()
# t = ()
# set1 = {}
# set1 = set() # Empty set creation
# for i in range(len(listz)):
#     for j in range(len(listz)):
#         temp1 = listz[i][0]
#         temp2 = listz[i][1]
#         temp3 = listz[j][0]
#         temp4 = listz[j][1]
#         if temp2 >= temp3 and temp2 <= temp4 and temp1 < temp3: #[[1,3],[2,4]]
#             print(temp1,temp4)
#         if temp2 < temp3:
#             t = (temp3,temp4)
#             set1.add(t)

# main_list = list(set1)
# main_list.sort()
# for x in range(len(main_list)):
#     temp5 = main_list[x][0]
#     temp6 = main_list[x][1]
#     print(temp5,temp6) 

#---------------------------------------------------------------------------#

#-------------------------------------------------------#
#            Time Complexity is O(nlogn)                #
#-------------------------------------------------------#

no_of_time_intervals = int(input())

dictz = {}

for i in range(no_of_time_intervals):
    if no_of_time_intervals in range(1,100000):
        a, b = [int(x) for x in input().split()]
        if a in range(1,1000) and b in range(1,1000) and a < b:
            dictz.update({int(a):int(b)})

# print() # For new empty line
# print(dictz)
listz = [(k, v) for k, v in dictz.items()]
# print(listz)

def merge_intervals(intervals):
    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  # replace by merged interval
            else:
                merged.append(higher)
    for x in range(len(merged)):
        print(merged[x][0],merged[x][1])

merge_intervals(listz)
