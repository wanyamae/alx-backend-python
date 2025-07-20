#!/usr/bin/env python3
"""
Unit tests for utils.py functions.
"""

from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function."""

    @parameterized.expand([
        ("simple", {"a": 1}, ("a",), 1),
        ("nested_dict", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("nested_path", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        name: str,
        nested_map: dict,
        path: tuple,
        expected
    ) -> None:
        """Test that access_nested_map returns expected result for valid paths."""
        self.assertEqual(
            access_nested_map(nested_map, path),
            expected
        )

    @parameterized.expand([
        ("missing_key", {}, ("a",)),
        ("missing_nested_key", {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
        self,
        name: str,
        nested_map: dict,
        path: tuple
    ) -> None:
        """Test that access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(
            str(cm.exception),
            repr(path[-1])
        )


class TestGetJson(unittest.TestCase):
    """Test cases for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(
        self,
        test_url: str,
        test_payload: dict,
        mock_get: Mock
    ) -> None:
        """Test that get_json returns expected payload and requests.get is called once."""
        mock_get.return_value = Mock(json=Mock(return_value=test_payload))
        self.assertEqual(
            get_json(test_url),
            test_payload
        )
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test cases for memoize decorator."""

    def test_memoize(self) -> None:
        """Test that memoize caches method result and calls underlying method only once."""

        class TestClass:
            """Class for testing memoize decorator."""
            def a_method(self: "TestClass") -> int:
                """Returns 42."""
                return 42

            @memoize
            def a_property(self: "TestClass") -> int:
                """Returns result of a_method, memoized."""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()
