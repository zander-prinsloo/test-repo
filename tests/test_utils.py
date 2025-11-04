"""
Tests for utility functions
"""

import pytest
import pandas as pd
from pathlib import Path
import tempfile
import os

# Add parent directory to path to import src module
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils import load_data, save_data


def test_save_and_load_data():
    """Test saving and loading data"""
    # Create sample data
    df = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': ['a', 'b', 'c']
    })
    
    # Use temporary file
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, 'test_data.csv')
        
        # Save data
        save_data(df, filepath)
        
        # Load data
        loaded_df = load_data(filepath)
        
        # Verify data matches
        pd.testing.assert_frame_equal(df, loaded_df)


def test_load_nonexistent_file():
    """Test loading a file that doesn't exist"""
    with pytest.raises(FileNotFoundError):
        load_data('nonexistent_file.csv')
