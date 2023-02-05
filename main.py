from datetime import date
from application import salary
from application.db import people

if __name__ == '__main__':
    today = date.today()
    print("Today's date:", today)

    salary.calculate_salary()
    people.get_employees()
    