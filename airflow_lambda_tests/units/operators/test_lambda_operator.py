# coding: utf8

import json
import unittest
from unittest.mock import Mock

from airflow_lambda.operators.lambda_operator import LambdaOperator


class LambdaOperatorTest(unittest.TestCase):

    def setUp(self):
        self.tested = LambdaOperator(
            context_to_payload=lambda x : x,
            lambda_function_name='test',
            task_id='test'
        )
        self.tested.lambda_client = Mock()

    def test_lambda_is_invoked(self):
        # Assign
        response_mock = Mock()
        read_mock = Mock()
        read_mock.read = Mock(return_value='{ "code": 200 }')
        response_mock.get = Mock(side_effect=[
            'test',
            read_mock,
            'test'
        ])

        self.tested.lambda_client.invoke = Mock(return_value=response_mock)

        # Acts
        self.tested.execute(context={})

        # Assert


if __name__ == '__main__':
    unittest.main()
