import binascii
from io import BytesIO

import jieba
import matplotlib.pyplot as plt
import pymysql

from wordcloud import WordCloud


def worldcloud_generator_genres():
    # 连接数据库 和 读取数据
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='1326555262', passwd='qq1968904856', db='doubanmovie',
                           charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT genres FROM movie_info"
    cursor.execute(sql)
    results = cursor.fetchall()

    # 把result转换成字符串，注意判断空字符串
    genres = []
    for result in results:
        if result[0] != '' and result[0] is not None:
            genres.append(result[0])
    genres = ' '.join(genres)

    # 分词
    cut_text = " ".join(jieba.cut(genres))
    # 生成词云
    wordcloud = WordCloud(
        font_path="C:\Windows\Fonts\Microsoft YaHei UI\msyh.ttc",
        background_color="white",
        width=1000,
        height=880,
        margin=2,
    ).generate(cut_text)

    # 显示词云图片
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('电影类型分布')
    plt.imshow(wordcloud)
    plt.axis("off")
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    imb = binascii.b2a_base64(plot_data)  # 对plot_data进行编码
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    context = {
        'img': imd,
    }
    return context


def worldcloud_generator_areas():
    # 连接数据库 和 读取数据
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='1326555262', passwd='qq1968904856', db='doubanmovie',
                           charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT areas FROM movie_info"
    cursor.execute(sql)
    results = cursor.fetchall()

    # 把result转换成字符串，注意判断空字符串
    genres = []
    for result in results:
        if result[0] != '' and result[0] is not None:
            genres.append(result[0])
    genres = ' '.join(genres)

    # 分词
    cut_text = " ".join(jieba.cut(genres))
    # 生成词云
    wordcloud = WordCloud(
        font_path="C:\Windows\Fonts\Microsoft YaHei UI\msyh.ttc",
        background_color="white",
        width=1000,
        height=880,
        margin=2,
    ).generate(cut_text)

    # 显示词云图片
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('电影地区分布')
    plt.imshow(wordcloud)
    plt.axis("off")
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    imb = binascii.b2a_base64(plot_data)  # 对plot_data进行编码
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    context = {
        'img': imd,
    }
    return context


def worldcloud_generator_actor():
    # 连接数据库 和 读取数据
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='1326555262', passwd='qq1968904856', db='doubanmovie',
                           charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT actors FROM movie_info"
    cursor.execute(sql)
    results = cursor.fetchall()

    # 把result转换成字符串，只添加有内容的字符串
    genres = []
    for result in results:
        if result[0] != '' and result[0] is not None:
            genres.append(result[0])
    genres = ' '.join(genres)

    # 分词
    cut_text = " ".join(jieba.cut(genres))
    # 生成词云
    wordcloud = WordCloud(
        font_path="C:\Windows\Fonts\Microsoft YaHei UI\msyh.ttc",
        background_color="white",
        width=1000,
        height=880,
        margin=2,
    ).generate(cut_text)

    # 显示词云图片
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('电影演员分布')
    plt.imshow(wordcloud)
    plt.axis("off")
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    imb = binascii.b2a_base64(plot_data)  # 对plot_data进行编码
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    context = {
        'img': imd,
    }
    return context
