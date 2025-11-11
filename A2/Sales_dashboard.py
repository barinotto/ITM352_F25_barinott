# Ben Barinotto
# Build a sales dashboard - Assignment 2
# This dashboard shall allow users to explore and analyze data in various dimensions (eg. by region, employee, product, and customer)
# I will include defensive programming (like the try/except blocks) to handle potential errors gracefully.

#---------------------------------------------------------------------------------------------------------
# REQUIREMENT 1 = Loading Sales Data

#import the libraries
import pandas as pd
import sys
import time
from pathlib import Path

# Use the Google Drive file id and a direct-download URL so pandas can read it
file_id = "1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

#loads the google drive csv into a pandas dataframe
def load_sales_dataframe(csv_url: str) -> pd.DataFrame:
    #For better visibility, I added color to the loading message compared to the actual pivot tables being in white.
    print("\033[94mLoading sales data...\033[0m")
	#This will start the timer for the initial timestamp for when the user runs the program
    start = time.perf_counter()

    try:
        # Try to read the CSV file directly from the URL
        df = pd.read_csv(csv_url)
    except Exception as e:
        # My defensive programming to catch errors like if the dataset cannot be loaded for any reason
		#also made it red for visibility
        print(f"\033[91m[❌ Failed to load data: {e}\033[0m")
        sys.exit(1)  # Stop the program safely

    elapsed = time.perf_counter() - start
	#making message green for clear visibility
    print(f"\033[92mLoad successful Duration: ({elapsed:.2f}s)\033[0m")
    return df, elapsed

def main():
    try:
        df, elapsed = load_sales_dataframe(url)
    except Exception as e:
        print(f"\033[91mFailed to load sales data: {e}\033[0m")
        # this is used to break the code from running any further if there is an error loading the data
        sys.exit(1)

    # show rows and columns
    n_rows = len(df)
    print(f"Rows loaded: {n_rows}, Columns loaded: {len(df.columns)}")
    # making a new line for the column list for better readability
    print("Columns:", df.columns.tolist())

    #printing a welcome message for the user
    print("\n\033[1;32mWelcome to the Sales Dashboard!📊\033[0m")

    # replace missing data with zeros as requested
    df.fillna(0, inplace=True)

    # converting order_date to datetime format so that pandas can read it properly and use it.    
    df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', errors='coerce')

    # this is like my checklist so that I can make sure all the necessary columns are present for the dashboard to work properly.
    necessary_columns = ['sales_region', 'order_type', 'customer_state', 'customer_type', 'produce_name', 'quantity', 'unit_price', 'product_category', 'employee_id']
    missing_columns = [col for col in necessary_columns if col not in df.columns]

    #Here we defensive programming/error handling to make sure/anticipate any issues within the file are caught asap before starting the analysis.
    if missing_columns:
        print(f"\033[93m⚠️ Warning!!\033[0m Missing necessary columns: {missing_columns}. Some analytics may not function without them!⚠️")
    else:
        print("\033[94m All necessary columns are here! ✅\033[0m")
    return df

#---------------------------------------------------------------------------------------------------------
# INDIVIDUAL REQUIREMENT = "7. Before performing an analysis, ask the user what date range of sales data to use. Use only that range for the analysis."

