from spider.get_movie_info import get_info_and_save

def run_spider(request):
    get_info_and_save()
    return render(request, 'mainWeb/spider.html')