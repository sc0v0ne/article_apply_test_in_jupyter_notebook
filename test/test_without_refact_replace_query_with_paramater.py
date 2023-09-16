from testbook import testbook
import pytest

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_treatment_missing_values_original(tb):
    function_notebook = tb.ref("treatment_missing_values_original")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']  
    assert function_notebook() is None
    with pytest.raises(Exception) as e_info:
        function_notebook(group) is None
    assert "takes 0 positional arguments but 1 was given" in str(e_info.value)





