iam_user = {
    'username': 'admin-dave',
    'mfa_enabled': False
}

if iam_user['mfa_enabled'] == False:
    print('Security Alert: MFA is disabled! Enforcing MFA now...')
    iam_user['mfa_enabled'] = True

print(iam_user)