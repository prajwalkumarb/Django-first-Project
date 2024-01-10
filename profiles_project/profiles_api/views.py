from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,filters
from rest_framework.authentication import TokenAuthentication


from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    
    def get (self , request ,format =None):
        """Return a list of APIView features"""
        an_apiviews  = [
            'uses HTTP method as function (get,post,patch,put,delete)',
            'is similar to a trasitional Django view',
            'Gives you the most control over you application logic',
            'Is mapped Manully to URLs'
        ]
        
        return Response({'message': 'Hello!','an_apiview':an_apiviews})
    
    def post(self,request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('enter_name')
            message = f'Hello { name }'
            return Response ({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self ,request, pk = None):
        """Handle updaating an object"""
        return Response({'method':'put'})
    
    def patch(self ,request , pk = None):
        """Handle a particl update of an object"""
        return Response ({'method': 'PATCH'})
    
    def delete(self , request ,pk= None):
        """Delete an object"""
        return Response({'method':'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    
    
    def list(self,request):
        """Return a hello Message"""
        
        a_viewset = [
            'User actions (list,create,retrieve,update,partual_update)',
            'Authontically maps to URLs using Routers',
            'Provides more funcationality with code',
        ]
        return Response ({'message':'Hello!!','a_viewset':a_viewset})
    
    def create(self ,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('enter_name')
            message = f'Heloooo!! {name}'
            return Response ({'message':message})
        else:
            return Response (
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self ,request,pk=None):
        """Handle Hetting am object by its ID"""
        return Response ({'http_method':'GET'})
    
    def update(self ,requestr , pk= None):
        """ Handle updating an object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self ,requestr , pk= None):
        """ Handle updating part of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self ,requestr , pk= None):
        """ Handle removeing an object"""
        return Response({'http_method':'DELETE'})
    
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and Updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)