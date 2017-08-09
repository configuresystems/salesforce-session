import unittest
import datetime
import os
from salesforce_session import SalesForceSession


class TestSalesForceSession(unittest.TestCase):
    def setUp(self):
        self.date = datetime.date(2017, 1, 6)
        self.sfl = SalesForceSession(
            username=os.environ['SF_USERNAME'],
            password=os.environ['SF_PASSWORD'],
            security_token=os.environ['SF_SECURITY_TOKEN'],
            client_id=os.environ['SF_CLIENT_ID'],
            )

    def test_get_session(self):
        session = self.sfl.get_session()
        self.assertNotEqual('', session.session_id)

    def test_raw_query(self):
        query = "SELECT Status FROM Case LIMIT 5"
        response = self.sfl.raw_query(query)
        self.assertEqual(5, len(response))

    def test_query(self):
        response = self.sfl.query(
            query_type='SELECT',
            fields=['Status'],
            sql_object='Case',
            conditions='',
            limit=5
            )
        self.assertEqual(5, len(response))

    def test_query_with_conditional(self):
        response = self.sfl.query(
            query_type='SELECT',
            fields=['Status'],
            sql_object='Case',
            conditions="Status='New'",
            limit=5
            )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual('New', response[0]['Status'])
        self.assertEqual(5, len(response))


if __name__ == '__main__':
    unittest.main()
