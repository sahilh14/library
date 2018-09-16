from django.conf.urls import url
from django.views.generic import TemplateView
from books import views

urlpatterns = [
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^display/([0-9]{1,2})$', views.display),
    url(r'^display$', views.displayhome),
    url(r'^insert/$', views.insert),
    url(r'^about/$', TemplateView.as_view(template_name='books/search_form.html')),
    url(r'^about-custom/$', views.AboutView.as_view())
]
