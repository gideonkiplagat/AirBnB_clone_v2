# test_params_create.py

import unittest
from console import HBNBCommand
from models import storage
from models.state import State
from models.place import Place

class TestCreateWithParameters(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        # Clean up (optional)
        storage.delete_all()
        storage.save()

    def test_create_state_with_parameters(self):
        # Create a State instance with parameters
        self.console.do_create("State name=\"California\"")
        self.console.do_create("State name=\"Arizona\"")

        # Check if the instances were created and saved
        state_ids = [self.console.last_id_created, self.console.last_id_created - 1]
        for state_id in state_ids:
            state_instance = storage.get("State", state_id)
            self.assertIsNotNone(state_instance)
            self.assertIn(state_instance.name, ["California", "Arizona"])

    def test_create_place_with_parameters(self):
        # Create a Place instance with parameters
        self.console.do_create("Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297")

        # Check if the Place instance was created and saved
        place_id = self.console.last_id_created
        place_instance = storage.get("Place", place_id)
        self.assertIsNotNone(place_instance)
        self.assertEqual(place_instance.city_id, "0001")
        self.assertEqual(place_instance.user_id, "0001")
        self.assertEqual(place_instance.name, "My little house")
        self.assertEqual(place_instance.number_rooms, 4)
        self.assertEqual(place_instance.number_bathrooms, 2)
        self.assertEqual(place_instance.max_guest, 10)
        self.assertEqual(place_instance.price_by_night, 300)
        self.assertAlmostEqual(place_instance.latitude, 37.773972, places=6)
        self.assertAlmostEqual(place_instance.longitude, -122.431297, places=6)

if __name__ == "__main__":
    unittest.main()
