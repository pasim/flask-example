#!env/bin/python
import os
import unittest
from models.Utility import Utility

class OutcodesTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_postcodeService(self):

        postcode = "GU34 2QS"
        data = Utility.load_postcode_data_single(postcode)
        self.assertIsNotNone(data)
        self.assertEqual(data['result']['longitude'], -0.956537)
        self.assertEqual(data['result']['latitude'], 51.157421)

    """
    @todo Mock the services
    """
    def test_outcodes(self):
        postcode = "SE28 0LH"
        radius = 25000
        data = Utility.nearest_outcodes(postcode,radius)
        self.assertIsNotNone(data)
        # Testing if data is sorted from North to South
        self.assertGreater(data[0]['northings'],data[-1]['northings'])

    def test_outcodesCase2(self):
        postcode = "GU34 2QS"
        radius = 25000
        data = Utility.nearest_outcodes(postcode,radius)
        self.assertIsNotNone(data)
        # Testing if data is sorted from North to South
        self.assertGreater(data[0]['northings'],data[-1]['northings'])

    def test_sorted(self):
        postcode = "GU34 2QS"
        radius = 25000
        data1 = Utility.nearest_outcodes(postcode, radius, False)
        data2 = sorted(data1, key=lambda i: i['northings'], reverse=True)
        self.assertNotEqual(data1,data2)

if __name__ == "__main__":
    unittest.main()
