from django.urls import path
from . import views

urlpatterns= [
    path('',views.MainPageView), 
    path('pdf/',views.PDFPageView, name='pdf'),
    path('pdfreport/',views.render_pdf_view,name="pdfreport")
]


