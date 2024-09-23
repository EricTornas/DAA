import unittest
import random
from dp import subset_sum_dp
from backtrack import backtrack

class TestSubsum(unittest.TestCase):
    def __init__(self, methodName, func):
        super().__init__(methodName)
        self.subsum = func
        
    def test_is_true_1(self):
        S = [1, 2, 3, 4, 5, 6]  
        T = 6
        resultado = self.subsum(S, T)
        self.assertEqual(resultado, True)
    

    def test_is_true_2(self):
        S = [random.randint(1, 500) for _ in range(20)] 
        j = random.randint(1, 20)
        ans = random.sample(S, j)
        T = sum(ans)
        resultado = self.subsum(S, T)
        self.assertEqual(resultado, True)

    def test_is_false_1(self):
        S = [1, 2, 5, 6, 7]  
        T = 4 
        resultado = self.subsum(S, T)
        self.assertEqual(resultado, False)  

    def test_is_false_2(self):
        S = [1, 2, 3, 4, 5, 6]  
        T = 100  
        resultado = self.subsum(S, T)
        self.assertEqual(resultado, False)  


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestSubsum('test_is_true_1', backtrack))
    suite.addTest(TestSubsum('test_is_true_2', backtrack))
    suite.addTest(TestSubsum('test_is_false_1', backtrack))  
    suite.addTest(TestSubsum('test_is_false_2', backtrack))  
    suite.addTest(TestSubsum('test_is_true_1', subset_sum_dp))
    suite.addTest(TestSubsum('test_is_true_2', subset_sum_dp))
    suite.addTest(TestSubsum('test_is_false_1', subset_sum_dp))  
    suite.addTest(TestSubsum('test_is_false_2', subset_sum_dp))  
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_tests()
