web_server = {
    'name': 'nimbus',
    'instance_type': 't2.micro',
    'region': 'eu-west-1',
    'is_encrypted': False
}

web_server['is_encrypted'] = True
web_server['port'] = 443

print(web_server)
