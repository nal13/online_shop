
from pprint import pprint

from .constants import *

def validate_modelo(form):

    # False if nome exists
    query = g.exists_modelo_name( form.cleaned_data['nome'] )

    for e in query['results']['bindings']:
        if e['exists_nome']['value'] == 'true':
            pprint('FALSE')
            return False

    pprint('TRUE')
    return True     # if not catch in any validation => True


def validate_loja(form):

    # False if nome exists
    query = g.exists_loja_name( form.cleaned_data['nome'] )

    for e in query['results']['bindings']:
        if e['exists_nome']['value'] == 'true':
            pprint('FALSE')
            return False

    pprint('TRUE')
    return True     # if not catch in any validation => True
