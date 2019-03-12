import unittest
import json
from run import APP

class TestViews(unittest.TestCase):
  

    def setUp(self):

        self.dairies = APP
        self.client = self.dairies.test_client
    def test_AllDairyEntries(self):

        result = self.client().get('/api/v1/entries/')
        self.assertEqual(result.status_code, 200)

    def test_OneEntry(self):
        result_one=self.client().get('/api/v1/entries/1')
        self.assertEqual(result_one.status_code,301)

    def test_PostEntry(self):
        result = self.client().post('/api/v1/entries/',content_type="application/json", data=json.dumps(
            dict(title="natasha", description="what is boot camp",event_id="1",)))
        self.assertEqual(result.status_code, 201)

