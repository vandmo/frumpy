import sys
import yaml

with open('petstore.yaml') as f:
    parsed = yaml.load(f)

valid = True
for path in parsed['paths']:
    if '{' in path or '}' in path:
        print(f'Found curly brackets in {path}')
        valid = False
    for method in parsed['paths'][path]:
        if method != 'post':
            print(f'Invalid method {method} for path {path}')
            valid = False

if not valid:
    print('API is NOT frumpy')
    sys.exit(-1)
