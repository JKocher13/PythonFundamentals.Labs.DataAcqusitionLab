import unittest
import make_request_revised 

class Test_make_request_revised(unittest.TestCase):
 	
 	def test_build_url(self):
 		self.assertEqual(make_request_revised.build_url("https://www.youtube.com/watch?v=6tNS--", "WetLI"), "https://www.youtube.com/watch?v=6tNS--WetLI")
 		self.assertEqual(make_request_revised.build_url('https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=', 2000), "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=2000")


 	def test_build_file_name(self):
 		self.assertEqual(make_request_revised.build_file_name(2),"location_2")
 		self.assertEqual(make_request_revised.build_file_name(54534),"location_54534")    


if __name__ == '__main__':
	unittest.main()
 