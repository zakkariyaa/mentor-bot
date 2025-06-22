import pytest
from mentor.llm_interface import explain_code
from unittest.mock import patch

@pytest.mark.slow
def test_explain_code_runs():
    code = "def double(x): return x * 2"
    explanation = explain_code(code, model="phi")
    
    assert isinstance(explanation, str)
    assert "double" in explanation.lower() or "multiply" in explanation.lower()


@patch("mentor.llm_interface.explain_code")
def test_explain_code_mocked(mock_explain):
    mock_explain.return_value = "This is a test explanation."

    code = "def square(x): return x * x"
    result = mock_explain(code, model="phi")

    assert result == "This is a test explanation."
    mock_explain.assert_called_once()
