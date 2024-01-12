
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homeView.as_view(),name="home"),
    path('category/<slug:val>', views.CategoryView.as_view(),name="category"),
    path('details/<int:pk>', views.ProductDetailView.as_view(),name="details"),
    path('about/',views.aboutView.as_view(),name="about"),
    path('contact/',views.contactView.as_view(),name="contact"),
    path('register/',views.CustomerRegistrationView.as_view(),name="register")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
