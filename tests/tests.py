
import unittest
import requests
from app import Expression
import app

class ComputationServerTest(unittest.TestCase):
    def initiaterequest(self,url,data):
        requests.post(url,data=data)
        val = Expression.query(value).last()
        return val

    def testrequest(self):
        """test wether correct expression is returned or not"""
        url = "http://{}:8000/add/".format(self.get_docker_host())
        data = {'expression = 5*5'}
        self.assertEqual(make_request(url,data),25)

    def testbadrequest(self):
        """test wether invalid expression is checked or not"""
        url = "http://{}:8000/add/".format(self.get_docker_host())
        data = {'expression = 5-'}
        self.assertRaises(app.InvalidExpressionError,make_request(url,data))

    def testdb(self):
        """checks the database is up to date and added only valid expressions"""
        self.assertEqual(Expression.query(id).count(),1)