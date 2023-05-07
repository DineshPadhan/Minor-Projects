# "accept_list_of_employee_salary(0-1000)_give_10%_hike_to_those_employee_whose_salary(0-500)_give_20%_hike_whose_salry(501-1000)_find_total_salary(0-500)_and_find_total_salary(501-1000)_and_find_total_salary_of_all_employee"
import functools
# input salary
print("Enter Salary with in 0-1000 with space: ")
sal=[int(val) for val in input().split()]
print("Orginal Salary List is {}".format(sal))
# filter salary
zf = list(filter(lambda x:x>0 and x<=500,sal))
ft = list(filter(lambda x:x>500 and x<=1000,sal))
# hike the salary accordingly
hikezf = list(map(lambda x:x+x*(10/100),zf))
hikeft = list(map(lambda x:x+x*(20/100),ft))

print("Hike salary of 0 - 500 salary employee is: {}".format(hikezf))
print("Hike salary of 500 - 1000 salary employee is: {}".format(hikeft))

# sum hike salary accordingly
zfsum = functools.reduce(lambda x,y:x+y,hikezf)
ftsum = functools.reduce(lambda x,y:x+y,hikeft)

total_sal = zfsum+ftsum

print("Total salary of 0-500 employee is: {}".format(zfsum))
print("Total salary of 500-1000 employee is: {}".format(ftsum))
print("Total salary of employee is: {}".format(total_sal))