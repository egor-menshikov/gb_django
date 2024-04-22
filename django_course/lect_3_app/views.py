
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView


# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'lect_3_app/index.html')


class TemplFor(TemplateView):
    template_name = 'lect_3_app/templ_for.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_list'] = ['one', 'two', 'three']
        context['my_dict'] = {
            'one': 1,
            'two': 2,
            'three': 3,
        }
        return context


class TemplIf(TemplateView):
    template_name = "lect_3_app/if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context


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
        " какой способ создания списков в Python работает быстрее...",
    }
    return JsonResponse(post, json_dumps_params={"ensure_ascii": False})
