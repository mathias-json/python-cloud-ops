ec2_instances = [
    {'instance_name': 'web-prod', 'env': 'prod', 'ssh_open':True},
    {'instance_name': 'sandbox-dev', 'env': 'dev', 'ssh_open': True},
    {'instance_name': 'db-prod', 'env': 'prod', 'ssh_open': False}
]

def audit_ec2_fleet(fleet_list):
    for instance in fleet_list:
        if instance['env'] == 'prod' and instance['ssh_open'] == True:
            instance['ssh_open'] = False
            print(instance['instance_name'])
    return fleet_list

secured_fleet = audit_ec2_fleet(ec2_instances)
print(secured_fleet)

