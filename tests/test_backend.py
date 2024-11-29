import unittest
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.main import app, detect_asd

class TestASDDetection(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_detect_route_exists(self):
        """Test that the detection route exists"""
        response = self.app.post('/detect')
        self.assertIn(response.status_code, [400, 500])  # No image uploaded

    def test_model_loading(self):
        """Test model loading"""
        from backend.main import model
        self.assertIsNotNone(model, "ML Model should be loaded")

if __name__ == '__main__':
    unittest.main()