import dynamic_crawler
import image_database
import unittest

class TestDynamicCrawler(unittest.TestCase):
    def test_null(self):
        self.assertEqual(dynamic_crawler.dynamic_crawler([], 0), None)

    def test_tag_1(self):
        self.assertEqual(len(dynamic_crawler.dynamic_crawler(['chair', 'sitting', 'man'], 1)[0]), 1)

    def test_tag_2(self):
        self.assertEqual(len(dynamic_crawler.dynamic_crawler(['running', 'dog'], 5)[0]), 5)

    def test_tag_3(self):
        self.assertEqual(len(dynamic_crawler.dynamic_crawler(['blue', 'cat'], 12)[0]), 12)

class TestOnlyColorInTags(unittest.TestCase):
    def test_object_1(self):
        self.assertTrue(image_database.onlyColorInTags(object = {'name':'apple', 'tags': ['green'], 'number':2}) == 1)

    def test_object_2(self):
        self.assertTrue(image_database.onlyColorInTags(object = {'name': None,'tags': ['cyan'], 'number': None}) == 1)

    def test_object_3(self):
        self.assertTrue(image_database.onlyColorInTags(object = {'name':'apple', 'tags': [], 'number':2}) == 0)

    def test_object_4(self):
        self.assertTrue(image_database.onlyColorInTags(object = {'name':'apple', 'tags': ['banana'], 'number':2}) == 0)

    def test_object_5(self):
        self.assertTrue(image_database.onlyColorInTags(object = {'name':'apple', 'tags': ['green', 'cyan'], 'number':2}) == 1)

    def test_object_6(self):
        self.assertTrue(image_database.onlyColorInTags(object = {'name':'apple', 'tags': ['green', 'cyan', 'beautiful'], 'number':2}) == 0)

class TestnameIndb(unittest.TestCase):
    def test_object_1(self):
        self.assertTrue(image_database.nameIndb(object = {'name':'apple', 'tags': ['green'], 'number':2}) == 1)

    def test_object_2(self):
        self.assertTrue(image_database.nameIndb(object = {'name': None, 'tags': ['green'], 'number':2}) == 0)

    def test_object_4(self):
        self.assertTrue(image_database.nameIndb(object = {'tags': ['green'], 'number':2}) == 0)

class TestGetNewTag(unittest.TestCase):
    def test_object_1(self):
        self.assertEqual(image_database.getNewTag(object = {'name': 'apple', 'tags': ['green'], 'number':2}), ['green','apple'])

    def test_object_2(self):
        self.assertEqual(image_database.getNewTag(object = {'name': 'Lily', 'tags': ['properNoun'], 'number': 1}), [])

    def test_object_3(self):
        self.assertEqual(image_database.getNewTag(object = {'name': 'Lily', 'tags': ['white'], 'number':2}), ['white','Lily'])

    def test_object_4(self):
        self.assertEqual(image_database.getNewTag(object = {'name': 'Lily', 'tags': ['person'], 'number': 1} ), [])

    def test_object_5(self):
        self.assertEqual(image_database.getNewTag(object = {'name': 'Lily', 'tags': ['beautiful', 'properNoun'], 'number': 1}),['beautiful'])

    def test_object_6(self):
        self.assertEqual(image_database.getNewTag(object = {'name': 'Lily', 'tags': ['beautiful', 'person'], 'number': 1}),['beautiful'])

class TestGetColorInTags(unittest.TestCase):
    def test_tag_1(self):
        self.assertEqual(image_database.getColorInTags([]), None)

    def test_tag_2(self):
        self.assertEqual(image_database.getColorInTags(['cyan']), 'cyan')

    def test_tag_3(self):
        self.assertEqual(image_database.getColorInTags(['beautiful']), None)

    def test_tag_4(self):
        self.assertEqual(image_database.getColorInTags(['beautiful', 'green']), 'green')

class TestLinearLayer(unittest.TestCase):
    def test_output_getImage_1(self):
        test_case  = {'name': 'apple', 'tags': [], 'number': 1}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 1)

    def test_output_getImage_2(self):
        test_case  = {'name': 'apple', 'tags': ['green'], 'number': 1}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 1)

    def test_output_getImage_3(self):
        test_case  = {'name': 'apple', 'tags': ['green'], 'number': 10}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 10)

    def test_output_getImage_4(self):
        test_case  = {'name': None, 'tags': ['green'], 'number': 1}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 0)

    def test_output_getImage_5(self):
        test_case  = {'name': 'apple', 'tags': ['green'], 'number': None}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 0)

    def test_output_getImage_6(self):
        test_case  = {'name': 'Prince', 'tags': ['beautiful'], 'number': 1}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 1)

    def test_output_getImage_7(self):
        test_case  = {'name': 'apple', 'tags': ['orange'], 'number': 1}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 1)

    def test_output_getImage_8(self):
        test_case  = {'name': 'apple', 'tags': ['pink'], 'number': 1}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 1)

    def test_output_getImage_9(self):
        test_case  = {'name': 'baby', 'tags': ['cute'], 'number': 1}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 1)

    def test_output_getImage_10(self):
        test_case  = {'name': 'Lily', 'tags': ['properNoun'], 'number': 1}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 0)

    def test_output_getImage_11(self):
        test_case  = {'name': 'apple', 'tags': ['big', 'green'], 'number': 1}
        # predicted result: base64
        self.assertEqual(len(image_database.getImage(test_case)), 1)


if __name__ == "__main__":
    unittest.main()
