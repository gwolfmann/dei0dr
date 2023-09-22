from rest_framework.routers import DefaultRouter
from .api import AlimentTypeViewSet, IngredientViewSet, IngredientInRecipeViewSet, RecipeViewSet

router = DefaultRouter()
router.register(r'meal/aliment-type', AlimentTypeViewSet)
router.register(r'meal/ingredient', IngredientViewSet)
router.register(r'meal/ingredient-in-recipe', IngredientInRecipeViewSet)
router.register(r'meal/recipe', RecipeViewSet)

urlpatterns = router.urls
