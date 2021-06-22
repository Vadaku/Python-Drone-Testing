import unittest

from datetime import date
from drones import Drone, DroneStore
from operators import Operator, OperatorStore, OperatorAction

class Task2Test(unittest.TestCase):
    def test_op_is_valid(self):
        
        #Arrange
        op = Operator()
        op.first_name = "Valid"
        op.family_name = "Drone"
        op.date_of_birth = date(1996, 11, 13)
        op.drone_license = 2
        op.operations = 5
        op.rescue_endorsement = True
        opStore = OperatorStore()
        
        #Act 
        act = opStore.add(op)
        
        #Assert
        self.assertTrue(act.is_valid())
        
    def test_name(self):
        #Arrange
        op = Operator()
        op.date_of_birth = date(1981, 11, 13)
        op.drone_license = 2
        opStore = OperatorStore()
        
        #Act
        act = opStore.add(op)
        
        #Assert
        self.assertFalse(act.is_valid())
        self.assertIn("First name is required", act.messages)
        
    def test_dob_is_valid(self):
        
        #Arrange
        op = Operator()
        op.first_name = "DOB"
        op.drone_license = 2
        opStore = OperatorStore()
        
        #Act
        act = opStore.add(op)
        
        #Assert
        self.assertFalse(act.is_valid())
        self.assertIn("Date of birth is required", act.messages)
        
    def test_license_is_valid(self):
        
        #Arrange
        op = Operator()
        op.first_name = "LIC"
        op.date_of_birth = date(1981, 11, 13)
        opStore = OperatorStore()
        
        #Act
        act = opStore.add(op)
        
        #Assert
        self.assertFalse(act.is_valid())
        self.assertIn("Drone license is required", act.messages)
        
    def test_age_is_valid(self):
        
        #Arrange
        op = Operator()
        op.first_name = "AGE"
        op.drone_license = 2
        op.date_of_birth = date(2005, 11, 30)
        opStore = OperatorStore()
        op.operations = 5
        #Act
        act = opStore.add(op)
        
        #Assert
        self.assertFalse(act.is_valid())
        self.assertIn("Operator should be at least twenty to hold a class 2 license", act.messages)
    
    def test_rescue_is_valid(self):
        
        #Arrange
        op = Operator()
        op.first_name = "RES"
        op.drone_license = 2
        op.date_of_birth = date(1999, 11, 30)
        
        opStore = OperatorStore()
        
        #Act
        act = opStore.add(op)
        
        #Assert
        self.assertFalse(act.is_valid())
        self.assertIn("Rescue endorsement and operations not valid", act.messages)
    
    def test_add_is_valid(self):
        
        #Arrange 
        op = Operator()
        op.first_name = "ADD"
        op.date_of_birth = date(1991, 11, 23)
        opStore = OperatorStore()
        op.operations = 5
        op.drone_license = 2
        op.rescue_endorsement = True
        
        
        #Act
        act = opStore.add(op)
        act.commit()

        #Assert
        self.assertIn(op.id, opStore.list_all())
       
        
if __name__ == '__main__':
    unittest.main()