#!/usr/bin/python3
'''
TestPlace class
'''
from models.place import Place
from tests.test_models.test_base_model import TestBaseModel

class TestBase(TestBaseModel):
    '''
    =====================
    Test place
    =====================
    '''
    
    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super().__init__(*args, **kwargs)
        self.test_class = Place
        self.test_name = "Place"

    def test_city_id(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.city_id, str)

    def test_user_id(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.user_id, str)

    def test_city_name(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.name, str)

    def test_description(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.description, str)

    def test_num_rooms(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.number_rooms, int)

    def test_num_bathrooms(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.number_bathrooms, int)

    def test_max_guest(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.max_guest, int)

    def test_price_by_night(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.price_by_night, int)

    def test_longitude(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.longitude, float)

    def test_latitude(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.latitude, float)

    def test_amenity_id(self):
        '''
        Attribute test
        '''
        Place = self.test_class()
        self.assertIsInstance(Place.amenity_ids, list)
