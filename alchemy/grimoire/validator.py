def validate_ingredients(ingredients: str) -> str:
    valid_ingred = [ "fire", "water", "earth", "air" ]
    list_ing = ingredients.split()
    for i in list_ing:
        if i not in valid_ingred :
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
