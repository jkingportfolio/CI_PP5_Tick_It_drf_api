
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework.decorators import api_view
from rest_framework.response import Response
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@api_view()
def home(request):
    return Response({
        'status': 200,
        'message': "Hello, welcome to Tick It Django REST Framework API"
        })
