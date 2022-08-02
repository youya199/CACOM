import math
import numpy as np

# 1. 找到4,3,6三个点
# 按顺序存进point_sort列表
# def find_points(point_list):
#     point_sort = []

#     point_list = sorted(point_list)
#     p5 = point_list[4]
#     p6 = point_list[5]
#     point_sort.append(point_list[3])
#     point_sort.append(point_list[0])
#     if p6[1] > p5[1]:
#         point_sort.append(point_list[5])
#     else:
#         point_sort.append(point_list[4])
#     return point_sort

# def find_points(point_list):
#     point_sort = []

#     point_list = sorted(point_list)
#     # 4 5 6很容易通过y大小来确定
#     p5 = point_list[4]
#     p6 = point_list[5]
#     p4 = point_list[3]
#     point_sort.append(p4)
    
#     # p1, p2, p3很容易混淆
#     # 此时通过 x值判断
#     p3 = point_list[0]
#     p2 = point_list[1]
#     p1 = point_list[2]

#     # p3 = max(p1[1], p2[1], p3[1])
#     p3 = max([p1, p2, p3], key=lambda x: x[1])
    
#     point_sort.append(p3)
#     point_sort.append(p6)
#     return point_sort

def find_points(point_list):
    # for points in point_list

    point_sort = []

    point_list = sorted(point_list)

    p6 = min(point_list, key=lambda x: x[1])
    # p6 = max(point_list)
    # p6 = point_list[5]
    p1 = point_list[0]
    if p6 == p1:
        p6 = max(point_list)

    p3 = max(point_list, key=lambda x: x[1])

    point_list.remove(p6)
    point_list.remove(p3)
    point_list.remove(p1)

    point_list = sorted(point_list)

    p4 = point_list[1]
    point_sort.append(p4)
    point_sort.append(p3)
    point_sort.append(p6)

    return point_sort

# 2.  计算三边长
def euclidean_distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


# 3. 计算角436的值
def angle(a, b, c):
    """
    a, b: the length of two adjacent edges
    c: the length of opposite site
    """
    d = math.degrees(math.acos((a * a + b * b - c * c) / (2 * a * b)))
    return d


"""
     4
     *
    *  * 
   *    *  
  *      * 
 *        *
************ 
3           6
"""
# INPUT
def coor2angle(all_points):
    # all_points = [[(1315.011474609375, 406.929443359375),
    #             (1212.295654296875, 626.8081665039062),
    #             (1084.995361328125, 752.9243774414062),
    #             (988.5630493164062, 753.6880493164062),
    #             (1302.6756591796875, 828.309326171875),
    #             (738.0346069335938, 831.6212158203125)],

    #             [(1302.8018798828125, 401.1720275878906),
    #             (1207.6300048828125, 626.0771484375),
    #             (1083.2247314453125, 756.1541137695312),
    #             (986.1935424804688, 757.182861328125),
    #             (1302.7919921875, 827.3223876953125),
    #             (736.1265869140625, 837.8878784179688)]]

    # main
    angles_change = []  # output angle_list
    # 视频一共多少帧
    nums_frames = len(all_points)
    for k in range(nums_frames):
        # 初始化三边长为0，以及三个点为0
        edge_34, edge_36, edge_46 = 0, 0, 0
        point_3, point_4, point_6 = 0, 0, 0
        numbers_points = 0

        # 判断第k帧里面是否为6个点
        points_perFrames = len(all_points[k])
        # 只处理6个点都完整检测到的帧
        if points_perFrames == 6:  # 如果不是6个点，会影响到点的排序
            # 找到436， 三个点
            points_coordinate = find_points(all_points[k])

            point_4 = points_coordinate[0]
            point_3 = points_coordinate[1]
            point_6 = points_coordinate[2]

            # 计算对应边长
            edge_34 = euclidean_distance(point_3, point_4)
            edge_36 = euclidean_distance(point_3, point_6)
            edge_46 = euclidean_distance(point_4, point_6)
        else:
            continue

        # 添加第k帧的angle到list中
        # angles_change.append(angle(edge_34, edge_36, edge_46))
        ag=angle(edge_34, edge_36, edge_46)
        angles_change.append(ag)
    final_angles=[]
    angle_mean=np.mean(angles_change)
    for i in range(len(angles_change)):
        if (angles_change[i] > (angle_mean-5)) and (angles_change[i] < (angle_mean+5)):
            angles_change[i]=angles_change[i]-14.5
            final_angles.append(angles_change[i])
        else:
            continue
    return final_angles
