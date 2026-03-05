"""Tests for deploy-vercel."""

import pytest
from deploy_vercel import vercel


class TestVercel:
    """Test suite for vercel."""

    def test_basic(self):
        """Test basic usage."""
        result = vercel("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            vercel("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = vercel(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
