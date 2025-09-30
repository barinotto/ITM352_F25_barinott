def determine_progress4(percentage):
    # List of messages in order of increasing progress
    messages = ["Just started", "Getting started", "Halfway there", "Nearly complete", "Complete"]
    
    # Compute index based on percentage
    index = min(percentage // 25, 4)  # integer division, capped at 4
    
    # Handle invalid input
    if percentage < 0 or percentage > 100:
        return "Invalid input"
    
    return messages[index]
