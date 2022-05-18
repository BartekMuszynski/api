import unittest
import requests
from variables import *

endpoint = "https://api.openweathermap.org/data/2.5/weather?"
class geoloc_tests(unittest.TestCase):

    def testc1_1(self):
        geo_params = {"lat": 51.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_geo = requests.get(endpoint, geo_params)
        self.assertEqual(locate_by_geo.status_code, 200)
        self.assertEqual(city["name"], locate_by_geo.json()["name"])

    def test1_2(self):
        geo_params = {"lat": 21312351.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_geo = requests.get(endpoint, geo_params)
        self.assertEqual(locate_by_geo.status_code, 400)

    def test1_3(self):
        geo_params = {"lat": 51.5085, "lon": -1231231230.1257, "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_geo = requests.get(endpoint, geo_params)
        self.assertEqual(locate_by_geo.status_code, 400)

    def test1_4(self):
        geo_params = {"lat": 51.5085, "lon": -1231231230.1257, "appid": "aaaaaa"}
        locate_by_geo = requests.get(endpoint, geo_params)
        self.assertEqual(locate_by_geo.status_code, 401)

    def test2_1(self):
        city_name_params = {"q": "London", "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_name = requests.get(endpoint, city_name_params)
        self.assertEqual(locate_by_name.status_code, 200)
        self.assertEqual(city["name"], locate_by_name.json()["name"])

    def test2_2(self):
        city_name_params = {"q": "London,uk", "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_name = requests.get(endpoint, city_name_params)
        self.assertEqual(locate_by_name.status_code, 200)
        self.assertEqual(city["name"], locate_by_name.json()["name"])

    def test2_3(self):
        city_name_params = {"q": "London,polska", "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_name = requests.get(endpoint, city_name_params)
        self.assertEqual(locate_by_name.status_code, 200)
        self.assertEqual(city["name"], locate_by_name.json()["name"])

    def test2_4(self):
        city_name_params = {"q": "Londonaaaa,uk", "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_name = requests.get(endpoint, city_name_params)
        self.assertEqual(locate_by_name.status_code, 404)

    def test2_5(self):
        city_name_params = {"q": "London,uk", "appid": "bbbbbbbbbb"}
        locate_by_name = requests.get(endpoint, city_name_params)
        self.assertEqual(locate_by_name.status_code, 401)

    def test3_1(self):
        city_id_params = {"id": 2643743, "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_id = requests.get(endpoint, city_id_params)
        self.assertEqual(locate_by_id.status_code, 200)
        self.assertEqual(city["name"], locate_by_id.json()["name"])

    def test3_2(self):
        city_id_params = {"id": 2643743213211232313, "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_id = requests.get(endpoint, city_id_params)
        self.assertEqual(locate_by_id.status_code, 404)

    def test3_3(self):
        city_id_params = {"id": 2643743, "appid": "oooooooo"}
        locate_by_id = requests.get(endpoint, city_id_params)
        self.assertEqual(locate_by_id.status_code, 401)

    def test4_1(self):
        city_zip_params = {"zip": "EC1A,gb", "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_zip = requests.get(endpoint, city_zip_params)
        self.assertEqual(locate_by_zip.status_code, 200)
        self.assertEqual(city["name"], locate_by_zip.json()["name"])

    def test4_2(self):
        city_zip_params = {"zip": "ECaaaaa1A,gb", "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_zip = requests.get(endpoint, city_zip_params)
        self.assertEqual(locate_by_zip.status_code, 404)

    def test4_3(self):
        city_zip_params = {"zip": "EC1A,gb", "appid": "vvv"}
        locate_by_zip = requests.get(endpoint, city_zip_params)
        self.assertEqual(locate_by_zip.status_code, 401)

    def test5_1(self):
        params_kevin = {"lat": 51.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99"}
        kevin_params  = requests.get(endpoint,params_kevin)
        params_celcius ={"lat": 51.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99","units":"metric"}
        celcius_params = requests.get(endpoint,params_celcius)
        self.assertAlmostEqual(kevin_params.json()["main"]["temp"]-273.15,celcius_params.json()["main"]["temp"],0)

    def test5_2(self):
        params_kevin = {"lat": 51.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99"}
        kevin_params = requests.get(endpoint, params_kevin)
        params_imperial = {"lat": 51.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99","units": "imperial"}
        imperial_params = requests.get(endpoint, params_imperial)
        self.assertAlmostEqual(1.8*(kevin_params.json()["main"]["temp"]-273) + 32,imperial_params.json()["main"]["temp"],0)

    def test5_3(self):
        params_kevin = {"lat": 51.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99"}
        kevin_params = requests.get(endpoint, params_kevin)
        params_wrong = {"lat": 51.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99","units":"nono"}
        wrong_params = requests.get(endpoint, params_wrong)
        self.assertAlmostEqual(kevin_params.json()["main"]["temp"],wrong_params.json()["main"]["temp"],0)

    def test5_4(self):
        params_celcius = {"lat": 51.5085, "lon": -0.1257, "appid": "1wwww","units": "metric"}
        celcius_params = requests.get(endpoint, params_celcius)
        self.assertEqual(celcius_params.status_code,401)

    def test5_5(self):
        params_imperial = {"lat": 51.5085, "lon": -0.1257, "appid": "1wwww","units": "imperial"}
        imperial_params = requests.get(endpoint, params_imperial)
        self.assertEqual(imperial_params.status_code,401)

    def test6_1(self):
        lang_change = {"lat": 51.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99", "lang": "pl"}
        locate_with_lang = requests.get(endpoint, lang_change)
        self.assertEqual(locate_with_lang.status_code, 200)
        self.assertEqual(locate_with_lang.json()["name"], "Londyn")

    def test6_2(self):
        lang_change = {"lat": 51.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99", "lang": "plaaa"}
        locate_with_lang = requests.get(endpoint, lang_change)
        geo_params = {"lat": 51.5085, "lon": -0.1257, "appid": "171de91891a63744eb7dd760cc43da99"}
        locate_by_geo = requests.get(endpoint, geo_params)
        self.assertEqual(locate_with_lang.json()["name"],locate_by_geo.json()["name"])

    def test6_3(self):
        lang_change = {"lat": 51.5085, "lon": -0.1257, "appid": "ggg", "lang": "pl"}
        locate_with_lang = requests.get(endpoint, lang_change)
        self.assertEqual(locate_with_lang.status_code, 401)

    def tes7_1(self):
        city_name_params = {"q": "Dallas,OR,US", "appid": "171de91891a63744eb7dd760cc43da99"}
        city = requests.get(endpoint, city_name_params)
        self.assertEqual(city.status_code,200)
        self.assertEqual(city.json()["id"],"5722064")


    def test7_2(self):
        city_name_params = {"q": "Dallas,OR", "appid": "171de91891a63744eb7dd760cc43da99"}
        city = requests.get(endpoint, city_name_params)
        self.assertEqual(city.status_code, 404)

    def test7_3(self):
        city_name_params = {"q": "Dallas", "appid": "171de91891a63744eb7dd760cc43da99"}
        city = requests.get(endpoint, city_name_params)
        self.assertEqual(city.status_code, 200)
        self.assertEqual(city.json()["id"],4684904)

    def test7_4(self):
        city_name_params = {"q": "Dallas,OR,US", "appid": "orr"}
        city = requests.get(endpoint, city_name_params)
        self.assertEqual(city.status_code, 401)

    def test7_5(self):
        city_name_params = {"q": "Dallas,TX,US", "appid": "171de91891a63744eb7dd760cc43da99"}
        city = requests.get(endpoint, city_name_params)
        self.assertEqual(city.status_code, 200)
        self.assertEqual(city.json()["id"], 4684904)

    def test7_6(self):
        city_name_params = {"q": "Dallas,TX,", "appid": "171de91891a63744eb7dd760cc43da99"}
        city = requests.get(endpoint, city_name_params)
        self.assertEqual(city.status_code, 200)
        self.assertEqual(city.json()["id"], 4684904)

    def test7_7(self):
        city_name_params = {"q": "Dallas", "appid": "171de91891a63744eb7dd760cc43da99"}
        city = requests.get(endpoint, city_name_params)
        self.assertEqual(city.status_code, 200)
        self.assertEqual(city.json()["id"],4684904)

    def test7_8(self):
        city_name_params = {"q": "Dallas,TX,US", "appid": "wrong"}
        city = requests.get(endpoint, city_name_params)
        self.assertEqual(city.status_code, 401)
















