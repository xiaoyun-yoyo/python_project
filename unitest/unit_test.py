# coding=utf-8
from user_info import get_formatted_name
import unittest

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'janis joplin')

if __name__ == '__main__':
    unittest.main()

# print("Enter 'q' at any time to quit.")
#
# while True:
#     first = input("\n Please give me a first name: ")
#     if first == 'q':
#         break
#     last = input("\n Please give me a last name: ")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first, last)
#     print(f"\t Neatly formatted name: {formatted_name}")