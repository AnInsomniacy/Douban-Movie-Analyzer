import binascii
from io import BytesIO

import matplotlib.pyplot as plt
import pymysql


def duration_generator():
    # 连接数据库 和 读取数据
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='1326555262', passwd='qq1968904856', db='doubanmovie',
                           charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT mins, count(*) as count FROM movie_info GROUP BY mins"
    cursor.execute(sql)
    results = cursor.fetchall()

    # 手动设置字体文件路径,解决警告
    font = {'family': 'SimHei',
            'weight': 'normal',
            'size': 14,
            }
    plt.rc('font', **font)
    plt.rcParams['axes.unicode_minus'] = False

    # 生成条形图
    time_range = [r[0] for r in results]
    counts = [r[1] for r in results]
    plt.figure(figsize=(9, 6))
    plt.bar(time_range, counts)
    plt.title('电影时长分布')
    plt.xlabel('时长(分钟)')
    plt.ylabel('电影数量')

    # 添加x轴和y轴
    plt.xticks(rotation=90)

    # 添加网格线
    plt.grid(axis='y', alpha=0.75)

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
