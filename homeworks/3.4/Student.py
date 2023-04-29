from typing import List


class Student:
    def __init__(self, full_name: str, group_number: int, progress: List[int]) -> None:
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def __lt__(self, student: __class__):
        return self.full_name < student.full_name
