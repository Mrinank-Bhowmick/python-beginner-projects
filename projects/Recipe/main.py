import sqlite3


# Create a SQLite database and table to store recipes
def create_database():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            ingredients TEXT,
            instructions TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Add a new recipe to the database
def add_recipe():
    title = input("Enter recipe title: ")
    ingredients = input("Enter recipe ingredients (comma-separated): ")
    instructions = input("Enter recipe instructions: ")

    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?)",
                   (title, ingredients, instructions))
    conn.commit()
    conn.close()

# List all saved recipes
def list_recipes():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM recipes")
    recipes = cursor.fetchall()
    conn.close()

    if recipes:
        for recipe in recipes:
            print(f"{recipe[0]}. {recipe[1]}")
    else:
        print("No recipes found.")


# Search for a recipe by title
def search_recipe():
    keyword = input("Enter the recipe title to search for: ")

    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes WHERE title LIKE ?", (f"%{keyword}%",))
    recipes = cursor.fetchall()
    conn.close()


    if recipes:
        for recipe in recipes:
            print(f"Recipe ID: {recipe[0]}")
            print(f"Title: {recipe[1]}")
            print(f"Ingredients: {recipe[2]}")
            print(f"Instructions: {recipe[3]}\n")
    else:
        print("No matching recipes found.")


# Delete a recipe by ID
def delete_recipe():
    recipe_id = input("Enter the ID of the recipe to delete: ")

    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM recipes WHERE id=?", (recipe_id,))
    conn.commit()
    conn.close()
    print("Recipe deleted successfully.")


# Main menu
def main():
    create_database()

    while True:
        print("\nRecipe Organizer Menu:")
        print("1. Add New Recipe")
        print("2. List Recipes")
        print("3. Search Recipe")
        print("4. Delete Recipe")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_recipe()
        elif choice == '2':
            list_recipes()
        elif choice == '3':
            search_recipe()
        elif choice == '4':
            delete_recipe()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
