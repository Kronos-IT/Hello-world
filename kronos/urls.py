from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as authViews

from users import views as userView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('reg/', userView.register, name='reg'),
    path('profile/', userView.profile, name='profile'),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)