def rule_based_ai(weather):
    if weather == "sunny":
        return "Go for a walk."
    elif weather == "rainy":
        return "Read a book indoors."
    elif weather == "snowy":
        return "Build a snowman."
    else:
        return "Stay at home and relax."

current_weather = input(str("Enter the current weather (sunny, rainy, snowy): "))
print(rule_based_ai(current_weather))