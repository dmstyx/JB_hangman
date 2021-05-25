import sqlite3

conn = sqlite3.connect("food_blog.db")
cur = conn.cursor()

cur.execute("PRAGMA foreign_keys = ON;")

cur.execute("""CREATE TABLE 
    IF NOT EXISTS 
    meals(meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_name VARCHAR(20) NOT NULL)""")

cur.execute("""CREATE TABLE 
    IF NOT EXISTS 
    ingredients(ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name VARCHAR(20) NOT NULL),
    FOREIGN KEY(measure_id) REFERENCES measures(measure_id),
    FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id),
    FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id)
    """)

cur.execute("""CREATE TABLE 
    IF NOT EXISTS
    measures(measure_id INTEGER PRIMARY KEY AUTOINCREMENT,
    measure_name VARCHAR(20) NOT NULL,
    FOREIGN KEY(measure_id) REFERENCES measures(measure_id),
    FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id),
    FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id))
    """)

cur.execute("""CREATE TABLE 
    IF NOT EXISTS 
    recipes(recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_name VARCHAR(20) NOT NULL,
    recipe_description VARCHAR(40),
    FOREIGN KEY(measure_id) REFERENCES measures(measure_id),
    FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id),
    FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id))
    """)

cur.execute("""CREATE TABLE 
    IF NOT EXISTS 
    serve(serve_id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER NOT NULL,
    meal_id INTEGER NOT NULL,
    FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id),
    FOREIGN KEY(meal_id) REFERENCES meals(meal_id))
    """)

cur.execute("""CREATE TABLE 
    IF NOT EXISTS 
    quantity(quantity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    measure_id INTEGER NOT NULL ,
    ingredient_id INTEGER NOT NULL ,
    quantity INTEGER NOT NULL ,
    recipe_id INTEGER NOT NULL)
    """)


conn.commit()

data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}


class RecepieDatabase:

    def __init__(self):
        self.data = data

    def add_data_to_db(self):

        for meal in [i for i in data['meals']]:
            cur.execute("INSERT INTO meals (meal_name) VALUES (?)", (meal,))
            conn.commit()

        for ingredient in [i for i in data['ingredients']]:
            cur.execute("INSERT INTO ingredients (ingredient_name) VALUES(?)", (ingredient,))
            conn.commit()

        for measure in [i for i in data['measures']]:
            cur.execute("INSERT INTO measures (measure_name) VALUES(?)", (measure,))
            conn.commit()

    def add_recipes(self):
        print("Pass the empty recipe name to exit.")
        while True:
            recipe = input("Recipe name:")
            if recipe == "":
                break
            else:
                description = input("Recipe description:")
                cur.execute("INSERT INTO recipes (recipe_name, recipe_description) VALUES (?, ?)", (recipe, description))
                conn.commit()

                self.get_all_db(recipe)

    def get_all_db(self, recipe):
        cur.execute('SELECT * FROM meals')
        print(cur.fetchall())
        cur.execute(f'SELECT recipe_id FROM recipes WHERE recipe_name = "{recipe}"')
        self.serve(cur.fetchone()[0])

    def serve(self, recipe_id):
        serve_times = input("When the dish can be served: ").split()
        for item in serve_times:
            item = int(item)
            if item == 1:
                cur.execute("INSERT INTO serve (recipe_id, meal_id) VALUES(?, ?)", (recipe_id, item))
                conn.commit()
            if item == 2:
                cur.execute("INSERT INTO serve (recipe_id, meal_id) VALUES(?, ?)", (recipe_id, item))
                conn.commit()
            if item == 3:
                cur.execute("INSERT INTO serve (recipe_id, meal_id) VALUES(?, ?)", (recipe_id, item))
                conn.commit()
            if item == 4:
                cur.execute("INSERT INTO serve (recipe_id, meal_id) VALUES(?, ?)", (recipe_id, item))
                conn.commit()

        self.enter_ingredients()
    
    def enter_ingredients(self):
        while True:
            food = input("Input quantity of ingredient <press enter to stop> ").split()
            if food == []:
                break
            else:
                print(food[0], food[1], food[2])

            



def main():
    RecepieDatabase.add_data_to_db(data)
    run = RecepieDatabase()
    run.add_recipes()
    # run.serve()


if __name__ == "__main__":
    main()
