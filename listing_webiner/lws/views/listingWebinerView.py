from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lws.models.webinerListsModel import WebinerListsModel
from lws.models.categoryModel import CategoryModel


@login_required
def listingWebiner(request):
    """webiner一覧を取得し、lws/webiner_list.htmlを表示する。

    Args:
        request ([type]): request

    Returns:
        HttpResponse: lws/webiner_list.htmlを表示するためのhttpレスポンス
    """
    webiners = WebinerListsModel.objects.all().order_by('start_date')
    categories = CategoryModel.objects.all().order_by('name')
    return render(request, 'lws/webiner_list.html',
                  {'webiners': webiners, 'categories': categories})
