import json
import os.path as osp

DIR_RES = 'res'
DIR_DIST = 'dist'
SCHEMA_NAME = 'schema'

def generate_scheme(name):
    schema = f'{DIR_RES}/{SCHEMA_NAME}.json'
    new_theme = f'{DIR_RES}/{name}.json'
    
    if not osp.exists(schema):
        raise FileNotFoundError(f'SCHEMA not found {schema}')
    if not osp.exists(new_theme):
        raise FileNotFoundError(f'new scheme config not found {new_theme}')
    
    with open(schema, 'r') as s:
        with open(new_theme, 'r') as f:
            schema = json.load(s)
            theme = json.load(f)
            d = {k:v for k, v in zip(schema, theme)}
            json.dump(d, open(f'{DIR_DIST}/{name}.json', 'w'))

if __name__ == '__main__':
    generate_scheme('macos')