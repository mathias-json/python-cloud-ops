# create a dictionary of keys

cloud_blueprint = {'service', 'tier', 'encrypted'}

def deploy_service(service, tier, encrypted):
    if encrypted == True:
        print('launching with encryption enabled')

deploy_service(**cloud_blueprint)

