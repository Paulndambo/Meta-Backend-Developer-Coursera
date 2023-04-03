class Employee:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last


class Supervisor(Employee):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)

        self.password = password


class Chef(Employee):
    def leave_request(self, days):
        return f"May i request a leave for {days} days"


andrian = Supervisor("Andrian Kovalenko", "A", "1234")
print(andrian.password)
emily = Chef("Emily", "E")
print(emily.leave_request(23))