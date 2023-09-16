import json
import pandas as pd
from testbook import testbook
import pytest
import os

os.environ['JUPYTER_PLATFORM_DIRS'] = '1'

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_treatment_missing_values_refc_01(tb):
    function_notebook = tb.ref("treatment_missing_values_refc_01")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook() is None
    with pytest.raises(Exception) as e_info:
        function_notebook(group) is None
    assert "takes 0 positional arguments but 1 was given" in str(e_info.value)
    

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_XXXNEWtreatment_missing_values_refc_02(tb):
    function_notebook = tb.ref("XXXNEWtreatment_missing_values_refc_02")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook(group) is None
    with pytest.raises(Exception) as e_info:
        function_notebook() is None
    assert "missing 1 required positional argument" in str(e_info.value)

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_XXXNEWtreatment_missing_values_refc_03_refactor(tb):
    function_notebook = tb.ref("XXXNEWtreatment_missing_values_refc_03_refactor")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook() is None
    with pytest.raises(Exception) as e_info:
        function_notebook(group) is None
    assert "takes 0 positional arguments but 1 was given" in str(e_info.value)

@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_XXXNEWtreatment_missing_values_refc_04(tb):
    function_notebook = tb.ref("XXXNEWtreatment_missing_values_refc_04")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook(group) is None
    with pytest.raises(Exception) as e_info:
        function_notebook() is None
    assert "missing 1 required positional argument" in str(e_info.value)


@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_treatment_missing_values_refc_05(tb):
    function_notebook = tb.ref("treatment_missing_values_refc_05")
    group = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
    assert function_notebook(group) is None
    with pytest.raises(Exception) as e_info:
        function_notebook() is None
    assert "missing 1 required positional argument" in str(e_info.value)


@testbook('./notebook_replace_query_with_parameter.ipynb', execute=True)
def test_treatment_missing_values_final_function(tb):
    function_notebook = tb.ref("treatment_binary")
    tb.inject("""
        df = pd.read_csv('data/dataset_mammography.csv')
    """)
    df = tb.ref("df")

    tb.inject("""
        cols_mean = ['margin', 'density', 'BI_RADS', 'shape']
    """)
    cols_mean = tb.ref("cols_mean")
    
    tb.inject("""
        cols_mode = ['age']
    """)
    cols_mode = tb.ref("cols_mode")

    tb.inject("""
        binary = 'severity'
    """)
    binary = tb.ref("binary")

    tb.inject("""
        method_f = 'mean'
    """)
    method_f = tb.ref("method_f")

    tb.inject("""
        method_f2 = 'mode'
    """)
    method_f2 = tb.ref("method_f2")

    tb.inject("""
        method_f3 = 'Cake'
    """)
    method_f3 = tb.ref("method_f3")


    result = function_notebook(
        df,
        cols_mean,
        binary,
        method_f
        )
    assert result.shape[1] == 6
    assert result.shape[0] > 0

    result = function_notebook(
        df,
        cols_mode,
        binary,
        method_f2
        )
    assert result.shape[1] == 6
    assert result.shape[0] > 0
    
    with pytest.raises(Exception) as e_info:

        result = function_notebook(
            df,
            cols_mode,
            binary,
            method_f3
        )
    assert "Method incorrect, use mean or mode" in str(e_info.value)
