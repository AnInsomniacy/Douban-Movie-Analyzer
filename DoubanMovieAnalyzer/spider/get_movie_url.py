import requests
import csv
from lxml import html

etree = html.etree

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

hrefs = []


# 获取电影的url
def get_movie_url(url):
    try:
        r = requests.get(url, headers=headers)
        selector = etree.HTML(r.text)
        movie_hrefs = selector.xpath('//div[@class="hd"]/a/@href')  # 电影的详情地址
        for i in range(0, len(movie_hrefs)):
            hrefs.append(movie_hrefs[i])
    except Exception as e:
        print(e)


# 保存到movie_urls.csv
def save_url():
    try:
        # 获取链接
        for href in hrefs:
            # 存入csv
            file_path = "./movie_urls.csv"
            with open(file_path, "a+", newline='', encoding='gb18030') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([href])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 拼接url，获取电影url
    for i in range(0, 250, 25):
        url = "https://movie.douban.com/top250?start=" + str(i) + ""
        get_movie_url(url)
        print("第" + str(i) + "页爬取完成")
    # 将爬取的url保存到csv文件中
    save_url()
    print("保存完成")
