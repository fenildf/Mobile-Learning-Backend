import json
from json.decoder import JSONDecodeError

def Bool(boolValue, *args, **kwargs):
    if type(boolValue) == bool:
        return boolValue
    falseList = ['False', 'false']
    trueList = ['True', 'true']
    if boolValue in falseList:
        return False
    elif boolValue in trueList:
        return True
    else:
        raise ValueError('Invalid bool value')

def RequestParamParser(request, urlParams, *args, **kwargs):
    parsers = [
        (int, ValueError),
        (float, ValueError),
        (Bool, ValueError),
        (json.loads, JSONDecodeError)
    ]
    request.params.update(urlParams)
    for paramName in request.params:
        if type(request.params[paramName]) == str:
            parsed = None
            for parser in parsers:
                try:
                    parsed = parser[0](request.params[paramName])
                    break
                except parser[1]:
                    pass
            if parsed != None:
                request.params[paramName] = parsed