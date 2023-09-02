import pytest
from testbook import testbook

@testbook('./notebookApp.ipynb', execute=True)
def test_tratar_ausentes(tb):
    tratar_ausentes = tb.ref("tratar_ausentes")
    lista = ['BI-RADS', 'Idade', 'Forma', ' Margem', ' Densidade', 'Severidade']
    assert tratar_ausentes() == None


