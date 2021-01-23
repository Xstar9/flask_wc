tuple1 = (1,2,3,4,5)
list1 = list(tuple1)
print(list1)

list2 =("one","two","three","four","five")

zipp = zip(list2,list1) # zip打包成对象
zip2dict = dict(zipp) # 将zip按字典的格式转换
print(zip2dict)

list4 = [[1,2,3,8],[4,5,6,7],[0,9,10]]
list3 = list(map(list,zip(*list4))) # map 将列表中的列表元素进行一一对应（映射）
print(list3)

area = 111.00054888
print("{:.3f}".format(area))  # 精确    "{格式符}"。format(变量)


# str to list
str5 ="[11,9,5]"
list5 = eval(str5)
print(list5)
print(type(list5))

