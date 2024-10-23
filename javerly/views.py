from django.shortcuts import render

from django.views import View

# Create your views here.

class JaverlyView(View):
    @staticmethod
    def get(request):
        context = {
            'title_name': 'javerly',
        }

        return render(request, 'javerly/base.html', context)
