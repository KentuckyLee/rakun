from rakun_elastic.document import TestUsersDocument
from elasticsearch_dsl.query import Q
from elasticsearch import Elasticsearch
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime
from system_mails.system_mails import Sys_Mails
import hashlib


class UsersService():

    def save_user(self, d):
        try:
            d['password'] = BaseUserManager().make_random_password(6)
            d['created_date'] = datetime.now()
            d['update_date'] = datetime.now()
            d['status_id'] = 2
            new_user = TestUsersDocument(**d)
            new_user.save()
            send_mail = Sys_Mails()
            send_mail.owner_first_record(d['mail'], d['phone_number'], d['password'])
            return new_user
        except Exception as e:
            print(e)

    def get_user_status(self,d):
        try:
            query = TestUsersDocument().\
                search().\
                query(
                    Q('match_phrase', phone_number=d['phone_number']) &
                    Q('match_phrase', password=d['password']) |
                    Q('match_phrase', password=hashlib.md5(d['password'].encode('utf8')).hexdigest())
            )
            response = query.execute()
            result = []
            for i in response:
                result.append(i.status_id)
                result.append(i.phone_number)
                result.append(i.company_id)
            return result
        except Exception as e:
            print(e)
    def user_password_update(self, d):
        try:
            password = hashlib.md5(d['password'].encode('utf8')).hexdigest()
            company_id = d['company_id']
            phone_number = d['phone_number']
            update_date = datetime.now()
            client = Elasticsearch()
            response = client.update_by_query(
                index="test_users",
                body={
                    "query": {
                        "bool": {
                            "must": [
                                {"match": {"phone_number": phone_number}},
                                {"match": {"company_id": company_id}}
                            ]
                        }
                    },
                    "script": {
                        "inline": "ctx._source[params.field0] = params.value0;"
                                  "ctx._source[params.field1] = params.value1;"
                                  "ctx._source[params.field2] = params.value2;",
                        "params": {
                            "field0": "password",
                            "value0": password,
                            "field1": "status_id",
                            "value1": 1,
                            "field2": "update_date",
                            "value2": update_date,
                        },
                    }
                },
            )
            return response['updated']
        except Exception as e:
            print(e)

