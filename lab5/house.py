def main():
    x, y = 100, 100
    width, height = 200, 300

    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Function draws a house with width and height from reference point (x, y),
    which is in the bottom middle of the house basement
    :param x: coordinate of the middle of the house
    :param y: coordinate of the bottom of the basement
    :param width: full width of the house with roof
    :param height: full height of the house with roof and basement
    :return: None
    """
    print('Draw house', x, y, width, height)
    foundation_height = 0.05 * height
    walls_height = 0.9 * height
    walls_width = 0.5 * width
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y, foundation_height, walls_width, walls_height)
    draw_house_roof(x, y, foundation_height, walls_height, width, roof_height)

def draw_house_foundation(x, y, width, foundation_height):
   """
    Function draws a house foundation with width and height from reference point (x, y),
    which is in the bottom middle of the house basement
    :param x: coordinate of the middle of the house basement
    :param y: coordinate of the bottom of the basement
    :param width: full width of the house with roof and basement
    :param foundation_height: full height of the basement
    :return: None
   """
   print('Draw foundation', x, y, width, foundation_height)
   pass
def draw_house_walls(x, y, foundation_height, walls_width, walls_height):
    """
    Function draws a house walls with width and height from reference point (x, y),
    which is in the bottom middle of the wall
    :param x: coordinate of the middle of the house wall
    :param y: coordinate of the bottom of the basement wall
    :param width: full width of the house with roof and basement
    :param height: full height of the basement
    :return: None
    """
    print('Draw walls', x, y - foundation_height, walls_width, walls_height)
    pass
def draw_house_roof(x, y, foundation_height, walls_height, width, roof_height):
    """
    Function draws a house roof with width and height from reference point (x, y),
    which is in the bottom middle of the house roof
    :param x: coordinate of the middle of the house roof
    :param y: coordinate of the bottom of the roof
    :param width: full width of the house with roof and basement
    :param height: full height of the whole house
    :return: None
    """
    print('Draw roof', x, y - foundation_height - walls_height, width, roof_height)
    pass

if __name__ == "__main__":
    main()