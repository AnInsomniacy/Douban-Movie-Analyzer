import pymysql


def show_movie_list_fun():
    datalist  = []
    # 连接数据库 和 读取数据
    con = pymysql.connect(host='127.0.0.1', port=3306, user='1326555262', passwd='qq1968904856', db='doubanmovie',
                           charset='utf8')
    cur = con.cursor()
    sql = "select * from movie_info order by score desc "
    data = cur.execute(sql)
    results = cur.fetchall()
    for result in results:
        datalist.append(result)

    #按照顺序重新标号
    for i in range(len(datalist)):
        datalist[i] = list(datalist[i])
        datalist[i][0] = i+1
        datalist[i] = tuple(datalist[i])

    cur.close()
    con.close()
    return datalist
