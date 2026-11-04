security_group = {
    'group_name': 'web_firewall',
    'open_ports': [22, 80, 443]
}

security_group['open_ports'].remove(80)
security_group['open_ports'].append(8443)

print(security_group)