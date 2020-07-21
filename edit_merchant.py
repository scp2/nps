#!/usr/bin/python
import requests
import json

# Variaveis para conexão a API gsurf propig.
endpoint_prod = 'https://sc3.gsurfnet.com/api'
ws_key_propig_prod = '9ae5bc76-e126-6c77-8f39-3eaa10d6b2bf'
headers_default = {'Content-Type': 'aplication/json',
                   'ws_key': ws_key_propig_prod}


def get_token(endpoint_prod, headers_default):
    response = requests.get(endpoint_prod+'/token', headers=headers_default)
    token = json.loads(response.content)
    headers = {'Content-Type': 'aplication/json',
               'ws_key': ws_key_propig_prod, 'ws_token': str(token['token'])}
    return headers


def get_merchants(endpoint_prod, headers):
    response = requests.get(endpoint_prod+'/merchants', headers=headers)
    response_content = json.loads(response.content)
    return response_content['merchant']


def edit_merchant(endpoint_prod, headers, merchant):
    response = requests.put(endpoint_prod+'/merchants/'+str(merchant['id']) +
                            '?flow_type=2', headers=headers)
    return response.status_code


if __name__ == "__main__":
    headers = get_token(endpoint_prod, headers_default)
    merchants = get_merchants(endpoint_prod, headers)
    for i in merchants:
        print('Atualizando lojista '+i['name'] + ' ' + i['cnpj'])
        print('Status', edit_merchant(endpoint_prod, headers, i))
    pass
