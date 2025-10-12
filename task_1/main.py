from pathlib import Path
from get_salary_num import get_salary_number
def total_salary(path: str) -> tuple:
    try:
        with open(path,"r", encoding="utf-8") as file:
            salaries = file.readlines()
            numbers_only = get_salary_number(salaries)
            sum_salary = int(sum(numbers_only))
            avg_salary = float(sum_salary/len(numbers_only))
            return f"General salary sum is {sum_salary}.\nAverage salary is {avg_salary:.2f}."
                
    
    except FileNotFoundError:
        return "File is not found :("

print(total_salary(r"C:\goit\repositories\goit-algo-hw-04\task_1\salaries.txt"))        
