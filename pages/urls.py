from django.urls import path
from pages.views import home, contact, about, member, team

urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('about/', about),
    path('members/', team, name="team"),
    path('category/<int:cat_id>/member/<int:mem_id>/', member, name="member"),
]