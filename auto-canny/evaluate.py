# -*- coding: UTF-8 -*-

# 这是文献中提到的“序贯算法”实现，用于求解连通成分数。
# matlab有封装好的函数可以替代，本文4连通的计算应该没错
# 8连通部分没有读懂文献思路，鉴于数模时间有限，便转战matlab

import numpy as np

# 把值填入等价表
def addToequaleTable(equaleTable, x, y):
    indexOfx = 0
    indexOfy = 0
    for i in range(len(equaleTable)):
        if x in equaleTable[i]:
            indexOfx = i
            break
    for j in range(len(equaleTable)):
        if y in equaleTable[j]:
            indexOfy = j
            break

    # 如果x和y都已存在于表中
    if indexOfy and indexOfx:
        # 如果他们存在表的不同行里
        if indexOfx != indexOfy:
            # 把y行的内容放进x行
            temp = equaleTable.pop(max(indexOfx, indexOfy))
            for k in temp:
                equaleTable[min(indexOfx, indexOfy)].append(k)
        # 如果在同一行了，就什么都不做
    # 如果x在表，y不在表
    elif indexOfx and not indexOfy:
        equaleTable[indexOfx].append(y)

    elif not indexOfx and indexOfy:
        equaleTable[indexOfy].append(x)

    elif not indexOfx and not indexOfy:
        equaleTable.append([x, y])


def evaluate4(image):
    # 设定标记数组
    flags = np.zeros([len(image), len(image[0])])
    equaleTable = [[]]
    tag = 1
    # 255是边的颜色，白边255
    if image[0][0] == 255:
        flags[0][0] = tag
        addToequaleTable(equaleTable, tag, tag)
        tag = tag + 1

    for j in range(1, len(image[0])):
        i = 0
        if image[i][j] == 255:
            # 获取左边点的标记
            leftFlag = flags[i][j - 1]
            # 如果这个点都有标记的话
            if leftFlag:
                flags[i][j] = leftFlag
            # 如果没有
            else:
                flags[i][j] = tag
                addToequaleTable(equaleTable, tag, tag)
                tag = tag + 1
    for i in range(1, len(image)):
        j = 0
        if image[i][j] == 255:
            # 获取左边点的标记
            upFlag = flags[i - 1][j]
            # 如果这个点都有标记的话
            if upFlag:
                flags[i][j] = upFlag
            # 如果没有
            else:
                flags[i][j] = tag
                addToequaleTable(equaleTable, tag, tag)
                tag = tag + 1

    for i in range(1, len(image)):
        for j in range(1, len(image[0])):
            # 如果像素点为1，也就是如果是边界点
            if image[i][j] == 255:
                # 获取上面和左边两个点的标记
                upFlag = flags[i - 1][j]
                leftFlag = flags[i][j - 1]

                # 如果两个点都有标记的话
                if upFlag and leftFlag:
                    # 如果两个点有不同的标记
                    if upFlag != leftFlag:
                        # 复制上面那个点的标记
                        flags[i][j] = flags[i - 1][j]
                        # 将上和左两个标记置入等价表
                        addToequaleTable(equaleTable, upFlag, leftFlag)
                    # 两个点的标记相同
                    else:
                        # 复制其中一个即可
                        flags[i][j] = upFlag
                # 如果上面有但左边没有
                elif upFlag and not leftFlag:
                    flags[i][j] = upFlag
                elif not upFlag and leftFlag:
                    flags[i][j] = leftFlag
                # 如果两个都没有
                else:
                    flags[i][j] = tag
                    addToequaleTable(equaleTable, tag, tag)
                    tag = tag + 1

    # 第三步，处理flags
    for i in range(len(flags)):
        for j in range(len(flags[0])):
            if flags[i][j] != 0:
                # 找出不等于0的flag
                temp = flags[i][j]
                # 去tables找等价的最小值并替换
                for k in range(len(equaleTable)):
                    if temp in equaleTable[k]:
                        break
                flags[i][j] = min(equaleTable[k])

    # 第四步 计算数量
    cnt = 0
    for i in range(1, len(flags) - 1):
        for j in range(1, len(flags[0]) - 1):
            temp = flags[i][j]
            if flags[i][j - 1] == temp and flags[i][j + 1] == temp and flags[i - 1][j] == temp and flags[i + 1][
                j] == temp:
                cnt = cnt + 1

    return cnt  # , flags, equaleTable

