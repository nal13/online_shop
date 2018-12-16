
from pprint import pprint

from .constants import *

def validate_modelo(form):

    # False if all unidades_ fields == 0
    hasUnidades = False

    for e in form.cleaned_data.keys():
        if 'unidades_' in e:
            if form.cleaned_data[ e ] > 0:
                hasUnidades = True

    if not hasUnidades:
        return False

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
