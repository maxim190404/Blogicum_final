from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]

handler403 = 'pages.views.page_403'
handler404 = 'pages.views.page_404'
handler500 = 'pages.views.page_500'
