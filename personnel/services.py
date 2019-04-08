from datetime import datetime

from elasticsearch import Elasticsearch

from rakun_elastic.document import PersonnelsDocument
from elasticsearch_dsl.query import Q


class PersonnelService(object):

    def save_personnel(self, d):
        try:
            print('.................personnels/services/get_all_personnels function called')
            if d.values() is not None:
                d['status_id'] = 1
                d['image_url'] = 'undefined'
                d['category_id'] = 2
                d['created_date'] = datetime.now()
                d['update_date'] = datetime.now()
                new_personnel = PersonnelsDocument(**d)
                save = new_personnel.save()
                if save:
                    return new_personnel
                else:
                    raise Exception('error while user registering')
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def find_by_id(self, d):
        try:
            print('.................personnels/services/find_by_id function called')
            if d.values() is not None:
                request = PersonnelsDocument.search().query(Q('match_phrase', _id=d['id']))
                result = request.execute()
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_all_personnels(self, d):
        try:
            print('.................personnels/services/get_all_personnels function called')
            if d.values() is not None:
                query = PersonnelsDocument.\
                    search().\
                    query(
                        Q('match_phrase', status_id=1) &
                        Q('match_phrase', company_id=d['company_id'])
                    )
                count = query.count()
                result = query[0:count].execute()
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def find_by_phone_number_and_company_id(self, d):
        try:
            print('.................personnels/services/find_by_phone_number_and_company_id function called')
            if d.values() is not None:
                request = PersonnelsDocument. \
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

    def update(self, d):
        try:
            print('.................personnels/services/find_by_phone_number_and_company_id function called')
            if d.values() is not None:
                id = d['id']
                update_date = datetime.now()
                d['update_date'] = update_date
                doc = {'doc': d}
                client = Elasticsearch()
                response = client.update(index='personnels', id=id, body=doc, doc_type='doc')
                print('sonuç: ', response['_shards']['successful'])
                if response['_shards']['successful'] != 0:
                    return True
                else:
                    return False
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)