from django.http import HttpResponse
from django.template import loader

# Create your views here.
def items(request):
    template = loader.get_template('items.html')
    return HttpResponse(template.render())