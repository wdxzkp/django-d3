"""PyDataVisualization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from d3Views import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^indenttree/', views.indenttree),
    url(r'^voronoi/', views.voronoi),
    url(r'^circlepacking/', views.circlepacking),
    url(r'^sunburst/', views.sunburst),
    url(r'^bubble/', views.bubble),
    url(r'^plane/', views.plane),
    url(r'^sankey/', views.sankey),
    url(r'^sankeychart/', views.sankeychart),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
