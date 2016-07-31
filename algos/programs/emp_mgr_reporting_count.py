'''
http://www.geeksforgeeks.org/find-number-of-employees-under-every-manager/
Find number of Employees Under every Employee
Given a dictionary that contains mapping of employee and his manager as a number of (employee, manager) pairs like below.

{ "A", "C" },
{ "B", "C" },
{ "C", "F" },
{ "D", "E" },
{ "E", "F" },
{ "F", "F" }

In this example C is manager of A,
C is also manager of B, F is manager
of C and so on.
'''


def create_mgr_emp_map(emp_mgr_map):
    mgr_emplist_map = {}
    for emp in emp_mgr_map:
        mgr = emp_mgr_map[emp]

        # exclude emp-emp entry
        if mgr == emp:
            continue

        emp_list = mgr_emplist_map.get(mgr)
        if emp_list is None:
            emp_list = [emp]
        else:
            emp_list.append(emp)

        mgr_emplist_map[mgr] = emp_list

    return mgr_emplist_map


def populate_result_map(mgr, mgr_emplist_map):
    # for employees with no reporters
    if mgr_emplist_map.get(mgr) is None:
        result_map[mgr] = 0
        return 0
    # avoid recomputation
    elif mgr in result_map:
        count = result_map[mgr]
    # recursively clauclate
    else:
        emp_list = mgr_emplist_map[mgr]
        count = len(emp_list)
        for emp in emp_list:
            count += populate_result_map(emp, mgr_emplist_map)
        result_map[mgr] = count
    return count


def calculate_and_print(emp_mgr_map):
    mgr_emplist_map = create_mgr_emp_map(emp_mgr_map)
    for emp in emp_mgr_map:
        populate_result_map(emp, mgr_emplist_map)
    print(result_map)


result_map = {}

if __name__ == '__main__':
    emp_mgr_map = {'A': 'C', 'B': 'C', 'C': 'F', 'D': 'E', 'E': 'F', 'F': 'F'}
    calculate_and_print(emp_mgr_map)
