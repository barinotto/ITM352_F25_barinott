# Step 1: Define the function
def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress

# Step 2: Define the test function
def test_determine_progress(progress_function):
    assert progress_function(10, 0) == "Get going!"
    assert progress_function(0, 5) == "Get going!"
    assert progress_function(1, 10) == "On your way!"
    assert progress_function(3, 10) == "Almost there!"
    assert progress_function(4, 8) == "You win!"
    print("All tests passed!")

# Step 3: Call the test function
test_determine_progress(determine_progress1)
