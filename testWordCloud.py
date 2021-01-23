import jieba
from matplotlib import pyplot as plt # 绘图，可视化
from wordcloud import WordCloud  # 词云
from PIL import Image # 图像处理库
import numpy as np      #矩阵运算
import sqlite3



# 词云所需的文本
con = sqlite3.connect('Doubanmovies.db')
cur = con.cursor() # 添加光标
sql = 'select inq from DouBanMovie'
data = cur.execute(sql) # 执行sql语句main.DouBanMovie
text = "" # 连接文本的字符串
for item in data:
    text = text + item[0]


cur.close()
con.close()

cut = jieba.cut(text) # jieba库分词工具
string =' '.join(cut)
print(len(string))
print(string)

img = Image.open(r'.\static\assets\img\loveheart.jpg')
img_array = np.array(img)  # 将图片转化为矩阵数组

wc = WordCloud(
    background_color="white",
    mask=img_array,
    font_path="AdobeKaitiStd-Regular.otf" # C:\Windows\Fonts
)
wc.generate_from_text(string)


# 绘制图片
fig = plt.figure(1)
plt.imshow(wc) # 绘制规则 按词云的规则绘制、
plt.axis("off")   # 不显示坐标轴

# plt.show() #显示生成的词云图片
plt.savefig(r'.\static\assets\img\wordtest.jpg',dpi=500) # dpi 设置分辨率清晰度