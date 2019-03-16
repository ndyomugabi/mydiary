import unittest
import json
from run import APP
"""
Class for all gets and Post
"""
class TestViews(unittest.TestCase):
  

    def setUp(self):

        self.question = APP
        self.client = self.question.test_client
    """
    methods defines test cases for get all enties
    """
    def test_get_all_entries(self):

        result = self.client().get('/api/v1/entries/')
        self.assertEqual(result.status_code,200)
      
    """
    methods defines test cases for get a single entry
    """
        
    def test_get_one_entry(self):

        result = self.client().get('/api/v1/entries/2')
        self.assertEqual(result.status_code,301)
                
    """
    methods defines test cases for post an entry
    """

    def test_add_entry(self):

        result = self.client().post('/api/v1/entries/', content_type="application/json", data=json.dumps(
            dict(title="bootcamp", description="meeting3",event_id="1",)))
        self.assertEqual(result.status_code, 201)
        
  
    def test_update(self):
        """
            Method for testing modifying an entry
        """
        result1 = self.client().post('/api/v1/entries/', content_type="application/json", data=json.dumps(
            dict(title="bootcamp2", description="meeting8")))
        result = self.client().put('/api/v1/entries/2/', content_type="application/json", data=json.dumps(dict(title='bootcamp')))      
        self.assertEqual(result.status_code, 200)
    