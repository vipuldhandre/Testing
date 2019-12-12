import unittest

class TestCase1(unittest.TestCase):

    def setUp(self):
        print("TestCase1: setUp")

    def test1(self):
        print("TestCase1:test1")

    def test2(self):
        print("TestCase1:test2")

    def test3(self):
        print("TestCase1:test3")

    def tearDown(self):
        print("TestCase1: tearDown")


        
        
