from django.urls import path

from recipes.views import create_view, list_view, detail_view, update_view

urlpatterns = [
    #   path('admin/', admin.site.urls),
    path('', create_view),
    #path('view/', create_view),
    path('list/', list_view),
    path('<id>/', detail_view),
    path('<id>/'+'update/', update_view),
]
