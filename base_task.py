from abc import ABC, abstractmethod

class AcademicTask:
    def __init__(self, title, max_points, is_graded):
        self.title = title
        self.max_points = 0
        self.is_graded = False

    @abstractmethod
    def submit_work(self):
        pass

    @abstractmethod
    def grade_work(self):
        pass

    @abstractmethod
    def get_details(self):  
        pass
