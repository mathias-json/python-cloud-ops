ec2_instances = [
    {'instance_name': 'web-prod', 'env': 'prod', 'ssh_open':True},
    {'instance_name': 'sandbox-dev', 'env': 'dev', 'ssh_open': True},
    {'instance_name': 'db-prod', 'env': 'prod', 'ssh_open': False}
]

for instance in ec2_instances:
    if instance['env'] == 'prod' and instance['ssh_open'] == True:
        instance['ssh_open'] = False
        print(instance['instance_name'])

print(ec2_instances)
