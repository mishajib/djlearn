from django.urls import path
from pages.views import home, contact, about, member, team

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('members/', team, name="team"),
    path('category/<int:cat_id>/member/<int:mem_id>/', member, name="member"),
]
