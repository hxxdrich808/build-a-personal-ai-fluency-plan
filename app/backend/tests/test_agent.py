import pytest
from ..agent import generate_fluency_plan

def test_generate_fluency_plan_non_empty():
    """Agent should return a non-empty plan for valid input."""
    sample_input = "I want to become proficient in using AI tools for data analysis."
    plan = generate_fluency_plan(sample_input)
    assert isinstance(plan, str)
    assert len(plan.strip()) > 0
    # Basic check that the plan contains stage headings
    for heading in ["Awareness", "Understanding", "Application", "Mastery"]:
        assert heading in plan

def test_generate_fluency_plan_empty_input():
    """Agent should raise ValueError when input is empty."""
    with pytest.raises(ValueError):
        generate_fluency_plan("   ")
