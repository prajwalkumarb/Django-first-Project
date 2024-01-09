from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    
    def get (self , request ,format =None):
        """Return a list of APIView features"""
        an_apiviews  = [
            'uses HTTP method as function (get,post,patch,put,delete)',
            'is similar to a trasitional Django view',
            'Gives you the most control over you application logic',
            'Is mapped Manully to URLs'
        ]
        
        return Response({'message': 'Hello!','an_apiview':an_apiviews})
