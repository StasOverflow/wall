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

        self.working_h_list = None

    def _generate(self):
        """
        Generates the wall of [1..100,000] meters long
        and with [1..1,000,000,000] heights on each meter
        """
        self.length = randint(1, 1000000)
        self.heights = [randint(1, 1000000000) for _ in range(self.length)]

    def _get_block_start_end_index(self, start_index, wall_seq):
        start = start_index
        # if len(wall_seq) > 1:
        #     end = start + 1
        # else:
        end = start_index
            # return start, end

        compare_value = wall_seq[start_index]
        for sub_ind, value in enumerate(wall_seq[1:]):
            if compare_value <= value:
                end = sub_ind
            else:
                break
        return start, end

    def calculate_blocks(self, wall_seq=None):
        block_count = 0
        if wall_seq is None:
            self.working_h_list = [height for height in self.heights]
            wall_seq = self.working_h_list

        print(wall_seq)
        for index, height in enumerate(wall_seq):
            if height:
                start, end = self._get_block_start_end_index(index, wall_seq)
                # print(wall_seq)
                print(start, end)
                if start != end:
                    sub_list = list()
                    for ind, val in enumerate(wall_seq[start:end+1]):
                        wall_seq[ind] = 0
                        sub_list.append(val)

                    if sub_list:
                        min_value = min(sub_list)
                        sub_list = [h - min_value for h in sub_list]
                        # print(sub_list)
                        block_count += self.calculate_blocks(sub_list)
                block_count += 1

        return block_count


if __name__ == '__main__':
    the_wall = Wall(heights=[8, 8, 5, 7, 9, 8, 7, 4, 8], length=9)
    print(the_wall.heights)
    print(the_wall.calculate_blocks())

    # the_wall = Wall(heights=[5, 5, 8, 4], length=4)
    # print(the_wall.calculate_blocks())

    # the_wall = Wall(heights=[8], length=1)
    # print(the_wall.calculate_blocks())
