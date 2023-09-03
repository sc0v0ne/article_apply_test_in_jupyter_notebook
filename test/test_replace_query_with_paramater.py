from testbook import testbook
import pytest


MESSAGE_EXCEPTION  = 'treatment_missing_values_original() takes 0 positional arguments but 1 was given'

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_treatment_missing_values_original(tb):
    function_notebook = tb.ref("treatment_missing_values_original")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    
    
    assert function_notebook() == None
    with pytest.raises(ValueError) as e_info:
        raise ValueError(MESSAGE_EXCEPTION)
        function_notebook(group) == None

    assert e_info.type is ValueError
    assert e_info.value.args[0] == MESSAGE_EXCEPTION

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_treatment_missing_values_refc_01(tb):
    function_notebook = tb.ref("treatment_missing_values_refc_01")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook() == None
    with pytest.raises(ValueError) as e_info:
        raise ValueError(MESSAGE_EXCEPTION)
        function_notebook(group) == None

    assert e_info.type is ValueError
    assert e_info.value.args[0] == MESSAGE_EXCEPTION
    

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_XXXNEWtreatment_missing_values_refc_02(tb):
    function_notebook = tb.ref("XXXNEWtreatment_missing_values_refc_02")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook(group) == None
    with pytest.raises(ValueError) as e_info:
        raise ValueError(MESSAGE_EXCEPTION)
        function_notebook() == None


    assert e_info.type is ValueError
    assert e_info.value.args[0] == MESSAGE_EXCEPTION

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_XXXNEWtreatment_missing_values_refc_03_refactor(tb):
    function_notebook = tb.ref("XXXNEWtreatment_missing_values_refc_03_refactor")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook() == None
    with pytest.raises(ValueError) as e_info:
        raise ValueError(MESSAGE_EXCEPTION)
        function_notebook(group) == None


    assert e_info.type is ValueError
    assert e_info.value.args[0] == MESSAGE_EXCEPTION

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_XXXNEWtreatment_missing_values_refc_04(tb):
    function_notebook = tb.ref("XXXNEWtreatment_missing_values_refc_04")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook(group) == None
    with pytest.raises(ValueError) as e_info:
        raise ValueError(MESSAGE_EXCEPTION)
        function_notebook() == None


    assert e_info.type is ValueError
    assert e_info.value.args[0] == MESSAGE_EXCEPTION


@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_treatment_missing_values_refc_05(tb):
    function_notebook = tb.ref("treatment_missing_values_refc_05")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook(group) == None
    with pytest.raises(ValueError) as e_info:
        raise ValueError(MESSAGE_EXCEPTION)
        function_notebook() == None


    assert e_info.type is ValueError
    assert e_info.value.args[0] == MESSAGE_EXCEPTION


