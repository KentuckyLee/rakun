from rakun_elastic.document import CompaniesDocument
from elasticsearch_dsl.query import Q
from datetime import datetime
from dateutil.relativedelta import relativedelta


class CompaniesService(object):

    def save_company(self, d):
        print('.................companies/services/ save_company function called')
        try:
            if d.values() is not None:
                d['credits'] = 3
                d['credits_price'] = 0
                d['credits_price_date'] = datetime.now()
                d['credits_expiration_date'] = datetime.now() + relativedelta(months=+1)
                d['created_date'] = datetime.now()
                d['update_date'] = datetime.now()
                d['status_id'] = 1
                new_company = CompaniesDocument(**d)
                save = new_company.save()
                if save:
                    return new_company
                else:
                    raise Exception('error while company registering')
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)


    def get_all_company(self, d):
        try:
            print('..............companies/services/ get_all_company function called')
            if d.values() is not None:
                query = CompaniesDocument. \
                    search(). \
                    query(
                        Q('match_phrase', mail=d['mail']) |
                        Q('match_phrase', phone_number=d['phone_number']) &
                        Q('match_phrase', status=1))
                results = query.execute()
                if results.hits.total != 0:
                    return results
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

