from django.contrib import admin

from .models import Ingredient, IngredientRecipe, Recipe, Tag
EMPTY = '-пусто-'


class IngredientInline(admin.TabularInline):
    model = IngredientRecipe


@admin.register(IngredientRecipe)
class IngredientRecipe(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')
    empty_value_display = EMPTY
    search_fields = ('ingredient__name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'cooking_time', 'text', 'author',
                    'ingredients_count', 'tags_count', 'favorites_count',
                    'shopping_cart_count')
    inlines = (IngredientInline,)
    empty_value_display = EMPTY
    list_filter = ('author', 'tags')
    search_fields = ('name',)

    def ingredients_count(self, obj):
        return obj.ingredients.count()

    def tags_count(self, obj):
        return obj.tags.count()

    def favorites_count(self, obj):
        return obj.favorites.count()

    def shopping_cart_count(self, obj):
        return obj.shopping_cart.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    empty_value_display = EMPTY


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    empty_value_display = EMPTY
