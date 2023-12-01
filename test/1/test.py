import os
import unittest

import _1 as solver


def readfile(filename):
    f = open(os.path.dirname(__file__) + '/' + filename, 'r')
    content = f.read()
    f.close()
    return content


class SolverTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(142, solver.part1(readfile('test_input_1')))
        print("Day 1 Part 1 solution: ", solver.part1(readfile('real_input')))

    def test_part2(self):
        self.assertEqual(281, solver.part2(readfile('test_input_2')))
        print("Day 1 Part 2 solution: ", solver.part2(readfile('real_input')))


if __name__ == '__main__':
    unittest.main()
