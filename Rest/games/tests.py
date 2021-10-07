from django.test import TestCase

# Create your tests here.


class soma(TestCase):
    def test_soma(self):
        res=1+2
        self.assertEqual(3,res)
    def test_sub(self):
        res=5-1
        self.assertEqual(4, res)
class TestStringMethods(TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)