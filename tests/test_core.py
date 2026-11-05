import unittest,math
from differential_drive_excitation.core import run
class DomainTests(unittest.TestCase):
 def test_known(self):
  x=run({'track_width':.5,'segments':[dict(left_rotation=1,right_rotation=1,distance=.1,yaw=0),dict(left_rotation=-1,right_rotation=1,distance=0,yaw=.4)]});self.assertAlmostEqual(x['left_radius'],.1);self.assertAlmostEqual(x['right_radius'],.1)
 def test_stationary(self):self.assertEqual(run({'track_width':1,'segments':[dict(left_rotation=0,right_rotation=0,distance=0,yaw=0)]*2})['status'],'unidentifiable')
 def test_one_wheel_unexcited(self):self.assertEqual(run({'track_width':1,'segments':[dict(left_rotation=0,right_rotation=1,distance=.5,yaw=1)]*2})['status'],'unidentifiable')
