import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFrontendUI(unittest.TestCase):
    def setUp(self):
        # Use headless Chrome for testing
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('file://' + os.path.abspath('frontend/index.html'))

    def test_ui_elements_exist(self):
        """Test that key UI elements are present"""
        image_upload = self.driver.find_element(By.ID, 'imageUpload')
        detect_button = self.driver.find_element(By.ID, 'detectButton')
        result_text = self.driver.find_element(By.ID, 'resultText')
        
        self.assertTrue(image_upload.is_displayed())
        self.assertTrue(detect_button.is_displayed())
        self.assertTrue(result_text.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()