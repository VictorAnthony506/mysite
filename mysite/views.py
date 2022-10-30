from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def profile(request):
    return Response({"slackUsername": "anthonyvictor385",
                     "backend": True,
                     "age": 23,
                     "bio": "An AI enthusiast with interest in backend"})