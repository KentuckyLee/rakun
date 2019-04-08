from datetime import datetime
from rakun_elastic.document import ClassesDocument
from elasticsearch_dsl.query import Q
from elasticsearch import Elasticsearch


class ClassService(object):

    def save_class(self, d):
        print('.................classes/services/save_class function called')
        try:
            if d.values() is not None:
                d['status_id'] = 1
                d['created_date'] = datetime.now()
                d['update_date'] = datetime.now()
                d['registered_student'] = 0
                new_class = ClassesDocument(**d)
                save = new_class.save()
                if save:
                    return new_class
                else:
                    raise Exception('error while class registering')
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_all_class(self, d):
        try:
            print('.................classes/services/get_all_class function called')
            print('d', d)
            if d.values() is not None:
                request = ClassesDocument.\
                    search().\
                    query(
                        Q('match_phrase', status_id=1) &
                        Q('match_phrase', company_id=d['company_id'])
                    )
                results = request.execute()
                print('result: ', results)
                if results.hits.total != 0:
                    return results
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def find_by_id(self, d):
        try:
            print('.................classes/services/find_by_id function called')
            if d.values() is not None:
                request = ClassesDocument.search().query(Q('match_phrase', _id=d['id']))
                result = request.execute()
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def update(self, d):
        try:
            print('.................classes/services/update function called')
            if d.values() is not None:
                class_id = d['id']
                update_date = datetime.now()
                d['update_date'] = update_date
                doc = {'doc': d}
                client = Elasticsearch()
                response = client.update(index='classes', id=class_id, body=doc, doc_type='doc')
                if response['_shards']['successful'] != 0:
                    return True
                else:
                    return False
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)