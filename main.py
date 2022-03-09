
if __name__ == '__name__':

 def id_func():
    while True:
        id_str = input("Employee ID")
    if id_str.isdigit():
        id_int = int(id_str)
    else:
        print("Add numbers")



 def first_name_func():
    while True:
        name = input("name")
    if len(name.strip()) > 2:
            break
    return name

 def last_name_func():
    while True:
        l_name = input("last name")
    if len(l_name.strip()) > 2:
            break
    return l_name
 def birth_year_func():
    while True:
        birth_year_str = (input("birth year"))
    if birth_year_str.isdigit():
        birth_year = int(birth_year_str)
    if (birth_year >= 1900) and (birth_year <= 2004):
            break
    else:
        print("Years ranging from 1990-2004")
    return birth_year

 def birth_month_func():
    while True:
        birth_month_str = (input("birth month"))
    if birth_month_str.isdigit():
        birth_month = int(birth_month_str)
    if (birth_month >= 1) and (birth_month <= 12):
        print("Please enter as a number")


 def bday_func():
    while True:
        bday_str = (input("birth Day"))
    if bday_str.isdigit():
        bday = int(bday_str)
    if (bday >= 1) and (bday <= 31):
        break
    return bday
else:
    print("Please enter as a number")


 def position_func():
    while True:
        position_str = input("Position")
    if len(position_str.strip()) > 0:
            position = str(position_str)


 def graduate_func():
    answers =["yes","no","Yes","No"]
    while True:
        graduate_str = input("Have you attended univerisity ? ")
    if graduate_str in answers:
        return graduate_str
    else:
        print("Please answer 'Yes' or 'No'")



 def add_employee():

    first_name = first_name_func()
    last_name = last_name_func()
    bday = bday_func()
    birth_month = birth_month_func()
    birth_year = birth_year_func()
    ids = id_func()
    pos = position_func()
    grad = graduate_func()

    employee = {
        "ID": ids,
        "First name": first_name,
        "Last name": last_name,
        "Birth Year": birth_year,
        "Birth Month": birth_month,
        "Birth Day": bday,
        "Position": pos,
        "Univeristy": grad
    }
    return employee
def remove_employee():
    first_name = first_name_func()
    last_name = last_name_func()
    bday = bday_func()
    birth_month = birth_month_func()
    birth_year = birth_year_func()
    ids = id_func()
    pos = position_func()
    grad = graduate_func()

