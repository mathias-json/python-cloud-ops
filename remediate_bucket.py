s3_buckets = [
    {'bucket_name': 'public-assets', 'public_access': True},
    {'bucket_name': 'customer-records', 'public_access': True}
]

s3_buckets[1]['public_access'] = False
print(s3_buckets[1])
