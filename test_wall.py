from wall import *


def test_wall_sane_algorithm():
    heights = [8, 8]
    wall = Wall(heights, len(heights))
    assert wall.calculate_blocks() is 1

    heights = [0, 8, 8, 8]
    wall = Wall(heights, len(heights))
    assert wall.calculate_blocks() is 1

    heights = [8, 8, 1, 8]
    wall = Wall(heights, len(heights))
    assert wall.calculate_blocks() is 3

    heights = [0, 8, 0, 8]
    wall = Wall(heights, len(heights))
    assert wall.calculate_blocks() is 2


def test_wall_right_calculations():
    heights = [4, 1, 2, 3, 2, 4, 1]
    wall = Wall(heights, len(heights))
    assert wall.calculate_blocks() is 5


def test_wall_builder_uses_efficient_algorithm():
    """
    Though implemented algorithm uses a bit different block orientation
    then the one in example, it still counts as efficient.
    """
    heights = [8, 8, 5, 7, 9, 8, 7, 4, 8]
    wall = Wall(heights, len(heights))
    assert wall.calculate_blocks() is 7

    # A bit more complicated example, that caused trouble in ver 0.1
    heights = [8, 8, 5, 8, 5, 7, 9, 8, 7, 4, 8]
    wall = Wall(heights, len(heights))
    assert wall.calculate_blocks() is 8
