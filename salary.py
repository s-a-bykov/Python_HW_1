# Count_Salary
from sys import argv


def count():
    try:
        job_hours, rate_hour, prize = map(float, argv [1:])
        print(f'Зарплата сотрудника - {job_hours * rate_hour + prize}')
    except (ValueError, TypeError):
        print("Введите через пробел - Выработку в часах - Ставку в часах - Премию")


count()