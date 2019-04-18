"""
ver 0.2

Uses a bit different algorithm then the one, given in example,

It relies more on wall-wide horizontal blocks (the task description did not
mention any sanity restrictions, so we assume that the wall can have a
wall-wide blocks)

i.e: original algorithm would split [4, 4, 2, 3, 1, 5] wall into 5 blocks
    - 2x4, 2x2. 1x1, 2x1, 1x4

    the given one would provide
    -6x1, 4x1, 2x2, 1x1, 1x4

    Note: blocks are represented as `length x height`

On small walls it seems as efficient as the one given in the example

Caution: Block calculations takes some time!!


- author note: I hope efficient algorithm didn't meant to be efficient in
               terms of speed

TODO: Increase algorithm's efficiency
"""

from random import randint


class Wall:
    """
    Wall class, to wrap Wall-dependant methods,

    such as:
        -generation (from given arrays or randomly)
        -minimum block_computation
    """
    def __init__(self, heights=None, **kwargs):
        """
        Create a wall

        Note: if no arguments were provided, the wall will be generated
              automatically

        :param heights: list of wall's max heights for every given meter
                        `H[]` From original task
        :param **kwargs: used for backward compatibility, previous version
                         specified length, which was unnecessary
        """
        if heights is None:
            self._generate()
        else:
            self.heights = heights
            self.length = len(heights)

        self.working_h_list = None

    def _generate(self):
        """
        Generates the wall of [1..100,000] meters long
        and with [1..1,000,000,000] heights on each meter
        """
        self.length = randint(1, 1000000)
        self.heights = [randint(1, 1000000000) for _ in range(self.length)]

    @staticmethod
    def split_sequence(seq):
        """
        Splits list of given integers into sequences
        :param seq:
        :return:
        """
        group = []
        for index, num in enumerate(seq):
            if num:
                group.append(num)
            if (group and not num) or index == len(seq) - 1:
                yield list(group)
                group = []

    def calculate_blocks(self, wall_sequence=None):
        """
        Representation of `int solution(args)` from original task.

        Step 1: get min value for all blocks off the wall sequence
                (that can be subtracted from every meter, thus making
                 us count it as a block, incrementing block count by 1)

        Note: if min value is 0, proceed to step 2!! Do not increment
              block count! Block cannot have 0 meters height!

        Step 2: If there are still uncovered meters left in the wall
                sequence, split the wall into sub_sequences and apply this
                method to every sub_sequence.

        Note: sub_sequence can be calculated either by

        Step 3: If there are no more meters to cover with blocks
                (all values of the wall_sequence are zero, or rather
                no positive integers left) return accumulated
                block count

        :param wall_sequence: a list of wall heights
        :return: minimum block count that can be used to build a given
                 wall sequence
        """
        block_count = 0

        # Pass all the wall as a wall sequence at start
        if wall_sequence is None:
            wall_sequence = [height for height in self.heights]

        # Step 1:
        min_height = min(wall_sequence)
        if min_height:
            block_count += 1

        wall_sub_sequence = [h-min_height for h in wall_sequence]

        # Step 2:
        if sum(wall_sub_sequence):
            # Get wall sub_sequences
            sub_sequences = list(self.split_sequence(wall_sub_sequence))

            for seq in sub_sequences:
                block_count += self.calculate_blocks(seq)

        # Step 3:
        return block_count


if __name__ == '__main__':
    the_wall = Wall(heights=[8, 8, 5, 8, 5, 7, 9, 8, 7, 4, 8], length=11)
    print(the_wall.heights)
    print(the_wall.calculate_blocks())

    the_wall = Wall()
    print(the_wall.calculate_blocks())
