"""testbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from nutrient import views as nutrient_views
from datas import views as data_views
from personal import views as personal_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('feed', nutrient_views.FeedViewSet)
router.register('nutrient', nutrient_views.NutrientViewSet)
router.register('snack', nutrient_views.SnackViewSet)
router.register('exchangedfeed', nutrient_views.ExchangedFeedViewSet)
router.register('exchangednutrient', nutrient_views.ExchangedNutrientViewSet)
router.register('exchangedsnack', nutrient_views.ExchangedSnackViewSet)

# datas #
router.register('agerange', data_views.AgeRangeViewSet)


# personal data #
router.register('mypet', personal_views.MyPetViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('exchange_feed/', nutrient_views.exchange_feed, name=""),
    path('exchange_nutrient/', nutrient_views.exchange_nutrient, name=""),
    path('exchange_snack/', nutrient_views.exchange_snack, name=""),

]
