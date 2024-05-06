import unittest
from fibonacci_service import fibonacci_gen




class TestFibonacciGen(unittest.TestCase):
    def test_1_digit_minute(self):
        """Test case where minute = 09, and 5 elements
            [0,9,9,18,27]
        """
        generator = fibonacci_gen(0,9)
        result = [next(generator) for _ in range(5)]
        correct = [0,9,9,18,27]

        self.assertEqual(result, correct)
        
    def test_biggest_case(self):
        """ Test to see the biggest use case where 59 digits are generated
         1,1 seeds to check with traditional fibonacci
        """
        generator = fibonacci_gen(1,1)
        result = [next(generator) for _ in range(59)]
        correct = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 
                   46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 
                   24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 
                   2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445,
                     225851433717, 365435296162, 591286729879, 956722026041]
    
        self.assertEqual(result, correct)