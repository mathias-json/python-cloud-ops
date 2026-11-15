import json

# a raw json string downloaded from AWS
raw_json_input = '[{"instance_name": "api-prod", "env": "prod", "ssh_open": true}]'

# Unpack the json string text

parsed_fleet = json.loads(raw_json_input)
parsed_fleet = audit_ec2_fleet(parsed_fleet)


