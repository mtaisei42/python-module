import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        usr_input = input("Enter new coordinates as floats in format 'x,y,z':")
        coord_list = usr_input.split(',')
        if len(coord_list) != 3:
            print("Invalid syntax")
            continue
        try:
            nbr = coord_list[0].strip()
            x = float(nbr)
            nbr = coord_list[1].strip()
            y = float(nbr)
            nbr = coord_list[2].strip()
            z = float(nbr)
            return (x, y, z)
        except ValueError as e:
            print(f"Error on parameter '{nbr}' : {e}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coord_tuple1 = get_player_pos()
    print(f"Got a first tuple: {coord_tuple1}")
    x1 = coord_tuple1[0]
    y1 = coord_tuple1[1]
    z1 = coord_tuple1[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    center_dist = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(center_dist, 4)}")

    print("\nGet a second set of coordinates")
    coord_tuple2 = get_player_pos()
    x2 = coord_tuple2[0]
    y2 = coord_tuple2[1]
    z2 = coord_tuple2[2]
    dist_between_p1_p2 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1))
    print(f"Distance between the 2 sets of coordinates: "
          f" {round(dist_between_p1_p2, 4)}")

if __name__ == "__main__":
    main()
