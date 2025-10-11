import re

def get_salary_number(salaries: list) -> list[int]:
    pattern = r"\D"
    salary_numbers = []
    for salary in salaries:
        modified = re.sub(pattern, '', salary)
        salary_numbers.append(int(modified))
    return salary_numbers