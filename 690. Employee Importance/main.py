
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


def getImportance(employees, id):
    """
    :type employees: Employee
    :type id: int
    :rtype: int
    """
    for employee in employees:
        if (employee.id == id):
            if (len(employee.subordinates) == 0):
                return employee.importance
            else:
                return (employee.importance + sum(getImportance(employees, subid) for subid in employee.subordinates))