# I am using ChatGPT to get me started with a skeleton of this function, then I will modify it to fit my needs with more comments and error handling.
def get_date_range(df):
    # this will prompt the user to enter a date range for analysis and filter the dataframe accordingly
    print("\nPlease enter the date range for analysis (YYYY-MM-DD format):")

    # Finding the earlierst and latest dates in the dataset to help the user know what range is available
    min_date = df['order_date'].min()
    max_date = df['order_date'].max()
    # printing so that the user knows what range to choose from
    print(f"\033[94mAvailable date range in dataset:\033[0m "  # Blue label only
      f"\033[1;37m{min_date.date()}\033[0m to \033[1;37m{max_date.date()}\033[0m")

    # including a shortcut to just view the entire range for my own checking purposes + it makes it easier if the user wants to see the entire range
    print("Press \033[1mall\033[0m or just press \033[1mEnter\033[0m to use the full available range.")

    # lopping until I get a valid input and not kicking the user out of the program because of it.
    while True:
        # read raw input first
        start_raw = input("Start date: ").strip().lower()

        # this is to access the full range faster
        if start_raw in ("", "all"):
            start_date = min_date
            end_date = max_date
            filtered_df = df[(df['order_date'] >= start_date) & (df['order_date'] <= end_date)]
            print(f"\033[94mUsing sales data from {start_date.date()} to {end_date.date()} ({len(filtered_df)} records)\033[0m")
            return filtered_df
        
        # my reminder that "coerce" will turn invalid dates into NaT
        start_date = pd.to_datetime(start_raw, errors='coerce')  # parse the first input you already read


        # Validate input for start date first
        if pd.isna(start_date):
            print("\033[91mInvalid start date. Please use the format YYYY-MM-DD.\033[0m")
        elif start_date < min_date or start_date > max_date:
            print(f"\033[91mStart date out of range. Dataset dates are between {min_date.date()} and {max_date.date()}.\033[0m")
        else:
            break

    # looping until a valid end date is submitted again
    while True:
        end_date = input("End date: ")
        end_date = pd.to_datetime(end_date, errors='coerce')

        # Validate input
        if pd.isna(end_date):
            print("\033[91mInvalid end date. Please use the format YYYY-MM-DD.\033[0m")
        elif start_date > end_date:
            print("\033[91mStart date cannot be after end date.\033[0m")
        elif end_date < min_date or end_date > max_date:
            print(f"\033[91mEnd date out of range. Dataset dates are between {min_date.date()} and {max_date.date()}.\033[0m")
        else:
            break

    # Filter and confirm
    filtered_df = df[(df['order_date'] >= start_date) & (df['order_date'] <= end_date)]
    print(f"\033[94mUsing sales data from {start_date.date()} to {end_date.date()} ({len(filtered_df)} records)\033[0m")

    return filtered_df

#---------------------------------------------------------------------------------------------------------
# REQUIREMENT 2 = Interactive Command line Menu (at the end of this section) & 
# REQUIREMENT 3 - Predefined analytical tasks

# I aboslutely needed the help of ChatGPT to get me started with a skeleton of this menu, then I will modify it to fit my needs with more comments and error handling. 
#

def _ensure_sales_total(df: pd.DataFrame) -> pd.DataFrame:
   # Adding a sales total since that column does not exist and is computed from quantity * unit_price
    if 'sales_total' not in df.columns:
        if 'quantity' in df.columns and 'unit_price' in df.columns:
            df = df.copy()
            df['sales_total'] = pd.to_numeric(df['quantity'], errors='coerce') * pd.to_numeric(df['unit_price'], errors='coerce')
        else:
            print("\033[91mMissing 'quantity' or 'unit_price'—cannot compute sales_total.\033[0m")
    return df

# 1) Show the first n rows of sales data
# to follow the prefined functinos of adding all rows or skipping preview or showing n rows
def show_first_n(df: pd.DataFrame):
    total = len(df)
    print(f"\nRows available: {total}")
    print("Enter a number 1 to {0}".format(total - 1))
    print("To see all rows, enter 'all'")
    print("To skip preview, press Enter")
    choice = input("Your choice: ").strip().lower()

    if choice == "":              # skip preview
        return
    if choice == "all":           # show all rows
        print(df.to_string(index=False))
        return
    if not choice.isdigit():      # reject non-numeric
        print("\033[91mInvalid input. Please enter a number, 'all', or press Enter.\033[0m")
        return

    n = int(choice)
    if not (1 <= n <= total - 1): # enforce range
        print(f"\033[91mOut of range. Enter 1 to {total - 1}, 'all', or press Enter.\033[0m")
        return

    print(df.head(n).to_string(index=False))

# 2) Total sales by region and order_type
# first pivot table being crated , I just wanted say that :)
def total_sales_by_region_and_order_type(df: pd.DataFrame):
    df2 = _ensure_sales_total(df)
    pivot = pd.pivot_table(df2,
                           index=['sales_region'],
                           columns=['order_type'],
                           values='sales_total',
                           aggfunc='sum',
                           fill_value=0,
                           margins=True,
                           margins_name='Total')
    print(pivot)

# 3) Average sales by region with average sales by state and sale type
def average_sales_by_region_state_type(df: pd.DataFrame):
    #using df2 because we made a copy in line 133 so that we don't modify the original dataframe for each of these 10 command functions.
    df2 = _ensure_sales_total(df)

    # Region-only average
    print("\n\033[94mAverage sales by region (overall):\033[0m")
    by_region = pd.pivot_table(
        df2,
        index=['sales_region'],
        values='sales_total',
        aggfunc='mean'
    )
    print(by_region)

    # Region with sub-columns (state × sale type)
    print("\n\033[94mAverage sales by region with sub-columns (state × sale type):\033[0m")
    by_region_subcols = pd.pivot_table(
        df2,
        index=['sales_region'],
        columns=['customer_state', 'order_type'],
        values='sales_total',
        aggfunc='mean',
        fill_value=0
    )
    print(by_region_subcols)

