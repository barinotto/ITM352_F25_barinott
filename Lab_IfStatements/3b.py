def determine_progress2(percentage):
    if percentage == 100:
        return "Complete"
    if percentage >= 75:
        return "Nearly complete"
    if percentage >= 50:
        return "Halfway there"
    if percentage >= 25:
        return "Getting started"
    if percentage >= 0:
        return "Just started"
    return "Invalid input"
