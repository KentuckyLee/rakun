from django_elasticsearch_dsl import DocType, Index
from loginorregister.models import Test

test = Index('emretest')
test.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@test.doc_type
class TestDocument(DocType):
    class Meta:
        model = Test

        fields = [
            'phone_number',
            'company',
            'password',
            'owner',
            'mail',
            'credit',
            'credits_price',
            'credits_price_date',
            'credits_expiration_date',
            'image_url',
            'country',
            'city',
            'district',
            'created_date',
            'status',
        ]