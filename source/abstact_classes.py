from abc import ABC, abstractmethod

from source.models import Building


class ComparableSorterAbstractClass(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def sort_by_height(self, buildings_list: list[Building]) -> None:
        """Sort an array of buildings by its height
        :param: buildings_list: List of buildings to sort
        :returns: None
        """
        pass

    @abstractmethod
    def sort_by_volume(self, buildings_list: list[Building]) -> None:
        """Sort an array of buildings by its volume
        :param: buildings_list: List of buildings to sort
        :returns: None
        """
        pass
