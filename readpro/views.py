from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import JsonResponse
from django.views.generic import FormView
from .forms import *

import pytesseract    # ======= > Add
try:
    from PIL import Image
except:
    import Image

# Create your views here.

class HomeView(FormView):
    form_class = UploadForm
    template_name = 'readpro/read_image.html'
    success_url = '/'

    def form_valid(self, form):
        upload = self.request.FILES['file']
        print(type(pytesseract.image_to_string(Image.open(upload)))) # =====> add line
        return super().form_valid(form)

@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        response_data = {}
        upload = request.FILES['file']
        content = pytesseract.image_to_string(Image.open(upload))
        response_data['content'] = content

        return JsonResponse(response_data)