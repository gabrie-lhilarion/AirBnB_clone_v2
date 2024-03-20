import unittest
import json
import subprocess
from models import storage
from models.base_model import BaseModel

class test_console(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Prepare environment for testing"""
        # Ensure file.json is in a known state or empty
        storage._FileStorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests"""
        # Clear FileStorage objects to ensure a clean slate for other tests
        storage._FileStorage__objects = {}
        # Save the empty state to 'file.json' to cleanup
        storage.save()

    def test_params_create(self):
        """Test creating objects with parameters via console"""
        # Preparing the command to be executed
        command = "cat test_params_create | ./console.py"
        # Execute the command
        subprocess.run(command, shell=True, check=True)
        
        # Reload storage to update with newly created objects from 'file.json'
        storage.reload()

        # Verification
        all_objects = storage.all()
        self.assertTrue(len(all_objects) > 0, "No objects were created")

        # Additional checks can be added here based on expected outcomes, such as:
        # - Checking for specific object types created
        # - Verifying attributes of created objects

if __name__ == '__main__':
    unittest.main()
