import sys
import yaml

with open('petstore.yaml') as f:
    parsed = yaml.load(f)

valid = True


def invalid(message):
    print(message)
    valid = False


def validate_operation(operation):
    operation_id = operation['operationId']
    if not 'produces' in operation:
        invalid(f'Missing produces: application/json for operation {operation_id}')
    else:
        if len(operation['produces']) != 1:
            invalid(f'Operation {operation_id}, should only contain one media type')
        else:
            if operation['produces'][0] != 'application/json':
                invalid(f'Invalid media type for operation {operation_id}, should be application/json')
    if not 'consumes' in operation:
        invalid(f'Missing consumes: application/json for operation {operation_id}')
    else:
        if len(operation['consumes']) != 1:
            invalid(f'Operation {operation_id}, should only contain one media type')
        else:
            if operation['consumes'][0] != 'application/json':
                invalid(f'Invalid media type for operation {operation_id}, should be application/json')
    parameters = operation['parameters']
    if len(parameters) != 1 or parameters[0]['in'] != 'body':
        invalid(f'Operation {operation_id} should have exactly one parameter, the body parameter')
    else:
        parameter = parameters[0]
        if parameter['name'] != 'body':
            invalid(f'For operation {operation_id}: the body parameter should be named "body"')
        if not parameter['required']:
            invalid(f'For operation {operation_id}: the body parameter should be required')
        schema = parameter['schema']

    responses = operation['responses']
    if len(responses) != 1 or (200 not in responses and '200' not in responses):
        invalid(f'For operation {operation_id}: there should be exactly one response, the 200 response')
        

for path in parsed['paths']:
    if '{' in path or '}' in path:
        print(f'Found curly brackets in {path}')
        valid = False
    for method in parsed['paths'][path]:
        if method != 'post':
            print(f'Invalid method {method} for path {path}')
            valid = False
        else:
            validate_operation(parsed['paths'][path]['post'])

if not valid:
    print('API is NOT frumpy')
    sys.exit(-1)
