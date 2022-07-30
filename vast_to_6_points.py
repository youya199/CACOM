import math

# Calculate the Eucli distance of two points
def eucliDist(A,B):
    return math.sqrt(sum([(a - b)**2 for (a,b) in zip(A,B)]))

# delete useless ponits
##input list
## output list and number of points

def delect_to_6(data):

    for i in data:
        for j in data: 
            dist = eucliDist(i,j)
            if dist < 15 and dist != 0:
                data.remove(j)
                
    for i in data:
        for j in data: 
            dist = eucliDist(i,j)
            if dist < 15 and dist != 0:
                data.remove(j)
                
    data_6 = data            
    num = len(data_6)
                 
    return data_6, num

# test 

# # data = np.array([[154, 824],[226, 826],[234, 797],[235, 797],[235, 798],[235, 799],[234, 799],[234, 800],[233, 800],[226, 825],[233, 802],[236, 797],[236, 798],[236, 799],[237, 797],[237, 796],[237, 800],[266, 785],[270, 755],[286, 674]])
# data = [[171, 628],[242, 608],[281, 563],[285, 534],[305, 458],[311, 634],[312, 634],[313, 634],[314, 634],[316, 635],[316, 636],[317, 636],[318, 636],[318, 635],[158, 675],[172, 624],[242, 604],[281, 559],[286, 530],[305, 453],[312, 630]]
# data_new, num_new = delect_to_6(data)
# data_new=np.array(data_new)
# x = data_new[:,0]
# y = data_new[:,1]
# plt.scatter(x,y)
# plt.show()
# print(num_new)