from django.http import JsonResponse
from django.shortcuts import render

from iframes.FramesGenerator.duration import duration_generator
from iframes.FramesGenerator.genres import show_genres
from iframes.FramesGenerator.areas import show_areas
from iframes.FramesGenerator.score import show_score
from iframes.FramesGenerator.show_movie_list import show_movie_list_fun
from iframes.FramesGenerator.showtime import show_showtime
from iframes.FramesGenerator.worldcloud import worldcloud_generator_genres, worldcloud_generator_areas, \
    worldcloud_generator_actor


def genres(request):
    return render(request, show_genres())


def areas(request):
    return render(request, show_areas())


def showtime(request):
    return render(request, show_showtime())


def score(request):
    return render(request, show_score())


def top_scores(request):
    return render(request, 'iframes/score_top.html')


def top_comments(request):
    return render(request, 'iframes/comment_top.html')


def group_urls(request):
    return render(request, 'iframes/showtime_group.html')


def search_urls(request):
    return render(request, 'iframes/film_search.html')


def duration_analysis(request):
    context = duration_generator()
    return render(request, 'iframes/duration_analysis.html', context)


def worldcloud_genres(request):
    args = worldcloud_generator_genres()
    return render(request, 'iframes/worldcloud.html', args)


def worldcloud_areas(request):
    args = worldcloud_generator_areas()
    return render(request, 'iframes/worldcloud.html', args)


def worldcloud_actor(request):
    args = worldcloud_generator_actor()
    return render(request, 'iframes/worldcloud.html', args)


def redirect(request):
    # 重定向页面到/
    redirect('')


def page_index(request):
    args = show_movie_list_fun()
    lenth = len(args)
    return render(request, 'mainWeb/index.html', {'length': lenth})


def show_movie(request):
    args = show_movie_list_fun()
    return render(request, 'mainWeb/database.html', {'movies': args})


def dynamic_image(request):
    return render(request, 'mainWeb/dynamic_graph_web.html')


def welcome(request):
    return render(request, 'mainWeb/welcome.html')


def static_image(request):
    return render(request, 'mainWeb/static_graph_web.html')


def wordcloud_center(request):
    return render(request, 'mainWeb/wordcloud_center.html')


def about_me(request):
    return render(request, 'mainWeb/about_me.html')

def show_spider(request):
    return render(request, 'mainWeb/spider.html')

def loading_page(request):
    return render(request,'mainWeb/loading.html')


def run_spider(request):
    return JsonResponse({'status': 'success'})