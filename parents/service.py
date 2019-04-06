from rakun_elastic.document import ParentDocument
from elasticsearch_dsl.query import Q
from datetime import datetime


class ParentService(object):

    def save_parent(self, d):
        try:
            print('.................parents/services/save_parent function called')
            if d.values() is not None:
                d['status_id'] = 1
                d['created_date'] = datetime.now()
                d['update_date'] = datetime.now()
                new_parent = ParentDocument(**d).save()
                if new_parent:
                    return new_parent
                else:
                    raise Exception('error while parent registering')
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_all_parent(self, d):
        try:
            print('.................parents/services/get_all_parent function called')
            if d.values() is not None:
                request = ParentDocument.\
                    search().\
                    query(
                        Q('match_phrase', status_id=1) &
                        Q('match_phrase', company_id=d['company_id'])
                    )
                result = request.execute()
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_parent(self, d):
        try:
            print('.................parents/services/get_parent function called')
            if d.values() is not None:
                if d.get('id') is not None:
                    request = ParentDocument.\
                        search().\
                        query(
                            Q('match_phrase', _id=d['id']) &
                            Q('match_phrase', company_id=d['company_id']) &
                            Q('match_phrase', status_id=1)
                        )
                else:
                    request = ParentDocument. \
                        search(). \
                        query(
                            Q('match_phrase', phone_number=d['phone_number']) &
                            Q('match_phrase', company_id=d['company_id']) &
                            Q('match_phrase', status_id=1)
                    )
                result = request.execute()
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)
