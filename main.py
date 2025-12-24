print("Restaurant Menu Assistant")
print("=" * 40)


def ask_assistant(user_query: str):
    query = user_query.lower()

    if "sushi" in query or "japanese" in query:
        return {
            "restaurant_name": "Sakura Sushi",
            "cuisine": "Japanese",
            "price_range": "$$",
            "recommendation": "Order the Chef's Omakase for a balanced tasting menu.",
            "must_try_dish": "Salmon Nigiri",
            "location": "Downtown"
        }

    if "bella pasta" in query or "italian" in query or "pasta" in query:
        return {
            "restaurant_name": "Bella Pasta",
            "cuisine": "Italian",
            "price_range": "$$",
            "recommendation": "Try the truffle tagliatelle for a rich, aromatic dish.",
            "must_try_dish": "Truffle Tagliatelle",
            "location": "Midtown"
        }

    if "mexican" in query or "taco" in query:
        return {
            "restaurant_name": "El Fuego",
            "cuisine": "Mexican",
            "price_range": "$",
            "recommendation": "Great choice for flavorful street-style food.",
            "must_try_dish": "Carne Asada Tacos",
            "location": "East Side"
        }

    if "indian" in query or "curry" in query:
        return {
            "restaurant_name": "Spice Route",
            "cuisine": "Indian",
            "price_range": "$$",
            "recommendation": "Perfect for rich, authentic regional flavors.",
            "must_try_dish": "Chicken Biryani",
            "location": "West End"
        }

    if "vegan" in query or "healthy" in query:
        return {
            "restaurant_name": "Green Bowl",
            "cuisine": "Vegan",
            "price_range": "$",
            "recommendation": "Fresh, nutritious plant-based meals.",
            "must_try_dish": "Buddha Bowl",
            "location": "Riverside"
        }

    if "french" in query or "fine dining" in query:
        return {
            "restaurant_name": "La Brasserie",
            "cuisine": "French",
            "price_range": "$$$",
            "recommendation": "Ideal for an upscale dining experience.",
            "must_try_dish": "Steak Frites",
            "location": "Uptown"
        }

    return "I'm here to help with restaurant recommendations! Are you looking for a place to dine?"


queries = [
    "I want to visit Paris next week",
    "Planning a trip to Tokyo in December",
    "What's the weather like in New York?",
    "Should I go to Sydney this summer?",
    "Tell me about London's weather",
    "What's the best time to travel?",
    "How are you doing?",
    "Where should I go for sushi?",
    "What's the best dish at Bella Pasta?"
]

for query in queries:
    print(f"\nQuery: {query}")
    response = ask_assistant(query)
    print("Response:")
    print(response)
    print("-" * 40)
