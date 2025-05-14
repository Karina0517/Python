# 1. Library Book Tracker
library = {}

def add_book(title, author, pages):
    library[title] = {"author": author, "pages": pages}

def find_book(title):
    return library.get(title, "Book not found.")

def show_books():
    return list(library.keys())


# 2. Student Grade Manager
grades = {}

def add_student(name):
    grades[name] = []

def add_grade(name, score):
    if name in grades:
        grades[name].append(score)

def get_average(name):
    student_grades = grades.get(name, [])
    return sum(student_grades) / len(student_grades) if student_grades else 0


# 3. Restaurant Menu Editor
menu = {}

def add_dish(name, price, available):
    menu[name] = {"price": price, "available": available}

def change_availability(name, available):
    if name in menu:
        menu[name]["available"] = available

def total_available_price():
    return sum(d["price"] for d in menu.values() if d["available"])


# 4. Warehouse Box Counter
warehouse = {}

def add_box(name, quantity):
    warehouse[name] = quantity

def update_quantity(name, change):
    if name in warehouse:
        warehouse[name] += change

def has_enough(name, needed):
    return warehouse.get(name, 0) >= needed


# 5. Movie Rating System
movies = {}

def add_movie(title):
    movies[title] = []

def rate_movie(title, rating):
    if title in movies:
        movies[title].append(rating)

def average_rating(title):
    ratings = movies.get(title, [])
    return sum(ratings) / len(ratings) if ratings else 0
# 6. Online Course Tracker
courses = {}

def add_course(title, hours, students):
    courses[title] = {"hours": hours, "students": students}

def update_enrollment(title, students):
    if title in courses:
        courses[title]["students"] = students

def filter_by_hours(min_hours):
    return [title for title, data in courses.items() if data["hours"] >= min_hours]


# 7. To-Do List Organizer
todos = {}

def add_task(name, priority):
    todos[name] = {"priority": priority, "status": "pending"}

def complete_task(name):
    if name in todos:
        todos[name]["status"] = "completed"

def filter_tasks(priority=None, status=None):
    return [
        {"name": name, **data}
        for name, data in todos.items()
        if (priority is None or data["priority"] == priority) and
           (status is None or data["status"] == status)
    ]


# 8. Digital Wallet
wallet = {}

def add_expense(category, amount):
    wallet[category] = wallet.get(category, 0) + amount

def total_spent():
    return sum(wallet.values())

def expense_percentages():
    total = total_spent()
    return {cat: (amt / total) * 100 for cat, amt in wallet.items()} if total else {}


# 9. Pet Adoption Center
pets = []

def add_pet(name, species, age):
    pets.append({"name": name, "species": species, "age": age})

def find_by_species(species):
    return [pet for pet in pets if pet["species"] == species]

def older_than(age):
    return [pet for pet in pets if pet["age"] > age]


# 10. Gym Membership System
members = {}

def register_member(name, plan, payment_status):
    members[name] = {"plan": plan, "status": payment_status}

def change_plan(name, new_plan):
    if name in members:
        members[name]["plan"] = new_plan

def unpaid_members():
    return [name for name, data in members.items() if data["status"] == "late"]