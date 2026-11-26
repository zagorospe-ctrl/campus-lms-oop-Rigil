from abc import ABC, abstractmethod

class AcademicTask(ABC):
    def __init__(self, title, max_points):
        self.title = title
        self.max_points = max_points
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
