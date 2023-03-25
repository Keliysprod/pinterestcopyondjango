from django.urls import path, include
from .views import MainPage,Category, PinsView, PinsDetail
from .views import Success, Register
from .views import AllPins, Search
from .views import post_create, post_delete

urlpatterns= [
    path('', MainPage, name='main_page'),
    path('category/', Category.as_view(), name='category'),
    path('category<slug:slug>/', PinsView.as_view(), name='selected_category'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accountsregister/', Register.as_view(),name='registrations'),
    path('', include('django.contrib.auth.urls')),
    path('accounts/success/',Success, name='successreg'),
    path('pins<slug:slug>/', PinsDetail.as_view(), name = 'pins_detail'),
    path('allpin/', AllPins.as_view(), name='allpins'),
    path('searchresult/', Search.as_view(), name='search'),
    path('createpin/', post_create, name='createapin'),
    
]



