import random
tiles = [1, 2, 3, 4, 5, 6, 7, 8, 0]
random.shuffle(tiles)
random_list = tiles
tile_map = [tiles[:3], tiles[3:6], tiles[6:9]]
tile_to_move = 0
blank_coords = [0], [0]
tile_coords = [0], [0]


def find_index(nested_list, item):
    for i, sublist in enumerate(nested_list):
        if item in sublist:
            return (i, sublist.index(item))
    return None


while tile_map != [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
    print(str(tile_map[0]) + "\n" +
          str(tile_map[1]) + "\n" +
          str(tile_map[2]))
    tile_to_move = int(input("enter the tile you want to move: "))
    blank_coords = find_index(tile_map, 0)
    tile_coords = find_index(tile_map, tile_to_move)
    if tile_coords is None:
        print("Error: This tile does not exist.")
        continue
    if abs(blank_coords[0] - tile_coords[0]) + abs(blank_coords[1] - tile_coords[1]) != 1:
        print("Error: Invalid move.")
        continue
    tile_map[blank_coords[0]][blank_coords[1]] = tile_to_move
    tile_map[tile_coords[0]][tile_coords[1]] = 0
print("You won!")
