from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('cat/',views.cat,name='cat'),
    path('categ/<str:cat>',views.categ,name='categ'),
    path('contact/',views.contact,name='contact'),
    path('single/<int:code>',views.single,name='single'),
    path('login/',views.login, name='login'),
    # path('draftlogin/',views.draftlogin, name='draftlogin'),
    path ('showall/',views.showall,name='showall'),
    path("delete/<int:obj>",views.delete,name='delete'),
    path("draftdelete/<int:obj>",views.draftdelete,name='draftdelete'),
    path("edit/<int:id>",views.edit,name='edit'),
    path('createpost/',views.createPost,name='createPost'),
    path('draft/',views.draft,name='draft'),
    path('about/',views.about,name='about'),
    path('addcat/',views.addcat,name='addcat')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)