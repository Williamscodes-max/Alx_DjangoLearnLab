# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls')),          # your blog app URLs
#     path('accounts/', include('django.contrib.auth.urls')),  # 👈 add this
# ]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
]
