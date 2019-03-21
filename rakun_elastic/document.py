from django_elasticsearch_dsl import DocType, Index
from companies.models import TestCompanies
from personnel.models import TestPersonnel
from notifications.models import TestNotifications
from users.models import TestUsers


test_companies = Index('test_companies')
test_companies.settings(
    number_of_shards=1,
    number_of_replicas=0
)

test_users = Index('test_users')
test_companies.settings(
    number_of_shards=1,
    number_of_replicas=0
)

test_personnel = Index('test_personnel')
test_personnel.settings(
    number_of_shards=1,
    number_of_replicas=0
)

test_notifications = Index('test_notifications')
test_notifications.settings(
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
            'user_name',
            'user_surname',
            'mail',
            'credits',
            'credits_price',
            'credits_price_date',
            'credits_expiration_date',
            'created_date',
            'update_date',
            'status_id'
        ]

@test_users.doc_type
class TestUsersDocument(DocType):

    class Meta:
        model = TestUsers

        fields = [
            'company_id',
            'company',
            'phone_number',
            'password',
            'category_id',
            'user_name',
            'user_surname',
            'mail',
            'created_date',
            'update_date',
            'status_id'


        ]

@test_personnel.doc_type
class TestPersonnelDocument(DocType):

    class Meta:
        model = TestPersonnel

        fields = [

            # Personnel data

            'user_name',
            'user_surname',
            'mail',
            'image_url',
            'birth_date',
            'address',
            'university',
            'domain',
            'language',
            'graduated_date',

            # Personnel authenticate data

            'phone_number',
            'password',
            'company_id',
            'company',
            'class_room',
            'position',
            'category',
            'status',
            'created_date',
            'update_date'
        ]

    # def get_personnel_data(self, ids):
    #
    #     query_object = TestPersonnelDocument.search().filter('ids', values=self.ids)  # id ye sahip personel dokumanı sorgulanıyor
    #     query = query_object.execute()  # personel dataları oluşturuluyor
    #     for per_data in query:
    #         per_data
    #     personnel_data = {
    #         'id': self.ids,
    #         'page': 'Personel',
    #         'user_name': per_data.user_name,
    #         'user_surname': per_data.user_surname,
    #         'mail': per_data.mail,
    #         'image_url': per_data.image_url,
    #         'birth_date': per_data.birth_date,
    #         'address': per_data.address,
    #         'university': per_data.university,
    #         'domain': per_data.domain,
    #         'language': per_data.language,
    #         'graduated_date':per_data.graduated_date,
    #
    #         # Personnel authenticate data
    #         'phone_number': per_data.phone_number,
    #         'password': per_data.phone_number,
    #         'company_id': per_data.company_id,
    #         'company': per_data.company,
    #         'class_room': per_data.class_room,
    #         'position': per_data.position,
    #         'category': per_data.category,
    #         'status': per_data.status,
    #         'created_date': per_data.created_date,
    #         'update_date': per_data.update_date
    #     }
    #     return personnel_data


@test_notifications.doc_type
class TestNotificationsDocument(DocType):
    class Meta:
        model = TestNotifications

        fields = [
            'created_user',
            'assigned_user',
            'company',
            'content',
            'is_read',
            'created_date'
        ]