# 4) Sales by customer type and order type by state
    # this one was pretty much left untouched from what ChatGPT generated for me because it printed out just perfect without any need for modications
def sales_by_customer_type_order_type_state(df: pd.DataFrame):
    df2 = _ensure_sales_total(df)
    pivot = pd.pivot_table(
        df2,
        index=['customer_state', 'customer_type', 'order_type'],  # sub-rows
        values='sales_total',
        aggfunc='sum',
        fill_value=0
    )
    print(pivot)


# 5) Total sales quantity and price by region and product
    # same for this step, very little modifications needed from what ChatGPT generated for me
def total_qty_price_by_region_product(df: pd.DataFrame):
    df2 = _ensure_sales_total(df)
    pivot = pd.pivot_table(df2,
                           index=['sales_region', 'produce_name'],
                           values=['quantity', 'sales_total'],
                           aggfunc='sum',
                           fill_value=0)
    print(pivot)

# 6) Total sales quantity and price by customer type
    # just to clarify, I have used AI to clarify what df2 means for each of these functions that I didn't really need to modify since it's running well as is.
def total_qty_price_by_customer_type(df: pd.DataFrame):
    df2 = _ensure_sales_total(df)
    pivot = pd.pivot_table(
        df2,
        index=['customer_type', 'order_type'],
        values=['quantity', 'sales_total'],
        aggfunc='sum',
        fill_value=0
    )
    print(pivot)


# 7) Max and min sales price of sales by category
def max_min_price_by_category(df: pd.DataFrame):
    df2 = _ensure_sales_total(df)
    "Interpret “sales price” as unit_price; include sales_total bounds too" # the message on the left was written by ChatGPT, to my understanding it means that we are grouping by product category and finding max/min of unit_price and sales_total
    grouped = df2.groupby('product_category').agg(
        max_unit_price=('unit_price', 'max'),
        min_unit_price=('unit_price', 'min'),
        max_sales_total=('sales_total', 'max'),
        min_sales_total=('sales_total', 'min'),
    )
    print(grouped)

# 8) Number of unique employees by region
# like the short and sweetness of this one in our code but in our results as well . Only con is breaking it down if the code hadn't worked but it gives us varierty in the code which i don't know is a good thing or not. Probably not but I'm keeping it.
def unique_employees_by_region(df: pd.DataFrame):
    result = df.groupby('sales_region')['employee_id'].nunique().rename('unique_employees')
    print(result)

#----------------------------------------------------------------------------------------------------------
# REQUIREMENT 4 - Create custom pivot table

# 9) Create a custom pivot table
# this one was probaly the most difficult one to get right since it required a lot of user input and error handling to make sure the pivot table is created correctly based on user choices.

def custom_pivot(df: pd.DataFrame):
    # this ensure sales total column exists
    df2 = _ensure_sales_total(df)
    print("\nEnter comma-separated lists (leave blank to skip a dimension).")
    #this next four lines are the basics needed to create and customize a pivot table for what the user is looking for
    idx = input("Index fields (e.g., sales_region,customer_state): ").strip()
    cols = input("Column fields (e.g., order_type or customer_type): ").strip()
    vals = input("Value field(s) (e.g., sales_total,quantity,unit_price): ").strip()
    agg  = input("Aggregation (sum, mean, max, min, count) [default=sum]: ").strip().lower() or 'sum'
    
    # this is to parse the inputs.
    index = [s.strip() for s in idx.split(',')] if idx else None
    columns = [s.strip() for s in cols.split(',')] if cols else None
    values = [s.strip() for s in vals.split(',')] if vals else None

    # this helps accept more inputs for the same aggregation function and then default to sum if the input cannot determine what the user input was supposed to indicate.
    valid_aggs = {'sum': 'sum', 'mean': 'mean', 'avg': 'mean', 'max': 'max', 'min': 'min', 'count': 'count'}
    aggfunc = valid_aggs.get(agg, 'sum')

    #this is what actually builds the pivot table based on user inputs and error handling to catch any issues.
    try:
        pivot = pd.pivot_table(df2,
                               index=index,
                               columns=columns,
                               values=values,
                               aggfunc=aggfunc,
                               fill_value=0)
        print(pivot)
    #this is our error handling so the program doesn't crash and instead notifies the user of the issue.
    except Exception as e:
        print(f"\033[91mFailed to build pivot: {e}\033[0m")

# 10) Exit
def exit_menu(_df: pd.DataFrame):
    print("\033[92mGoodbye! Thanks for using our Sales Dashboard Application :)\033[0m")

#----------------------------------------------------------------------------------------------------------
# INDIVIDUAL REQUIREMENT 8 - Sales by region and product, including % of region totals

