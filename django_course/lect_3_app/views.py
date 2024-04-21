from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View


# Create your views here.
class IndexView(View):
    def get(self, request):
        return HttpResponse('Test view.')


class YearView(View):
    def get(self, request, year):
        return HttpResponse(year)


def post_detail(request, year, month, slug):
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем,"
                   " какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})
