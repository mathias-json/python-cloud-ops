s3_buckets = [
    {'bucket_name': 'prod-data', 'public_access': True},
    {'bucket_name': 'app-logs', 'public_access': False},
    {'bucket_name': 'user-uploads', 'public_access': True}
]

for bucket in s3_buckets:
    if bucket['public_access'] == True:
        bucket['public_access'] = False
        print(bucket['bucket_name'])

print(s3_buckets)

# STORAGE ACCESS
# Day 5 - for loop
