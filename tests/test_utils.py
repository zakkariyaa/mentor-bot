from mentor.utils import static_warnings

def test_detects_missing_base_case():
    code = "def factorial(n): return n * factorial(n - 1)"
    warnings = static_warnings(code)
    
    assert any("base case" in w.lower() for w in warnings)

def test_detects_infinite_loop():
    code = "while True:\n    pass"
    warnings = static_warnings(code)
    
    assert any("infinite loop" in w.lower() for w in warnings)

def test_warns_on_eval():
    code = "eval('2 + 2')"
    warnings = static_warnings(code)
    
    assert any("eval" in w.lower() for w in warnings)
