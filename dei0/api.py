from rest_framework import viewsets
from .models import AlimentType, Ingredient, IngredientInRecipe, Recipe
from .serializers import AlimentTypeSerializer, IngredientSerializer, IngredientInRecipeSerializer, RecipeReadSerializer, RecipeWriteSerializer

class AlimentTypeViewSet(viewsets.ModelViewSet):
    queryset = AlimentType.objects.all().order_by('id')
    serializer_class = AlimentTypeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('id')
    serializer_class = IngredientSerializer

class IngredientInRecipeViewSet(viewsets.ModelViewSet):
    queryset = IngredientInRecipe.objects.all()
    serializer_class = IngredientInRecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('id')    
#    serializer_class = RecipeSerializer
    def get_serializer_class(self):
        print(self.action)
        if self.action in ['create','update','partial_update']:
            return RecipeWriteSerializer
        return RecipeReadSerializer
