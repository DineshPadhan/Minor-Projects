# emp no only positive
# salary must be positive
# if bs grater than 10000 then give da = 20% bs & ta = 15% bs &

emp_no = int(input("Enter employee number: "))
basic_salary = float(input("Enter basic salary: "))

if emp_no <= 0:
    print("Employee number must be positive.")
elif basic_salary <= 0:
    print("Basic salary must be positive.")
else:
    if basic_salary > 10000:
        da = 0.2 * basic_salary
        ta = 0.15 * basic_salary
    else:
        da = 0
        ta = 0

    gross_salary = basic_salary + da + ta
    print("Gross salary:", gross_salary)
