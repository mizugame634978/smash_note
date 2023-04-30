from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings
app_name="smash_note"


urlpatterns = [
    path('',views.CharacterSelect.as_view(),name='character_index'),#name=によりhtml上でcharaという名前で呼び出せる
    path('<int:pk>/',views.CharacterDetailView.as_view(),name="character_detail"),
    path('create/',views.MemoCreateView.as_view(),name='memo_create'),
    #path('<int:pk>/update/',views.MemoUpdateView.as_view(),name='memo_update'),


]


