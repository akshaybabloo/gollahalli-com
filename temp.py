# from __future__ import print_function
# from django.utils.crypto import get_random_string
#
# chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
# SECRET_KEY = get_random_string(50, chars)
#
# print(SECRET_KEY)
# print(''.join(str(x) for x in range(10)))


# import bibtexparser
#
# with open('gollahalli/static/static_dirs/my_papers.bib') as bibtex_file:
#     bibtex_str = bibtex_file.read()
#
# bib_database = bibtexparser.loads(bibtex_str)
# print(bib_database.entries_dict)

# import feedparser
# data = feedparser.parse("https://blog.gollahalli.com/rss")
#
# for a in data.entries:
#     print(a['tags'])

# import phonenumbers
# from authy.api import AuthyApiClient
# email_id = 'akshaybabloo@gmail.com'
# phone_number = '+64210393363'
#
# phone_number = phonenumbers.parse(str(phone_number))
# authy_api = AuthyApiClient('Tf4gloeNvezlEPVF52Vm9p2BEU19Pj3t')
# authy_user = authy_api.users.create(email_id, phone_number.national_number, phone_number.country_code)
# {'user': {'id': 44474079}, 'success': True, 'message': 'User created successfully.'}

# authy_user = authy_api.phones.info(phone_number.national_number, phone_number.country_code) {'carrier': 'Telecom
# New Zealand (Spark)', 'message': 'Text message sent to +64 21-039-3363.', 'uuid':
# '6dadca60-49f8-0135-346b-0e5d6a065904', 'is_cellphone': True, 'success': True, 'seconds_to_expire': 599}

# authy_user = authy_api.phones.verification_start(phone_number.national_number, phone_number.country_code,
# via='sms') {'carrier': 'Telecom New Zealand (Spark)', 'message': 'Text message sent to +64 21-039-3363.',
# 'uuid': '6dadca60-49f8-0135-346b-0e5d6a065904', 'is_cellphone': True, 'success': True, 'seconds_to_expire': 599}

# authy_user = authy_api.phones.verification_check(phone_number.national_number, phone_number.country_code, 2172)
# {'message': 'Verification code is correct.', 'success': True}

# authy_user = authy_api.phones.verification_check(phone_number.national_number, phone_number.country_code, 2172)
# {'message': 'No pending verifications for +64 21-039-3363 found.', 'success': False, 'errors': {'message': 'No
# pending verifications for +64 21-039-3363 found.'}, 'error_code': '60023'}

# authy_user = authy_api.apps.fetch()
# {'message': 'Application information.', 'app': {'plan': 'pay_as_you_go',
# 'app_id': 65257, 'name': 'Gollahalli', 'sms_enabled': True, 'onetouch_enabled': True, 'phone_calls_enabled': True},
#  'success': True}

# authy_user = authy_api.stats.fetch()
# {'app_id': 65257, 'message': 'Monthly statistics.', 'success': True, 'total_users': 1, 'stats': [{'year': 2017,
# 'month': 'June', 'auths_count': 9, 'api_calls_count': 266, 'users_count': 1, 'sms_count': 2, 'calls_count': 0},
# {'year': 2017, 'month': 'July', 'auths_count': 2, 'api_calls_count': 2801, 'users_count': 1, 'sms_count': 0,
# 'calls_count': 0}], 'count': 2}

# print(authy_user.content)

# a = {'a': 2}
# import dj_database_url
#
# print(dj_database_url.config(conn_max_age=500))

# import boto3
# from botocore.exceptions import ClientError
# import os
# from pprint import pprint
#
# os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAIMLZILBL5GVGIODA'
# os.environ['AWS_SECRET_ACCESS_KEY']='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'
#
# # pprint(dict(os.environ))
#
# session = boto3.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID', 'a'),
#                         aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY', 'a'))
# s3 = session.client('s3')
#
# for bucket_list in s3.list_buckets()['Buckets']:
#     bucket_list['Name']
