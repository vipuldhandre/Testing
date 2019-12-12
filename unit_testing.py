##import unittest
##
##
##class TestCaseDemo(unittest.TestCase):
##    
##    def setUp(self):
##        print("set up method execution")
##
##    def test_method1(self):
##        print("Test method execution")
##
##    def tearDown(self):
##        print("Tear down method execution")
##
##
##unittest.main()


##import unittest
##
##class TestCaseDemo(unittest.TestCase):
##
##    def setUp(self):
##        print("Set up method execution")
##
##    def test_method1(self):
##        print("test method 1 execution")
##
##    def test_method2(self):
##        print("test method 2 execution")
##
##    def tearDown(self):
##        print("Tear down method execution")
##
##unittest.main()
        
##import unittest
##
##class TestCaseDemo(unittest.TestCase):
##
##    def setUp(self):
##        print("Set up method execution")
##
##    def test_method1(self):
##        print("test method 1 execution")
##
##    def test_method2(self):
##        print("test method 2 execution")
##
##    def test_method3(self):
##        print("test method 3 execution")
##
##    def tearDown(self):
##        print("Tear down method execution")
##
##unittest.main()


##import unittest
##
##class TestCaseDemo(unittest.TestCase):
##
##    def setUp(self):
##        print("Set up method execution")
##
##    def test_method1(self):
##        print(10/0)
##        print("test method 1 execution")
##        
##    
##
##    def test_method2(self):
##        
##        print("test method 2 execution")
##        
##
##    def test_method3(self):
##        print("test method 3 execution")
##        
##    def tearDown(self):
##        print("Tear down method execution")
##
##unittest.main()


##import unittest
##
##class TestCaseDemo(unittest.TestCase):
##
##    @classmethod
##    def setUpClass(cls):
##        print("Set up class method")
##
##    def setUp(self):
##        print("set up method")
##
##    def test_method1(self):
##        print("test method 1")
##
##    def test_method2(self):
##        print("test method 2")
##
##    def tearDown(self):
##        print("tear down method")
##
##    @classmethod
##    def tearDownClass(cls):
##        print("tear down class method")
##
##
##unittest.main()

##import unittest
##
##class TestCaseDemo(unittest.TestCase):
##
##    @classmethod
##    def setUpClass(cls):
##        print("Set up class method")
##
##    def setUp(self):
##        print("set up method")
##
##    def test_method1(self):
##        print("test method 1")
##        print(10/0)
##
##    def test_method2(self):
##        print("test method 2")
##
##    def tearDown(self):
##        print("tear down method")
##
##    @classmethod
##    def tearDownClass(cls):
##        print("tear down class method")
##
##
##unittest.main()

##import unittest
##
##class TestCaseDemo(unittest.TestCase):
##
##    @classmethod
##    def setUpClass(cls):
##        print("Set up class method")
##
##    def setUp(self):
##        print("set up method")
##
##    def test_method1(self):
##        print(10/0)
##        print("test method 1")
##
##    def test_method2(self):
##        print("test method 2")
##
##    def tearDown(self):
##        print("tear down method")
##
##    @classmethod
##    def tearDownClass(cls):
##        print("tear down class method")
##
##
##unittest.main()

##import unittest
##
##class TestCaseDemo(unittest.TestCase):
##
##    @classmethod
##    def setUpClass(cls):
##        print("Set up class method")
##
##    def setUp(self):
##        print("set up method")
##
##    def test_method1(self):
##        print("test method 1")
##
##    def test_method2(self):
##        print("test method 2")
##
##    def tearDown(self):
##        print("tear down method")
##
##    def test_method3(self):
##        print("test method 3")
##
##    def test_method4(self):
##        print("test method 4")
##
##    @classmethod
##    def tearDownClass(cls):
##        print("tear down class method")
##
##
##unittest.main()

##import unittest
##
##class TestCaseDemo(unittest.TestCase):
##
##    @classmethod
##    def setUpClass(cls):
##        print("Set up class method")
##
##    def setUp(self):
##        print("set up method")
##
##    def test_method1(self):
##        print("test method 1")
##        print(10/0)
##
##    def test_method2(self):
##        print("test method 2")
##
##    def tearDown(self):
##        print("tear down method")
##
##    def test_method3(self):
##        print("test method 3")
##
##    def test_method4(self):
##        print("test method 4")
##
##    @classmethod
##    def tearDownClass(cls):
##        print("tear down class method")
##
##
##unittest.main()

import unittest

class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Set up class method")

    def setUp(self):
        print("set up method")

    def test_method1(self):
        print("test method 1")
        print(10/0)

    def test_method2(self):
        print("test method 2")

    def test_method3(self):
        print("test method 3")

    def test_method4(self):
        print("test method 4")
        print(10/0)

    def tearDown(self):
        print("tear down method")

    

    @classmethod
    def tearDownClass(cls):
        print("tear down class method")


unittest.main()
