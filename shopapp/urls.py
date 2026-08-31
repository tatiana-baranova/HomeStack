from rest_framework.routers import SimpleRouter
from .views import ItemPage

router = SimpleRouter()

router.register('api/items', ItemPage)
urlpatterns = []
urlpatterns += router.urls