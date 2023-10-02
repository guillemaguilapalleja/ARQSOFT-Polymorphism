class Building:
    def __init__(self, volume_cube_meters: int, height_meters: int):
        self.volume_cube_meters = volume_cube_meters
        self.height_meters = height_meters

    def __repr__(self):
        return f'{self.volume_cube_meters}'
