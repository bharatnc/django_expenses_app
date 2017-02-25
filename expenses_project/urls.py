from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^expenses/', include("expenses.urls")),
    url(r'^', include("main.urls")),
]
