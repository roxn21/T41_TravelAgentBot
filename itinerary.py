def generate_itinerary(destination, days):
    if destination.lower() == "egypt":
        itinerary = [
            ("Cairo", ["Visit pyramids of Giza", "Nile river boating", "Visit Museum"]),
            ("Alexandria", ["Visit port of Alexandria", "Visit beaches"]),
        ]
    elif destination.lower() == "paris":
        itinerary = [
            ("Paris", ["Eiffel Tower", "Louvre Museum", "Notre Dame Cathedral"]),
        ]
    else:
        itinerary = [("Destination unknown", ["Explore the city!"])]
    
    result = f"Here is your itinerary for {days} days in {destination}:\n"
    for day, (city, activities) in enumerate(itinerary, start=1):
        result += f"{city} (Day {day}): {', '.join(activities)}\n"
    
    return result
