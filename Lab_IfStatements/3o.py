def determine_progress3(percentage):
    if percentage == 100:
        return "Complete"
    elif percentage >= 75:
        return "Nearly complete"
    elif percentage >= 50:
        return "Halfway there"
    elif percentage >= 25:
        return "Getting started"
    elif percentage >= 0:
        return "Just started"
    else:
        return "Invalid input"
