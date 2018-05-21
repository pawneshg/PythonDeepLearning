# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:52:03 2018

@author: admin
"""

import unittest
from mock import patch

from employee import Employee

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print 'setup Class\n'
        
    @classmethod
    def tearDownClass(cls):
        print 'tearDownClass\n'
        
    def setUp(self):
        print 'setUp'
        self.emp_1 = Employee('first', 'last', 50000)
        self.emp_2 = Employee('shayam', 'gupta', 60000)
        
    def tearDown(self):
        print 'tearDown\n'
    
    def test_email(self):
        print 'test email\n'
        
        self.assertEqual(self.emp_1.email, 'first.last@email.com')
        self.assertEqual(self.emp_2.email, 'shayam.gupta@email.com')
        
    def test_fullname(self):
        print 'test fullname'
        
        self.assertEqual(self.emp_1.fullname, 'first last')
        self.assertEqual(self.emp_2.fullname, 'shayam gupta')
        
    def test_apply_raise(self):
        print 'test apply raise'
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
    
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'success'
            
            schedule = self.emp_1.monthly_schedule('may')
            mocked_get.assert_called_with('http://company.com/last/may')
            self.assertEqual(schedule, 'success')
            
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/gupta/June')
            self.assertEqual(schedule, 'bad Response!')
            
            
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    