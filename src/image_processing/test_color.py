import extract_color
from PIL import Image
import unittest

class TestGetColorName(unittest.TestCase):

    def test_black_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/black.png')),'black')

    def test_blue_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/blue.png')),'blue')

    def test_brown_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/brown.png')),'brown')

    def test_green_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/green.png')),'green')

    def test_grey_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/grey.png')),'grey')

    def test_orange_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/orange.png')),'orange')

    def test_pink_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/pink.png')),'pink')

    def test_purple_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/purple.png')),'purple')

    def test_red_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/red.png')),'red')

    def test_white_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/white.jpg')),'white')

    def test_yellow_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/yellow.png')),'yellow')

    def test_cyan_color(self):
        self.assertEqual(extract_color.get_color_name(Image.open('./test_imagedata/cyan.png')),'cyan')

class TestGetDominantColor(unittest.TestCase):
    def test_zeroA(self):
        dominant_color = extract_color.get_dominant_color(Image.open('./test_imagedata/transparent.png'))
        self.assertTrue(dominant_color == 0)
    def test_multicolor(self):
        dominant_color = extract_color.get_dominant_color(Image.open('./test_imagedata/multicolor.png'))
        self.assertTrue(dominant_color == (250,7,7))

class TestRGB2HSV(unittest.TestCase):
    def testMXequalsMN(self):
        h, s, v = extract_color.rgb2hsv(255,255,255)
        self.assertTrue((h,s,v) == (0,0.0,1.0))
    def testMXequalsR(self):
        h, s, v = extract_color.rgb2hsv(255,0,0)
        self.assertTrue((h,s,v) == (0.0,1.0,1.0))
    def testMXequalsG(self):
        h, s, v = extract_color.rgb2hsv(0,255,0)
        self.assertTrue((h,s,v) == (120.0,1.0,1.0))
    def testMXequalsB(self):
        h, s, v = extract_color.rgb2hsv(0,0,255)
        self.assertTrue((h,s,v) == (240.0,1.0,1.0))
    def testMXequals0(self):
        h, s, v = extract_color.rgb2hsv(0,0,0)
        self.assertTrue((h,s,v) == (0,0,0.0))

if __name__ == '__main__':
    unittest.main()
