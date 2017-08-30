
import sys
sys.path.append('/usr/local/aws/lib/python2.7/site-packages')
import boto3
import json

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
#    for obj in bucket.objects.all():
        print('{0}'.format(bucket.name))
