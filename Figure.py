from abc import ABC, abstractmethod


class Figure(ABC):
    
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Аргументом должна быть фигура. Проверьте данные")
        return self.get_area + other_figure.get_area