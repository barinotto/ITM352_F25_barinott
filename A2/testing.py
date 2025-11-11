# Ben Barinotto
# Sales Dashboard Application

# I was succuesfully able to load my google drive link and I confirmed that the it would also show the appropriate message if the link was not able to load (I deleted parts of the link and it was able to let me know what was wrong)

# Now I'm adding colors to my loading and error messages for better visibility
# I tested it once again with all the colors I implemented on the loading message, the time to load, and the warning message.
# plus the error message if the data fails to load

# Just testing to see if the changes I made to necesssay columsn will give me an error message for "gang"
    # I was infact correct and the warning message popped up! And does't when I ran it with the correct columns

# I ran into an issue when fulfillling R7 where I need to ask the user for a date range. I had not called the function in main() so I fixed that.

# I am correcting now the validity of inputs for the date range as it would stop the prgram if an invliad input was submitted. Starting at line 83

# I also added a welcome message for the user when they start the program at line 54 so that it cleans up the user experience

# Starting on R2 now, I need to create an interactive command line menu for the user to select options from.
# I am going to use ChatGPT to help me get started on a skeleton of this menu and added a sales_total column since that does not exist in the data.

# I accidentally called the get_range function twice so I removed the one in main() and left the one after main() where it makes more sense.

# I have run every single menu item thus far and they all work as intended. Now I am going to add comments to the code to explain what each part does for clarity.

# added my bonues analytic requirement (R8) after the main menu function which was a simple fix because the problems lit up as soon as I tried to save but was able to add it on the menu and easily able to add it.

# I have ran through all the menu items with success for each one + the bonus one. The bonus requirement was a bit more difficutl to work around since it required more grouping and getting percentages from a table that we can't easily just do math. We had to get sales total first which thankfully we already had and then do math and then convert to percentage
# So basically was using more functions from pandas to get the desired result.

#final edits made to Sales_dashboard.py before submission like accidental repeats and cleaning up comments.