# def evaluate8(image):
#     # 设定标记数组
#     flags = np.zeros([len(image), len(image[0])])
#     equaleTable = [[]]
#     tag = 1
#
#     if image[0][0] == 255:
#         flags[0][0] = tag
#         addToequaleTable(equaleTable, tag, tag)
#         tag = tag + 1
#
#     for j in range(1, len(image[0])):
#         i = 0
#         if image[i][j] == 255:
#             # 获取左边点的标记
#             leftFlag = flags[i][j - 1]
#             # 如果这个点都有标记的话
#             if leftFlag:
#                 flags[i][j] = leftFlag
#             # 如果没有
#             else:
#                 flags[i][j] = tag
#                 addToequaleTable(equaleTable, tag, tag)
#                 tag = tag + 1
#     for i in range(1, len(image)):
#         j = 0
#         if image[i][j] == 255:
#             # 获取左边点的标记
#             upFlag = flags[i - 1][j]
#             # 如果这个点都有标记的话
#             if upFlag:
#                 flags[i][j] = upFlag
#             # 如果没有
#             else:
#                 flags[i][j] = tag
#                 addToequaleTable(equaleTable, tag, tag)
#                 tag = tag + 1
#
#     for i in range(1, len(image)):
#         for j in range(1, len(image[0])):
#             # 如果像素点为1，也就是如果是边界点
#             if image[i][j] == 255:
#                 # 获取上面，左边，斜方向3个点的标记
#                 upFlag = flags[i - 1][j]
#                 leftFlag = flags[i][j - 1]
#                 obliqueFlag = flags[i - 1][j - 1]
#
#                 # 如果3个点都有标记的话
#                 if upFlag and leftFlag and obliqueFlag:
#                     # 如果两个点有不同的标记
#                     if upFlag != leftFlag or upFlag != obliqueFlag:
#                         # 复制上面那个点的标记
#                         flags[i][j] = flags[i - 1][j]
#                         # 将3个标记置入等价表
#                         addToequaleTable(equaleTable, upFlag, leftFlag)
#                         addToequaleTable(equaleTable, upFlag, obliqueFlag)
#                     # 3个点的标记相同
#                     else:
#                         # 复制其中一个即可
#                         flags[i][j] = upFlag
#                 # 如果上面,斜边有但左边没有
#                 elif upFlag and obliqueFlag and not leftFlag:
#                     flags[i][j] = upFlag
#                     addToequaleTable(equaleTable, upFlag, obliqueFlag)
#                 elif upFlag and not obliqueFlag and not leftFlag:
#                     flags[i][j] = upFlag
#                 elif obliqueFlag and not upFlag and not leftFlag:
#                     flags[i][j] = obliqueFlag
#                 elif obliqueFlag and leftFlag and not upFlag:
#                     flags[i][j] = obliqueFlag
#                     addToequaleTable(equaleTable, leftFlag, obliqueFlag)
#                 elif leftFlag and not upFlag and not obliqueFlag:
#                     flags[i][j] = leftFlag
#                 elif leftFlag and upFlag and not obliqueFlag:
#                     flags[i][j] = leftFlag
#                     addToequaleTable(equaleTable, leftFlag, upFlag)
#
#                 # 如果3个都没有
#                 else:
#                     flags[i][j] = tag
#                     addToequaleTable(equaleTable, tag, tag)
#                     tag = tag + 1
#
#     # 第三步，处理flags
#     for i in range(len(flags)):
#         for j in range(len(flags[0])):
#             if flags[i][j] != 0:
#                 # 找出不等于0的flag
#                 temp = flags[i][j]
#                 # 去tables找等价的最小值并替换
#                 for k in range(len(equaleTable)):
#                     if temp in equaleTable[k]:
#                         break
#                 flags[i][j] = min(equaleTable[k])
#
#     # 第四步 计算数量
#     cnt = 0
#     for i in range(1, len(flags) - 1):
#         for j in range(1, len(flags[0]) - 1):
#             temp = flags[i][j]
#             if temp == flags[i][j - 1] == flags[i][j + 1] == flags[i - 1][j] == flags[i + 1][
#                 j] == flags[i-1][j-1] == flags[i+1][j+1] == flags[i-1][j+1] == flags[i+1][j-1]:
#                 cnt = cnt + 1
#
#     return cnt, flags, equaleTable
