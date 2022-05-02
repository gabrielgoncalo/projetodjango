from django.urls import path

from recipes.views import create_view

urlpatterns = [
    #   path('admin/', admin.site.urls),
    path('', create_view),
    #path('view/', create_view),


]
