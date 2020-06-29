from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
	path('',views.index, name='index'),
	path('home/',views.home, name='home'),
	path('boys/ranking2/',views.ranking2, name='ranking2'),
	path('boys',views.boys, name='boys'),
	path('home/ranking/',views.rankings,name='ranking'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


