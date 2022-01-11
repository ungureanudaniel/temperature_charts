from django.contrib import admin
from django.urls import path, include
# import debug_toolbar
from django.conf import settings
from django.contrib.auth import views as auth_views
from users.views import register, user_login, contact, about, privacy, account, terms
from django.conf.urls.static import static
app_name = 'users'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_login, name='login'),
    path('register/', register, name='register'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    # path('review/', include('review.urls')),
    path('account/', account, name='account'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('privacy-policy/', privacy, name='privacy-policy'),
    path('terms-of-service/', terms, name='terms-of-service'),
    path('', include('users.urls')),
    path('', include('temperature_data.urls')),
    path('captcha/', include('captcha.urls')),
    # path('__debug__/', include(debug_toolbar.urls)),
    # path('', include('pwa.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
