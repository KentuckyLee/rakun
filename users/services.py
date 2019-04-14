from rakun_elastic.document import UsersDocument
from elasticsearch_dsl.query import Q
from elasticsearch import Elasticsearch
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime
from system_mails.system_mails import Sys_Mails
import hashlib


class UsersService(object):

    def save_user(self, d):
        print('...............UsersService/service/save_user function called.')
        try:
            if d.values() is not None:
                password = BaseUserManager().make_random_password(6)
                d['password'] = hashlib.md5(password.encode('utf8')).hexdigest()
                d['created_date'] = datetime.now()
                d['update_date'] = datetime.now()
                d['status_id'] = 2
                new_user = UsersDocument(**d)
                save = new_user.save(id=d['id'])
                if save:
                    send_mail = Sys_Mails()
                    mail = send_mail.owner_first_record(d['mail'], d['phone_number'], password)
                    if mail:
                        return new_user
                    else:
                        raise Exception('error while sending password mail')
                else:
                    raise Exception('error while user registering')
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def login(self, d):
        print('...............companies/service/login function called.')
        try:
            # None control
            if d.values() is not None:
                if d['authorization_type'] == '1':
                    category_id = [3, 0, 0]
                    print('category: ', category_id)
                    print('d:', d)
                    print('password:', hashlib.md5(d['password'].encode('utf8')).hexdigest())
                else:
                    category_id = [1, 2, 4]
                query = UsersDocument. \
                    search(). \
                    query(
                        Q('match_phrase', phone_number=d['phone_number']) &
                        Q('match_phrase', password=hashlib.md5(d['password'].encode('utf8')).hexdigest()) &
                        (
                                Q('match', category_id=category_id[0]) |
                                Q('match', category_id=category_id[1]) |
                                Q('match', category_id=category_id[2])
                        )
                    )
                print('query: ', query.__dict__)
                result = query.execute()
                print('user result: ', result)
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_all_user(self, d):
        print('...............companies/service/get_all_user function called.')
        try:
            # None control
            if d.values() is not None:
                query = UsersDocument. \
                    search(). \
                    query(
                        Q('match_phrase', company_id=d['company_id']) &
                        Q('match_phrase', status_id=1)
                    )
                result = query.execute()
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_all_personnel(self, d):
        print('...............companies/service/get_personnel_user function called.')
        try:
            # None control
            if d.values() is not None:
                query = UsersDocument. \
                    search(). \
                    query(
                        Q('match_phrase', company_id=d['company_id']) &
                        Q('match_phrase', category_id=2) &
                        Q('match_phrase', status_id=1)
                    )
                result = query.execute()
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_all_parent(self, d):
        print('...............companies/service/get_all_parent function called.')
        try:
            # None control
            if d.values() is not None:
                query = UsersDocument. \
                    search(). \
                    query(
                        Q('match_phrase', company_id=d['company_id']) &
                        Q('match_phrase', category_id=3) &
                        Q('match_phrase', status_id=1)
                    )
                result = query.execute()
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_user(self, d):
        print('...............companies/service/get_user function called.')
        try:
            # None control
            if d.values() is not None:
                if d['authorization_type'] == '1':
                    category_id = [3, 0, 0]
                else:
                    category_id = [1, 2, 4]
                query = UsersDocument. \
                    search().\
                    query(
                         Q('match_phrase', phone_number=d['phone_number']) &
                         Q('match_phrase', category_id=category_id[0]) |
                         Q('match_phrase', category_id=category_id[1]) |
                         Q('match_phrase', category_id=category_id[2])
                    )
                result = query.execute()
                print('user result: ', result)
                if result.hits.total != 0:
                   return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def find_by_id(self, d):
        try:
            print('...............companies/service/get_user_find_by_id function called.')
            if d.values() is not None:
                request = UsersDocument.search().query(Q('match_phrase', _id=d['id']))
                result = request.execute()
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def user_password_update(self, d):
        try:
            print('...............companies/service/user_password_update function called.')
            if d.values() is not None:
                password = hashlib.md5(d['password'].encode('utf8')).hexdigest()
                company_id = d['company_id']
                phone_number = d['phone_number']
                update_date = datetime.now()
                client = Elasticsearch()
                response = client.update_by_query(
                    index="users",
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
                if response['updated'] != 0:
                    return response['updated']
                else:
                    return False
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def update(self, d):
        try:
            print('...............companies/service/update_user function called.')
            if d.values() is not None:
                update_date = datetime.now()
                d['update_date'] = update_date
                doc = {'doc': d}
                client = Elasticsearch()
                response = client.update(index='users', id=d['id'], doc_type='doc', body=doc)
                if response['_shards']['successful'] != 0:
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
