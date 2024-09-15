import random
tiles = [1, 2, 3, 4, 5, 6, 7, 8, 0]
tile_map = []


def Randomize_map(tiles):
    random.shuffle(tiles)
    tile_map = [tiles[:3], tiles[3:6], tiles[6:9]]
    Check_solvable(tiles)
    return tile_map


def Check_solvable(tiles):
    inversions = 0
    for num in tiles:
        if num == 0:
            continue
        for num2 in tiles:
            if num2 == num or num2 == 0:
                continue
            if num2 < num:
                inversions += 1
    if inversions % 2 != 0:
        Randomize_map(tiles)


tile_map = Randomize_map(tiles)
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
    try:
        tile_to_move = int(input("enter the tile you want to move: "))
    except ValueError:
        print("Error: Not an integer")
        continue
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
