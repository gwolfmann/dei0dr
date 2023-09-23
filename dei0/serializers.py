from rest_framework import serializers
from .models import AlimentType, Ingredient, IngredientInRecipe, Recipe

class AlimentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlimentType
        fields = ('id', 'name', 'type')

class CustomAlimentTypeField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, obj):
        serializer = AlimentTypeSerializer(obj)
        return serializer.data

class IngredientCreateUpdateSerializer(serializers.ModelSerializer):
    types = CustomAlimentTypeField(queryset=AlimentType.objects.all(), many=True, required=True)

    class Meta:
        model = Ingredient
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    types = serializers.PrimaryKeyRelatedField(queryset=AlimentType.objects.all(), many=True, required=True)

    class Meta:
        model = Ingredient
        fields = '__all__'

    def to_representation(self, instance):
        # Override the to_representation method to include additional information
        data = super().to_representation(instance)
        data['types'] = AlimentTypeSerializer(instance.types.all(), many=True).data
        return data
    

    def create(self, validated_data):
        # Remove 'types' from the validated_data if it's empty
        types = validated_data.pop('types', [])
        
        # Create the Ingredient instance without types
        ingredient = Ingredient.objects.create(**validated_data)

        # Add the types if they exist
        if types:
            ingredient.types.set(types)

        return ingredient


class IngredientInRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientInRecipe
        fields = ('ingredient','quantity','measure_unit')

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientInRecipeSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('name','preparation','ingredients')

    def create(self, validated_data):
        print(validated_data)
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            IngredientInRecipe.objects.create(recipe_id=recipe.id, **ingredient_data)
        return recipe

    def to_representation(self, instance):
        # Override the to_representation method to include additional information
        data = super().to_representation(instance)
        data['ingredients'] = IngredientInRecipeSerializer(instance.types.all(), many=True).data
        return data
