from django_elasticsearch_dsl import DocType, Index
from loginorregister.models import TestCompanies

test_companies = Index('test_companies')
test_companies.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@test_companies.doc_type
class TestCompaniesDocument(DocType):

    class Meta:
        model = TestCompanies

        fields = [
            'phone_number',
            'company',
            # 'password',
            'owner_name',
            'owner_surname',
            'mail',
            'credit',
            'credits_price',
            'credits_price_date',
            'credits_expiration_date',
            # 'image_url',
            'country',
            'city',
            'district',
            'created_date',
            'update_date',
            'status'
        ]