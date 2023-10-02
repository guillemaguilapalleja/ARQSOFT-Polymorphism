from source.SortingAlgorithms.ComparatorBubbleSorter import ComparatorBubbleSorter
from source.SortingAlgorithms.ComparatorDirInsertSorter import ComparatorDirInsertSorter
from source.models import Building
from random import randint

if __name__ == '__main__':

    building1: Building = Building(volume_cube_meters=randint(10, 20), height_meters=randint(1, 5))
    building2: Building = Building(volume_cube_meters=randint(1, 8), height_meters=randint(6, 9))
    building3: Building = Building(volume_cube_meters=randint(100, 200), height_meters=randint(1, 3))

    buildings_list: list[Building] = [building1, building2, building3]
    print(building1.volume_cube_meters, building2.volume_cube_meters)

    bubble_sorter = ComparatorBubbleSorter()
    dir_insert_sorter = ComparatorDirInsertSorter()

    dir_insert_sorter.sort_by_volume(buildings_list)

    print(buildings_list)

