
from django.urls import path
from .views import homepage,muscianpage,albumpage,editalbum,deletedata,editmuscian
urlpatterns = [
   
   path('',homepage,name='home_page'),
   path('muscian/',muscianpage, name='muscian_page'),
   path('album/',albumpage, name='album_page'),
   path('editalbum/<int:id>/',editalbum, name='edit_album'),
   path('deletealbum/<int:id>/',deletedata, name='delete_album'),
   path('eidtmuscian/<int:id>/',editmuscian, name='edit_muscian'),

]
