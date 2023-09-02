from testbook import testbook
import pytest


@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_treatment_missing_values_original(tb):
    function_notebook = tb.ref("treatment_missing_values_original")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    message_exception  = 'treatment_missing_values_original() takes 0 positional arguments but 1 was given'
    
    assert function_notebook() == None
    with pytest.raises(ValueError) as e_info:
        raise ValueError(message_exception)
        function_notebook(group) == None

        assert e_info.type is ValueError
        assert e_info.value.args[0] == message_exception
    

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_treatment_missing_values_refc_05(tb):
    function_notebook = tb.ref("treatment_missing_values_refc_05")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook(group) == None


