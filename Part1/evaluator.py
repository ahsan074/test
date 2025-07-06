from models import EvaluationResult
from agent import handle_prompt

TEST_CASES = [
    {"name": "Weather Query", "input": "What's the weather in Paris?", "expect_tool": "Weather API"},
    {"name": "Wikipedia Query", "input": "Tell me about Python programming", "expect_tool": "Wikipedia Tool"},
    {"name": "Fallback Case", "input": "Sing me a song", "expect_tool": "Fallback"},
    {"name": "Empty Input", "input": "", "expect_tool": "Error Handler"},
    {"name": "Tool Edge Case", "input": "Tell me about", "expect_tool": "Error Handler"},
]

def evaluate():
    results = []
    for case in TEST_CASES:
        result = handle_prompt(case["input"])
        passed = result["tool_used"] == case["expect_tool"]
        results.append(EvaluationResult(
            test_name=case["name"],
            passed=passed,
            reason=f"Expected {case['expect_tool']}, got {result['tool_used']}"
        ))
    return results

if __name__ == "__main__":
    results = evaluate()
    for res in results:
        status = "✅ PASS" if res.passed else "❌ FAIL"
        print(f"{res.test_name:25} | {status} - {res.reason}")
