# test_trustguard.py
"""
Tests for TrustGuard module.
"""

import unittest
from trustguard import TrustGuard

class TestTrustGuard(unittest.TestCase):
    """Test cases for TrustGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrustGuard()
        self.assertIsInstance(instance, TrustGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrustGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
