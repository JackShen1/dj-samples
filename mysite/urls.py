import os
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.contrib.auth import views as auth_views

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

    path('concentus/', include('concentus.urls')),
    path('constellation/', include('constellation.urls')),
    path('expressionism/', include('expressionism.urls')),
    path('expressionism2/', include('expressionism2.urls')),
    path('fractal/', include('fractal.urls')),
    path('galaxy/', include('galaxy.urls')),
    path('heartverse/', include('heartverse.urls')),
    path('infinity/', include('infinity.urls')),
    path('neon/', include('neon.urls')),
    path('phoenix/', include('phoenix.urls')),
    path('spirals/', include('spirals.urls')),
    path('whirlpool/', include('whirlpool.urls')),
]

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