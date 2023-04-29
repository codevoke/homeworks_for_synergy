```python
from multipledispatch import dispatch


class Student:
    def __init__(self, full_name: str, group_number: int, progress: List[int]) -> None:
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def __lt__(self, student):
        return self.full_name < student.full_name

    
s1 = Student("Petya", 1, [5, 4, 5])
s2 = Student("Anya", 2, [3, 4, 5])
s3 = Student("Vasya", 1, [3, 4, 3])
_list_ = [s1, s2, s3]
for _ in _list_:
    print(_.full_name)

_list_.sort()
for _ in _list_:
    print(_.full_name)

for student in _list_:
    for mark in student.progress:
        if mark == 2 or mark == 3:
            print(student.full_name)
            break
```
[Назад](../../readme.md)