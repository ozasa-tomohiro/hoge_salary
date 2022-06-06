def cal_salary(salary):
    tax = 0
    if salary > 100:
        tax += (salary - 100) * 0.2
        tax += 100 * 0.1
    else:
        tax += salary * 0.1

    get_salary = int(salary - tax)
    tax_salary = int(tax)

    return get_salary, tax_salary
