# Python Budget Planner

An academic Python project that analyzes monthly expense records and recommends a budget based on historical spending.

## Features

- Reads expense records from text files.
- Groups expenses by category.
- Calculates monthly averages for categories appearing in multiple months.
- Combines categories appearing in only one month into a sinking fund for occasional spending.
- Reports unavailable files and requires at least two successfully loaded months.

## File Format

Each expense record uses three comma-separated fields:

description,amount,category

Example:

Groceries,75.50,Food
Gas,40.00,Transportation

Monthly files follow this naming convention:

jan_expenses.txt
feb_expenses.txt
mar_expenses.txt

## How to Run

Requires Python 3 and uses no external libraries.

1. Keep budgetPlanner.py and the expense files in the same folder.
2. Open a terminal in that folder.
3. Run:

   python budgetPlanner.py

4. Enter the months to analyze, separated by commas without spaces:

   jan,feb,mar,apr,may

The program prints recommended monthly amounts for recurring categories and a sinking fund for occasional expenses.

## Calculation Method

For recurring categories, total spending is divided by the number of successfully loaded months.

Categories that appear in only one loaded month are combined, then divided by the number of loaded months to estimate a monthly sinking fund.

## Skills Demonstrated

- Python functions, loops, lists, and dictionaries
- Text-file reading and data parsing
- Category aggregation and arithmetic analysis
- Command-line user interaction
- Basic exception handling

## Current Limitations

- Input must use matching month names without spaces.
- Expense records must follow the expected format.
- Spending frequency determines how categories are classified.
- Results are printed to the terminal rather than saved.

## Author

Wesley Werner
University of Missouri — Industrial Engineering
