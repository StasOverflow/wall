from random import randint


class Wall:
    """
    Wall class, to wrap Wall-dependant methods,

    such as:
        -generation (from given arrays or randomly)
        -minimum block_computation
    """
    def __init__(self, heights=None, length=None):

        if heights is None or length is None:
            self._generate()
        else:
            assert len(heights) == length
            self.heights = heights
            self.length = length

    def _generate(self):
        """
        Generates the wall of [1..100,000] meters long
        and with [1..1,000,000,000] heights on each meter
        """
        self.length = randint(1, 1000000)
        self.heights = [randint(1, 1000000000) for _ in range(self.length)]

    def calculate_block(self, height):
        block_height = 0
        block_width = 0
        return block_height, block_width


    def min_blocks_required(self):
        """
        Represents `int solution(int H[], int N);`,
        where H is self.heights attribute class
        and   N is self.length attribute class

        :return: minimum number of blocks required to build the wall
        """
        block_count = 0
        meters_covered = 0

        height_list = [height for height in self.heights]
        while meters_covered < self.length:
            start_index = 0
            start_height = height_list[start_index]
            end_index = 1
            while height_list[start_index] <= height_list[end_index]:
                end_index += 1
                print(end_index)
            for index, height in enumerate(height_list[:end_index]):
                height_list[index] = height - start_height
            height_list = [h for h in height_list if h is not 0]
            meters_covered = self.length - len(height_list)
            print('list is {0}\n, '
                  'meters covered: {1}'.format(height_list, meters_covered))

        minimal = min(height_list)
        # height_list = [height-minimal for height in self.heights]
        return block_count


if __name__ == '__main__':
    the_wall = Wall(heights=[8, 8, 5, 7, 9, 8, 7, 4, 8], length=9)
    the_wall.min_blocks_required()
    # print(the_wall.heights)
