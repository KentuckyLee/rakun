from datetime import datetime
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

                result = query.execute()
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_personnel(self, d):
        try:
            print('.................personnels/services/get_personnel function called')
            if d.values() is not None:
                if d.get('id')is not None:
                    request = PersonnelsDocument.\
                        search().\
                        query(
                            Q('match_phrase', _id=d['id']) &
                            Q('match_phrase', company_id=d['company_id']) &
                            Q('match_phrase', status_id=1)
                        )
                else:
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

    def update_personnel(self, d):
        try:
            pass
        except Exception as e:
            print(e)
