##import unittest
##
##class TestCaseDemo(unittest.TestCase):
##
##    def test_c(self):
##        print("Test C method execution")
##
##    def test_b(self):
##        print("Test B method execution")
##
##    def test_a(self):
##        print("Test A method execution")
##
##unittest.main()

'''
Testsuite - A group of test case classes.
1. Test results will be displayed to the console only and it is not possible to generate reports.
2. UnitTest framework generates results in alphabetical order only and it is not possible to customised results.
3. As a part of batch execution(TestSuit),All specified methods from a specified TestCase classes will be executed and it is not possible to specify particular method.
4. In unittesting only limited setUp and tearDown methods are available.

    setUpClass() ----> Before executing all test methods of TestCase class.
    tearDownClass() ---->After executing all test methods of TestCase class.
    setUp() ---->Before every test method execution.
    tearDown() ---->After every test method execution.

    If we want to execute any activity before executing testsuite and after
    executing testsuite,then unittest framework does not define any methods.
    
'''
