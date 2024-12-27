import pytest
from src.app import lambda_handler


def test_lambda_handler():
    # Test event
    event = {}
    context = {}

    # Call the handler
    response = lambda_handler(event, context)

    # Assert the response
    assert response['statusCode'] == 200
    assert response['body']['message'] == 'Hello from Lambda!'