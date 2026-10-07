def load_month(file_name):
    file = open(file_name)
    data = []

    for line in file:
        line = line.strip()

        if line != "":
            parts = line.split(",")

            amount = float(parts[1])
            category = parts[2]

            data.append([amount, category])

    file.close()
    return data


def process_months(months):
    all_data = []
    month_count = 0

    for m in months:
        file_name = m + "_expenses.txt"

        try:
            data = load_month(file_name)
            all_data.append(data)
            month_count = month_count + 1
        except:
            print("You do not have the expenses record for", m + ".")

    return all_data, month_count


def calculate_budget(all_data, month_count):
    category_totals = {}
    category_months = {}

    for month_data in all_data:
        seen = []

        for item in month_data:
            amount = item[0]
            category = item[1]

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] = category_totals[category] + amount

            if category not in seen:
                seen.append(category)

        for category in seen:
            if category not in category_months:
                category_months[category] = 0

            category_months[category] = category_months[category] + 1

    print("Based on the analysis of your expenses for the selected months, your budget is calculated as follows:")

    sinking_total = 0
    sinking_categories = []

    for category in category_totals:
        if category_months[category] > 1:
            print(category + ":", category_totals[category] / month_count)
        else:
            sinking_total = sinking_total + category_totals[category]
            sinking_categories.append(category)

    print()
    print("Finally, you should leave $" + str(sinking_total / month_count) + " as sinking fund for occasional spending, such as things in the categories of:")

    for category in sinking_categories:
        print(category)


def main():
    months_input = input("Which months' expenses should be used to plan the budget: ")
    months = months_input.split(",")

    all_data, month_count = process_months(months)

    if month_count < 2:
        print("Insufficient data to calculate the budget. You select more than one month.")
    else:
        calculate_budget(all_data, month_count)


main()