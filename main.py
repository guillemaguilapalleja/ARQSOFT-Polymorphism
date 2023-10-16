from source.SortingAlgorithms.ComparatorBubbleSorter import ComparatorBubbleSorter
from source.SortingAlgorithms.ComparatorDirInsertSorter import ComparatorDirInsertSorter
from source.models import Building
from random import randint


def main() -> None:
    building1: Building = Building(volume_cube_meters=randint(10, 20), height_meters=randint(1, 5))
    building2: Building = Building(volume_cube_meters=randint(1, 8), height_meters=randint(6, 9))
    building3: Building = Building(volume_cube_meters=randint(100, 200), height_meters=randint(1, 3))

    buildings_list: list[Building] = [building1, building2, building3]
    copy_buildings_list: list[Building] = buildings_list.copy()

    bubble_sorter = ComparatorBubbleSorter()
    dir_insert_sorter = ComparatorDirInsertSorter()

    print("List before sorting:", buildings_list)

    bubble_sorter.sort_by_height(buildings_list)
    dir_insert_sorter.sort_by_height(copy_buildings_list)

    print("List after sorting with Bubble sorter:", buildings_list)
    print("List after sorting with Dir Insert sorter:", copy_buildings_list)


if __name__ == '__main__':
    main()
