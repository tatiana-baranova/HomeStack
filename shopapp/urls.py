from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ItemPage, ItemEdit

router = SimpleRouter()

router.register('api/items', ItemPage)
urlpatterns = []
urlpatterns += router.urls

urlpatterns += [
    path("api/edit-item/<slug:slug>", ItemEdit.as_view()),
]