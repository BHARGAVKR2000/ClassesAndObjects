def marks(total) -> None:
    add = 0
    for item in range(total):
        add += int(input("enter subject :"))


class Student:
    def __init__(self, total):
        self.total = total


if __name__ == "__main__":
    student = Student(6)
    print(marks(5))
