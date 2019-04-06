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
            if d.values() is not None:
                request = ClassesDocument.\
                    search().\
                    query(
                        Q('match_phrase', status_id=1) &
                        Q('match_phrase', company_id=d['company_id'])
                    )
                results = request.execute()
                if results.hits.total != 0:
                    return results
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_class(self, d):
        try:
            if d.values() is not None:
                request = ClassesDocument. \
                    search(). \
                    query(
                        Q('match_phrase', _id=d['_id']) &
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

    def registered_student_update(self, d):
        try:
            print('...............companies/service/user_password_update function called.')
            if d.values() is not None:
                id = d['_id']
                registered_student = d['registered_student']
                update_date = datetime.now()
                client = Elasticsearch()
                response = client.update_by_query(
                    index="classes",
                    body={
                        "query": {
                            "match": {
                                "_id": id,
                            }
                        },
                        "script": {
                            "inline": "ctx._source[params.field0] = params.value0;"
                                      "ctx._source[params.field1] = params.value1;",
                            "params": {
                                "field0": "registered_student",
                                "value0": registered_student,
                                "field1": "update_date",
                                "value1": update_date,
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
