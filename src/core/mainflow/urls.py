# from image.views import upload
# from image.views import data, dataDetail
# from django.urls import include, path 
# from django.conf.urls import url
# from django.contrib import admin
# # from image.views import *

# urlpatterns = [
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^admin/', admin.site.urls),
# ]

# urlpatterns += [
# 	path('',data.as_view()),
#     path('<int:pk>/',dataDetail.as_view()),
# ]



from django.urls.conf import path
from image.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# admin.autodiscover()

urlpatterns = [
        path('admin/', admin.site.urls),
        path('data/',data.as_view()),
        path('data/<int:pk>',dataDetail.as_view()),
        path('doc/',doc.as_view()),
        path('doc/edit/<int:pk>',docEdit.as_view()),
        path('doc/<int:pk>',docProceed.as_view()),
        

 ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)