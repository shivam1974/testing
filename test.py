# Write your code below:
import surfshop
import unittest

class test_checker(unittest.TestCase):

  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboards1(self):
    self.assertEqual(self.cart.add_surfboards(1),'Successfully added 1 surfboard to cart!')

  def test_add_surfboards2(self):
    self.assertEqual(self.cart.add_surfboards(2),'Successfully added 2 surfboards to cart!')

  @unittest.skip
  def test_add_surfboards3(self):
    self.assertRaises(surfshop.TooManyBoardsError,self.cart.add_surfboards(5))

  #@unittest.expectedFailure
  def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

  def test_add_more_surfboards(self):
    num_surfboards = [2, 3, 4]

    for num in num_surfboards:
      self.cart = surfshop.ShoppingCart()
      with self.subTest(num):
        self.assertEqual(self.cart.add_surfboards(num), f'Successfully added {num} surfboards to cart!')


unittest.main()