# I decided to label this as a bonus since this was a separate requirement so that it didn't affect the other requirements in the list.

# 11 (BONUS) 
def percent_by_region_and_product(df: pd.DataFrame):
    """
    Sales by region and product, including % of region totals
    for both quantity and sales_total. Percent columns are added.
    """ # This is ChatGPT's explanation for what the lab requirement called for what is pretty straightforward to me so I don't feel like I need to explain in my own terms.
    df2 = _ensure_sales_total(df)

    # 1) Aggregate to region×product
    # This allows the grouping so that its then presented in a pivot table format as columns.
    grp = (
        df2.groupby(['sales_region', 'produce_name'])
           .agg(quantity=('quantity', 'sum'),
                sales_total=('sales_total', 'sum'))
           .reset_index()
    )
    # defensive programming check
    if grp.empty:
        print("\033[93mNo rows after filtering. Nothing to summarize.\033[0m")
        return

    # 2) Compute region totals (denominators)
    # sums by the region for both quantity and sales total
    region_totals = grp.groupby('sales_region')[['quantity', 'sales_total']].transform('sum')

    # 3) Add % of region columns
    # we are getting our percentages here as a fraction of the total region sales
    grp['qty_pct_of_region']   = grp['quantity']    / region_totals['quantity']
    grp['sales_pct_of_region'] = grp['sales_total'] / region_totals['sales_total']

    # 4) Make % readable (0–100 with 2 decimals)
    # now we convert those fractions to percentages as required by the lab instructions
    grp['qty_pct_of_region']   = (grp['qty_pct_of_region'] * 100).round(2)
    grp['sales_pct_of_region'] = (grp['sales_pct_of_region'] * 100).round(2)

    # 5) Sort by region then descending sales share
    # this is to help readility when printed out in the terminal
    grp = grp.sort_values(['sales_region', 'sales_pct_of_region'], ascending=[True, False])

    # 6) Print as a compact “pivot-like” table
    #    (index=False keeps it clean in the terminal)
    # this is to display our selected columns only for better readability
    print(
        grp[['sales_region', 'produce_name', 'quantity', 'sales_total',
             'qty_pct_of_region', 'sales_pct_of_region']].to_string(index=False)
    )
#----------------------------------------------------------------------------------------------------------
# Back to R2 & 3 to finish off 

# These are the menu items to be able to adjust by reordering or adding new items easily.
MENU: tuple[tuple[str, callable], ...] = (
    ("Show the first n rows of sales data",              show_first_n),
    ("Total sales by region and order_type",             total_sales_by_region_and_order_type),
    ("Average sales by region with average sales by state and sale type", average_sales_by_region_state_type),
    ("Sales by customer type and order type by state",   sales_by_customer_type_order_type_state),
    ("Total sales quantity and price by region and product", total_qty_price_by_region_product),
    ("Total sales quantity and price customer type",     total_qty_price_by_customer_type),
    ("Max and min sales price of sales by category",     max_min_price_by_category),
    ("Number of unique employees by region",             unique_employees_by_region),
    ("Create a custom pivot table",                      custom_pivot),
    ("Sales by region and product with % of region totals", percent_by_region_and_product),
    ("Exit",                                             exit_menu),
)

def run_menu(df: pd.DataFrame):
    """Main loop for the text-based dashboard.""" # This message was written by ChatGPT to clarify the purpose of this function. Which basically means that this loop is here to keep the menu running until the user decides to exit rather than automatically ending after one selection and mkaing the user run the prgogram again.
    while True:
        print("\n--- Sales Data Dashboard ---")
        for i, (label, _fn) in enumerate(MENU, start=1):
            print(f"{i}. {label}")
        choice = input("Select an option (1–{0}): ".format(len(MENU))).strip()

        # Validate choice
        if not choice.isdigit():
            print("\033[91mPlease enter a number.\033[0m"); continue
        idx = int(choice) - 1
        if idx < 0 or idx >= len(MENU):
            print("\033[91mInvalid menu option.\033[0m"); continue

        label, fn = MENU[idx]

        # Exit path
        if fn is exit_menu:
            fn(df)
            break

        # Execute the selected item
        #defensive progeramming to catch any errors that may occur during the execution of the selected menu item.
        try:
            fn(df)
        except KeyboardInterrupt:
            print("\n\033[93mOperation cancelled by user.\033[0m")
        except Exception as e:
            print(f"\033[91mError running '{label}': {e}\033[0m")


if __name__ == "__main__":
    df = main()
    df_filtered = get_date_range(df)
    run_menu(df_filtered)





