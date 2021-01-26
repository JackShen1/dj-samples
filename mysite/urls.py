import os

from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    # Sample applications
    path('ads/', include('ads.urls')),
    path('authz/', include('authz.urls')),
    path('chat/', include('chat.urls')),
    path('xmas-tree/', include('xmas-tree.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 ='home.views.error_404'

# Serve the favicon
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0, path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login)))
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')
