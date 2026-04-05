import unittest
from pathlib import Path
import tempfile
import shutil
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def setUp(self):
        """Create a temporary directory for testing"""
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = Path.cwd()
        
    def tearDown(self):
        """Clean up temporary directory"""
        shutil.rmtree(self.test_dir)
    
    def test_write_file_simple(self):
        """Test writing a file in the project root"""
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(f"Test 1 - Simple write: {result}")
        self.assertTrue(result)
    
    def test_write_file_nested(self):
        """Test writing a file in a nested directory"""
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(f"Test 2 - Nested write: {result}")
        self.assertTrue(result)
    
    def test_write_file_absolute_path_denied(self):
        """Test that absolute paths are not allowed"""
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(f"Test 3 - Absolute path denied: {result}")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()