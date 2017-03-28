# =============================================================================
# Author: Azizou Ogbone
# File: test_get_graph.py
# Description: Unit test for the get_graph function in the module graph.py
# Date: March 28, 2017
# Version: 1.0
# =============================================================================

import unittest # Provide useful methods like assertEqual for unit-testing 
import graph # The module containing the method to be tested


class TestGraphMethod(unittest.TestCase):

	def test_get_graph(self):
		fx = 'x + 2'
		expected_result = "          |       o  "\
						+ "          |      o   "\
						+ "          |     o    "\
						+ "          |    o     "\
						+ "          |   o      "\
						+ "          |  o       "\
						+ "          | o        "\
						+ "          |o         "\
						+ "          o          "\
						+ "         o|          "\
						+ "--------o-+----------"\
						+ "       o  |          "\
						+ "      o   |          "\
						+ "     o    |          "\
						+ "    o     |          "\
						+ "   o      |          "\
						+ "  o       |          "\
						+ " o        |          "\
						+ "o         |          "\
						+ "          |          "\
						+ "          |          \n"
		self.assertEqual(expected_result,graph.get_graph(20,fx),"Same graph should be produced")
		self.assertNotEqual(expected_result,graph.get_graph(30,fx),"Same graph should be produced")

if __name__ == '__main__':
    unittest.main()