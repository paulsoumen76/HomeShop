"""ecommecrce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from homeshop import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', views.about_us),
    url(r'^$', views.home_view),
    url(r'^mobiles/', views.mobile_view),
    url(r'^laptops/', views.laptop_view),
    url(r'^speakers/', views.speaker_view),
    url(r'^menshirts/', views.menshirt_view),
    url(r'^menjeans/', views.menjeans_view),
    url(r'^mentshirts/', views.mentshirt_view),
    url(r'^womentshirts/', views.womentshirt_view),
    url(r'^womenjeans/', views.womenjeans_view),
    url(r'^womenkurtas/', views.womenkurta_view),
    url(r'^(?P<id>\d+)/$', views.mobile_detail_view),
    url(r'^cart/', views.cart_view),
    url(r'^search/', views.search_view),
    url(r'^signup/', views.signup_view),
    url(r'^accounts/', include("django.contrib.auth.urls")),
    url(r'^checkout/', views.placeorder_view),
    url(r'^get-pdf/', views.getpdfpage),
    url(r'^paytm/', views.payment_handler , name='paytm'),
    url(r'^contact/', views.saved_contact_view , name='contact'),
    # url(r'^success/', views.success_view,name='success'),
    # url(r'^failure/', views.failure,name='failure'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
