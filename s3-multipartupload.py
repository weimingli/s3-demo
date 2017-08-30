import sys
sys.path.append('/usr/local/aws/lib/python2.7/site-packages')

import os
import math
import functools
import logging
import socket
import threading
import random
import string
import boto3
from boto3.s3.transfer import *

client = boto3.client('s3', 'cn-north-1')

config = TransferConfig(
    multipart_threshold=20 * 1024 * 1024,
    max_concurrency=50,
    num_download_attempts=10,
)

class Progress_callback():

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
    def __call__(self, bytes_amount):

            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            print("\r%s  %s / %s  (%.2f%%)" % (self._filename, self._seen_so_far, self._size, percentage))

transfer = S3Transfer(client,config)

transfer.upload_file('/Users/weiminl/testfile1G', 'demo', 'testfile1G', callback=Progress_callback('/Users/weiminl/testfile1G'))

#transfer.upload_file('/Users/weiminl/testfile10M', 'demo', 'testfile10M', callback=Progress_callback('/Users/weiminl/testfile10M'))
#transfer._multipart_upload('/Users/weiminl/testfile1G', 'demo', 'testfile1G', callback=Progress_callback('/Users/weiminl/testfile1G'),extra_args={})