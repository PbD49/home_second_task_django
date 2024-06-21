from django.http import HttpResponse
from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


# Create your views here.
def answer_data(request, recipe_name):
    """Сервис-помощник для приготовления блюд"""
    template_page = 'index.html'
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get(recipe_name, None)
    if recipe:
        context = {
            'recipe': {
                key: value * servings for key, value in recipe.items()
            }
        }
        return render(request, template_page, context)
    else:
        return HttpResponse("Рецепт не найден!")
