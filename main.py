from datetime import date
from application import salary
from application.db import people
from app import app

if __name__ == '__main__':
    today = date.today()
    print("Today's date:", today)

    salary.calculate_salary()
    people.get_employees()

    app.run(debug=True)