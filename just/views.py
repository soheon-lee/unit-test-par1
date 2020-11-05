import json

from django.views  import View
from django.http   import HttpResponse, JsonResponse

class JustView(View):
    def get(self, request):
        return JsonResponse({'message':'Just Do Python with >Wecode'}, status = 200)
