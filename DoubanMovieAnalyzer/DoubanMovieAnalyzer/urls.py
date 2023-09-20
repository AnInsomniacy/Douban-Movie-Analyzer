"""
URL configuration for DoubanMovieAnalyzer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from iframes.views import genres, areas, showtime, score, top_scores, top_comments, search_urls, \
    duration_analysis, worldcloud_genres, worldcloud_areas, worldcloud_actor, page_index, redirect, show_movie, \
    dynamic_image, welcome, static_image, wordcloud_center, about_me, show_spider, loading_page, run_spider

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iframes/genres/', genres, name='genres'),  # 电影类型分布卡片图
    path('iframes/areas/', areas, name='areas'),  # 上映地区分布横向图
    path('iframes/showtime/', showtime, name='showtime'),  # 上映年份折线图
    path('iframes/score_img/', score, name='score_img'),  # 评分分布横线图
    path('iframes/top_scores/', top_scores, name='top_scores'),  # 评分前十动图
    path('iframes/top_comments/', top_comments, name='top_comments'),  # 评论前十动图
    path('iframes/search_urls/', search_urls, name='search_urls'),  # 频数前二主演动图
    path('iframes/duration_analysis/', duration_analysis, name='duration_analysis'),  # 时长分布直方图
    path('iframes/worldcloud_genres/', worldcloud_genres, name='worldcloud_genres'),  # 词云图
    path('iframes/worldcloud_areas/', worldcloud_areas, name='worldcloud_areas'),
    path('iframes/worldcloud_actor/', worldcloud_actor, name='worldcloud_actor'),
    path('', page_index, name='main'),  # 欢迎页面
    path('index/', redirect, name='index'),  # 欢迎页面
    path('database/', show_movie, name='database'),
    path('dynamic_graph/', dynamic_image, name='dynamic_graph'),
    path('welcome/', welcome, name='welcome'),
    path('static_graph/', static_image, name='static_graph'),
    path('wordcloud_center/', wordcloud_center, name='wordcloud_center'),
    path('aboutMe/', about_me, name='aboutMe'),
    path('spider/', show_spider, name='spider'),
    path('loading/', loading_page, name='loading'),
    path('run_spider/', run_spider, name='run_spider'),
]
