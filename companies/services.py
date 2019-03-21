from rakun_elastic.document import TestCompaniesDocument
from elasticsearch_dsl.query import Q
from datetime import datetime
from dateutil.relativedelta import relativedelta


class CompaniesService():

    def save_company(self, d):

        try:
            d['credits'] = 3
            d['credits_price'] = 0
            d['credits_price_date'] = datetime.now()
            d['credits_expiration_date'] = datetime.now() + relativedelta(months=+1)
            d['created_date'] = datetime.now()
            d['update_date'] = datetime.now()
            d['status_id'] = 1
            new_company = TestCompaniesDocument(**d)
            new_company.save()
            return new_company
        except Exception as e:
            print(e)


    def get_active_companies_count(self, d):

        try:
            query = TestCompaniesDocument. \
                search(). \
                query(
                Q('match_phrase', mail=d['mail']) |
                Q('match_phrase', phone_number=d['phone_number']) &
                Q('match_phrase', status=1))
            results = query.execute()
            return results
        except Exception as e:
            print(e)

    def get_company(self, doc_id):
        try:
            company = TestCompaniesDocument().search().filter('ids', values=doc_id)
            print('...........company type: ', type(company))
            print('...........company: ', company)
            result = company.execute()
            for hits in result:
                print('.....................bura ne laaa: ', hits.company)
            print('............company execute: ', result.__dict__)

            print('............get_company bitti')
            return result
        except Exception as e:
            print(e)
    #
    # {
    #   '_search': < django_elasticsearch_dsl.search.Search # object # at  # 0x04E56B30 >,
    #   '_doc_class': None,
    #   '_d_': {
    #     'took': 1,
    #     'timed_out': False,
    #     '_shards': {
    #         'total': 1,
    #         'successful': 1,
    #         'skipped': 0,
    #         'failed': 0
    #     },
    #     'hits': {
    #         'total': 0,
    #         'max_score': None,
    #         'hits': []
    #     }
    #   },
    # '_hits': [],
    # '_aggs': {}
    # }


    # new_company = TestCompaniesDocument(
    #                 phone_number=phone_number,
    #                 company_id=phone_number,
    #                 company=company,
    #                 owner_name=owner_name,
    #                 owner_surname=owner_surname,
    #                 mail=mail,
    #                 credit=credit,
    #                 credits_price=credits_price,
    #                 credits_price_date=credits_price_date,
    #                 credits_expiration_date=credits_expiration_date,
    #                 country='undefined',
    #                 city='undefined',
    #                 district='undefined',
    #                 created_date=created_date,
    #                 update_date=update_date,
    #                 status=2
    #             )
    #             new_company.save()
