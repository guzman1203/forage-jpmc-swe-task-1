import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceBidLessThanAsk(self):
    quotes = [
      {'top_ask': {'price': 120.48, 'size': 109}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.2, 'size': 36}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 117.87, 'size': 81}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.68, 'size': 4}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
 
  def test_getDataPoint_calculatePriceBidEqualAsk(self):
    quotes = [
      {'top_ask': {'price': 120.48, 'size': 109}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.68, 'size': 4}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
 
  def test_getRatio_calculateRatio(self):
    price_as = [120.23, 331.22]
    price_bs = [56.45 , 102.44]
    for index in range(len(price_as)):
      self.assertEqual(getRatio(price_as[index], price_bs[index]), price_as[index]/price_bs[index])

  def test_getRatio_calculatePriceAGreaterThanPriceB(self):
    price_as = [120.23, 331.22]
    price_bs = [56.45 , 102.44]
    for index in range(len(price_as)):
      self.assertEqual(getRatio(price_as[index], price_bs[index]), price_as[index]/price_bs[index])

  def test_getRatio_calculatePriceALessThanPriceB(self):
    price_as = [56.45 , 102.44]
    price_bs = [120.23, 331.22]
    for index in range(len(price_as)):
      self.assertEqual(getRatio(price_as[index], price_bs[index]), price_as[index]/price_bs[index])

  def test_getRatio_calculatePriceAEqualPriceB(self):
    price_as = [56.45 , 102.44]
    price_bs = [56.45 , 102.44]
    for index in range(len(price_as)):
      self.assertEqual(getRatio(price_as[index], price_bs[index]), price_as[index]/price_bs[index])

  def test_getRatio_calculatePriceBEqualZero(self):
    price_as = [56.45 , 102.44]
    price_bs = [0 , 0]
    for index in range(len(price_as)):
      self.assertEqual(getRatio(price_as[index], price_bs[index]), None)

if __name__ == '__main__':
    unittest.main()
