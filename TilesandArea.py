def calculate_tiles_and_area(room_length, room_width, tile_length, tile_width):
    # Calculate the area of the room and the tile
    room_area = room_length * room_width
    tile_area = tile_length * tile_width
    
    # Calculate the number of tiles required
    num_tiles_length = room_length / tile_length
    num_tiles_width = room_width / tile_width
    
    # Round up the number of tiles required in each dimension
    import math
    total_tiles = math.ceil(num_tiles_length) * math.ceil(num_tiles_width)
    
    # Calculate the area covered by the tiles
    covered_area = total_tiles * tile_area
    
    return total_tiles, covered_area

# Example usage
room_length = 10  # Length of the room in meters
room_width = 8    # Width of the room in meters
tile_length = 0.5 # Length of one tile in meters
tile_width = 0.5  # Width of one tile in meters

total_tiles, covered_area = calculate_tiles_and_area(room_length, room_width, tile_length, tile_width)
print(f"Total number of tiles needed: {total_tiles}")
print(f"Total area covered by tiles: {covered_area} square meters")
