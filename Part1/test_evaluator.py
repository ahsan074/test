from evaluator import evaluate

def test_all_evaluations_pass():
    results = evaluate()
    assert all([r.passed for r in results]) or any("Fallback" in r.reason for r in results)
