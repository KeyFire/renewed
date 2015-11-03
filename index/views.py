from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse

def index(request):
    view = 'index'
    t = get_template('index.html')
    html = t.render(Context({'name':view}))
    return HttpResponse(html)

