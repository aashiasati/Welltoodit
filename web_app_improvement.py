# 🌟 Hacktoberfest 2025 – Python Web App Improvement Example
# Author: Aashi Asati
# Description: Added search functionality and data handling in Python

def search_items(items, query):
    """
    Function to filter items based on a search query.
    :param items: List of dictionaries with 'name' and 'category'
    :param query: String to search in item names
    :return: Filtered list of items
    """
    if not query:
        return items  # if no query, return all items
    return [item for item in items if query.lower() in item['name'].lower()]

def display_items(items):
    """
    Function to display items in a readable format
    """
    if not items:
        print("⚠ No items found.")
        return
    print("🌟 Item List 🌟")
    for idx, item in enumerate(items, start=1):
        print(f"{idx}. {item['name']} - {item['category']}")

def main():
    # Sample data
    items = [
        {"name": "Apple", "category": "Fruit"},
        {"name": "Banana", "category": "Fruit"},
        {"name": "Carrot", "category": "Vegetable"},
        {"name": "Broccoli", "category": "Vegetable"},
        {"name": "Mango", "category": "Fruit"}
    ]

    print("Welcome to the Python Web App Demo! 🎉")
    query = input("Enter search term (or press enter to show all): ").strip()

    filtered_items = search_items(items, query)
    display_items(filtered_items)

if _name_ == "_main_":
    main()
