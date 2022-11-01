#!/usr/bin/python3
'''
TestReview class
'''
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel

class TestReview(TestBaseModel):
    '''
    =====================
    Test Review
    =====================
    '''
    
    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super().__init__(*args, **kwargs)
        self.test_class = Review
        self.test_name = "Review"

    def test_place_id(self):
        '''
        Attribute test
        '''
        Review = self.test_class()
        self.assertIsInstance(Review.place_id, str)

    def test_user_id_review(self):
        '''
        Attribute test
        '''
        Review = self.test_class()
        self.assertIsInstance(Review.user_id, str)

    def test_text(self):
        '''
        Attribute test
        '''
        Review = self.test_class()
        self.assertIsInstance(Review.text, str)
