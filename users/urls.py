from django.urls import path, include
from .views import ExampleAuthentication, UserViewSet, GroupViewSet, SignUp
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)



urlpatterns = [
    path('alluser/', include(router.urls)),
    # path('', include('django.contrib.auth.urls')), # login
    #  path('signup/', SignUp.as_view(), name='signup'),  #signup
     path('rest-auth/', include('rest_auth.urls')),
     path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', ExampleAuthentication.as_view())

]
