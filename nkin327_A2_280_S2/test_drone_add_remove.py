import unittest

from drones import Drone, DroneStore
from operators import Operator

class Task1Test(unittest.TestCase):
    def test_drone_is_added(self):
        
        #Arrange 
        dr = Drone("Add_Test", class_type=1)
        dr2 = Drone("Add_Te3st", class_type=1)
        store = DroneStore()
        
        #Act
        act = store.add(dr)

        #Assert
        self.assertIn(dr.id, store.list_all() , "Drone not added.")
        self.assertRaises(Exception, lambda: store.add(dr))
    
    def test_drone_is_removed(self):
        
        #Arrange
        dr = Drone("Remove_Test", class_type=1)
        store = DroneStore()
        
        #Act
        act = store.add(dr)
        act = store.remove(dr)
        
        #Assert
        self.assertFalse(dr.id in store.list_all(), "Is in.")
        self.assertRaises(Exception, lambda: store.remove(dr))
        
        
if __name__ == '__main__':
    unittest.main()
