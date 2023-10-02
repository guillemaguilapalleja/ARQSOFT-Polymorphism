from ..abstact_classes import ComparableSorterAbstractClass
from ..models import Building


class ComparatorDirInsertSorter(ComparableSorterAbstractClass):
    def __init__(self):
        super().__init__()

    def sort_by_height(self, buildings_list: list[Building]) -> None:
        for index in range(1, len(buildings_list)):
            current_value = buildings_list[index].height_meters
            position = index

            while position > 0 and buildings_list[position - 1].height_meters > current_value:
                buildings_list[position] = buildings_list[position - 1]
                position -= 1

            buildings_list[position].height_meters = current_value

    def sort_by_volume(self, buildings_list: list[Building]) -> None:
        for index in range(1, len(buildings_list)):
            current_value = buildings_list[index].volume_cube_meters
            position = index

            while position > 0 and buildings_list[position - 1].volume_cube_meters > current_value:
                buildings_list[position] = buildings_list[position - 1]
                position -= 1

            buildings_list[position].volume_cube_meters = current_value
