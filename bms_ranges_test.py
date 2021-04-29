import unittest
import bms_ranges_monitor

class test_battery_current_ranges(unittest.TestCase):
  def test_handled_fail_current_ranges(self):
    self.assertTrue(bms_ranges_monitor.current_ranges([]) == "Invalid Input")
    
  def test_passing_current_ranges(self):
    self.assertTrue(bms_ranges_monitor.current_ranges([3, 3, 5, 4, 10, 11, 12]) == "Valid Input") 

  def test_failing_current_ranges(self):
    self.assertTrue(bms_ranges_monitor.current_ranges(['a']) == "Invalid Input")    
    

if __name__ == '__main__':
  unittest.main()
