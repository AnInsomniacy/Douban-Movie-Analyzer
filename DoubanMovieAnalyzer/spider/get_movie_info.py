import csv
import pymysql
import requests
import re
from lxml import html
import time

conn = pymysql.connect(host='127.0.0.1', port=3306, user='1326555262', passwd='qq1968904856', db='doubanmovie',
                       charset='utf8')
cursor = conn.cursor()

# 请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'll="118288"; bid=h4WM_cGaVNk; _vwo_uuid_v2=D11007C63904917875F42ACCB063CEDFB|6b42d8c972f0571dce094bc21789a459; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1675241372,1675429971; __utmz=30149280.1676706340.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1676706340.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1682131153%2C%22https%3A%2F%http://2Fwww.baidu.com&quot;https%3A%2F%http://2Fwww.baidu.com>%2Flink%3Furl%3DOANmaF7xF4-gaTECP3A7i3LLbat7VdaOPIQ9-2aTvFECAEZdy1GJwlYweYARJ8icIALuAzy3UcqtWl1ckeacX_%26wd%3D%26eqid%3D96cb9e780013826c0000000663f0821f%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.689787580.1675241372.1682041969.1682131153.11; __utmb=30149280.0.10.1682131153; __utmc=30149280; __utma=223695111.1269601210.1675241372.1682041969.1682131153.11; __utmb=223695111.0.10.1682131153; __utmc=223695111; dbcl2="182426180:x5gv0wXLvD0"; ck=_aWA; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=c5a0755f75869af2.1675241371.11.1682132897.1682041968.',
    'Host': 'movie.douban.com',
    'Referer': 'https://accounts.douban.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

# 读取电影url
with open('./movie_urls.csv', 'r') as f:
    reader = csv.reader(f)
    urls = [row[0] for row in reader]


def get_info_and_save():
    for i in range(0, len(urls)):
        print("正在爬取第{}部电影".format(i + 1))
        url = urls[i]
        # 请求页面
        r = requests.get(url=url, headers=headers, timeout=10)
        time.sleep(2)
        etree = html.etree
        selector = etree.HTML(r.text)

        # 获取电影名称
        filmname = []
        try:
            filmname = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]  # 电影名
            if filmname == "":
                filmname = None
        except Exception as e:
            filmname = None
        print("名称 :{}".format(filmname))

        # 获取电影评分
        score = []
        try:
            score_list = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
            score = score_list[0].replace("\t", "").replace("\n", "")
            if score == "":
                score = None
        except Exception as e:
            score = None
        print("评分 :{}/10".format(score))

        # 获取电影上映时间
        showtime = []
        try:
            st = selector.xpath('//*[@id="content"]/h1/span[2]/text()')[0]  # 上映日期
            showtime = st.replace("(", "").replace(")", "")
            if showtime == "":
                showtime = None
        except Exception as e:
            showtime = None
        print("年份 :{}年".format(showtime))

        # 获取电影片长
        mins = []
        try:
            mins_list = re.findall('片长:</span>.*?>(.*?)</span>', r.text, re.S)  # 片长
            mins = mins_list[0].replace(' ', '').replace('分钟', '')
            #只保留数字
            mins = re.findall(r"\d+\.?\d*", mins)[0]
            if mins == "":
                mins = None
        except Exception as e:
            mins = None
        print("时长 :{}分钟".format(mins))

        # 获取电影类型
        genres_list = []
        try:
            genres_list = re.findall('<span property="v:genre">(.*?)</span>', r.text, re.S)
            genres_list = '/'.join(genres_list)
            if genres_list == "":
                genres_list = None
        except Exception as e:
            genres_list = None
        print("类型 :{}".format(genres_list))

        # 获取电影制片地区
        area_list = []
        try:
            area_list = re.findall('<span class="pl">制片国家/地区:</span> (.*?)<br/>', r.text, re.S)
            area_list = '/'.join(area_list).replace(' ', '')
            if area_list == "":
                area_list = None
        except Exception as e:
            area_list = None
        print("地区 :{}".format(area_list))

        # 获取电影导演
        directors_list = []
        try:
            d_list = selector.xpath('//div[@id="info"]/span[1]/span[2]/a/text()')  # 导演
            if len(d_list) > 2:
                for i in range(0, 3):
                    directors_list.append(d_list[i])
            else:
                for j in range(0, len(d_list)):
                    directors_list.append(d_list[j])
            directors_list = '/'.join(directors_list)
            if directors_list == "":
                directors_list = None
        except Exception as e:
            directors_list = None
        print("导演 :{}".format(directors_list))

        # 获取电影编剧
        scriptwriters_list = []
        try:
            w_list = selector.xpath('//*[@id="info"]/span[2]/span[2]/a/text()')  # 编剧
            if len(w_list) > 2:
                for i in range(0, 3):
                    scriptwriters_list.append(w_list[i])
            else:
                for j in range(0, len(w_list)):
                    scriptwriters_list.append(w_list[j])
            scriptwriters_list = '/'.join(scriptwriters_list)
            if scriptwriters_list == "":
                scriptwriters_list = None
        except Exception as e:
            scriptwriters_list = None
        print('编剧 :{}'.format(scriptwriters_list))

        # 获取电影主演
        actors_list = []
        try:
            actors = selector.xpath('//*[@id="info"]/span[3]/span[2]')[0]  # 演员
            a_list = actors.xpath('string(.)').replace(' ', '').split('/')  # 标签套标签，用string(.)同时获取所有文本
            if len(a_list) > 2:
                for i in range(0, 3):
                    actors_list.append(a_list[i])
            else:
                for j in range(0, a_list):
                    actors_list.append(a_list[j])
            actors_list = '/'.join(actors_list)
            if actors_list == "":
                actors_list = None
        except Exception as e:
            actors_list = None
        print('主演 :{}'.format(actors_list))

        # 获取电影评价
        comment = []
        try:
            comment = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')[0]
            if comment == "":
                comment = None
        except Exception as e:
            comment = None
        print("评价 :{}条".format(comment))
        print("--------------------------------------------------")
        try:
            # # 执行sql语句
            query = 'insert into movie_info(url, filmname, score, showtime, genres, areas, mins, directors, scriptwriters, actors, comments) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            values = (
                url, filmname, score, showtime, genres_list, area_list, mins, directors_list, scriptwriters_list,
                actors_list,
                comment)
            cursor.execute(query, values)
            # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
            conn.commit()
        except Exception as e:
            print(e)
            # 回滚
            conn.rollback()


if __name__ == '__main__':
    get_info_and_save()
    # 关闭cursor对象
    cursor.close()
    # 关闭数据库连接
    conn.close()
