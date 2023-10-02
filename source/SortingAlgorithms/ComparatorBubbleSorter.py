from ..abstact_classes import ComparableSorterAbstractClass
from ..models import Building


class ComparatorBubbleSorter(ComparableSorterAbstractClass):
    def __init__(self):
        super().__init__()

    def sort_by_height(self, buildings_list: list[Building]) -> None:
        n = len(buildings_list)
        swapped = False
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if buildings_list[j].height_meters > buildings_list[j + 1].height_meters:
                    swapped = True
                    buildings_list[j].height_meters, buildings_list[j + 1].height_meters = buildings_list[j + 1].height_meters, buildings_list[j].height_meters
            if not swapped:
                return

    def sort_by_volume(self, buildings_list: list[Building]) -> None:
        n = len(buildings_list)
        swapped = False
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if buildings_list[j].volume_cube_meters > buildings_list[j + 1].volume_cube_meters:
                    swapped = True
                    buildings_list[j].volume_cube_meters, buildings_list[j + 1].volume_cube_meters = buildings_list[j + 1].volume_cube_meters, buildings_list[j].volume_cube_meters
            if not swapped:
                return


