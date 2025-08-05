import sys
import os
import pytest
import unittest.mock
import uuid

# Add the project root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Mock AWS credentials before importing app
os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
os.environ['AWS_SECURITY_TOKEN'] = 'testing'
os.environ['AWS_SESSION_TOKEN'] = 'testing'
os.environ['AWS_DEFAULT_REGION'] = 'ap-southeast-1'

from app import app, TodoItem

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture
def todo_item():
    """Create a mock TodoItem for testing"""
    mock_item = unittest.mock.MagicMock()
    mock_item.id = str(uuid.uuid4())
    mock_item.title = 'Test Todo'
    mock_item.completed = False
    
    # Mock the update method
    def mock_update(actions):
        # Simulate the update action
        for action in actions:
            if hasattr(action, 'value'):
                mock_item.completed = action.value
            else:
                mock_item.completed = not mock_item.completed
    
    mock_item.update = mock_update
    mock_item.save = unittest.mock.MagicMock()
    mock_item.delete = unittest.mock.MagicMock()
    
    yield mock_item

@pytest.fixture(autouse=True)
def mock_dynamodb():
    """Mock all DynamoDB operations globally for all tests"""
    with unittest.mock.patch.object(TodoItem, 'save') as mock_save, \
         unittest.mock.patch.object(TodoItem, 'delete') as mock_delete, \
         unittest.mock.patch.object(TodoItem, 'scan') as mock_scan, \
         unittest.mock.patch.object(TodoItem, 'get') as mock_get:
        
        # Configure mocks
        mock_save.return_value = None
        mock_delete.return_value = None
        mock_scan.return_value = []
        
        # Mock get to return a default item or raise DoesNotExist
        def mock_get_func(item_id):
            if item_id == 'nonexistent':
                raise TodoItem.DoesNotExist()
            mock_item = unittest.mock.MagicMock()
            mock_item.id = item_id
            mock_item.title = 'Test Todo'
            mock_item.completed = False
            return mock_item
        
        mock_get.side_effect = mock_get_func
        
        yield {
            'save': mock_save,
            'delete': mock_delete,
            'scan': mock_scan,
            'get': mock_get
        }