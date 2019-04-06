from django_elasticsearch_dsl import DocType, Index
from companies.models import Companies
from personnel.models import Personnels
from classes.models import Classes
from users.models import Users
from parents.models import Parents
from students.models import Students
from notifications.models import Notifications

parents = Index('parents')
parents.settings(
    number_of_shards=1,
    number_of_replicas=0
)

student = Index('students')
student.settings(
    number_of_shards=1,
    number_of_replicas=0
)

classes = Index('classes')
classes.settings(
    number_of_shards=1,
    number_of_replicas=0
)

companies = Index('companies')
companies.settings(
    number_of_shards=1,
    number_of_replicas=0
)

users = Index('users')
users.settings(
    number_of_shards=1,
    number_of_replicas=0
)

personnels = Index('personnels')
personnels.settings(
    number_of_shards=1,
    number_of_replicas=0
)

notifications = Index('notifications')
notifications.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@student.doc_type
class StudentDocument(DocType):

    class Meta:
        model = Students

        fields = [
            'student_name',
            'student_surname',
            'parent_id',
            'parent',
            'class_name',
            'class_id',
            'image_url',
            'student_birth_date',
            'company_id',
            'company',
            'private_student',
            'student_height',
            'student_weight',
            'student_note',
            'status_id',
            'created_date',
            'update_date',
        ]


@parents.doc_type
class ParentDocument(DocType):

    class Meta:
        model = Parents

        fields = [
            'user_name',
            'user_surname',
            'phone_number',
            'mail',
            'birth_date',
            'company_id',
            'company',
            'category_id',
            'students_count',
            'status_id',
            'created_date',
            'update_date',
        ]

@companies.doc_type
class CompaniesDocument(DocType):

    class Meta:
        model = Companies

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
            'status_id',
        ]

@users.doc_type
class UsersDocument(DocType):

    class Meta:
        model = Users

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


@classes.doc_type
class ClassesDocument(DocType):

    class Meta:
        model = Classes

        fields = [
            'company_id',
            'class_name',
            'quota',
            'registered_student',
            'status_id',
            'created_date',
            'update_date',
        ]

@personnels.doc_type
class PersonnelsDocument(DocType):

    class Meta:
        model = Personnels

        fields = [

            # Personnel data

            'user_name',
            'user_surname',
            'mail',
            'image_url',
            'birth_date',
            'address',
            'university',

            # Personnel authenticate data

            'phone_number',
            'company_id',
            'company',
            'class_room',
            'personnel_type',
            'category_id',
            'status_id',
            'created_date',
            'update_date'
        ]


@notifications.doc_type
class NotificationsDocument(DocType):
    class Meta:
        model = Notifications

        fields = [
            'created_user_id',
            'assigned_user_id',
            'company_id',
            'content',
            'is_read',
            'created_date'
        ]
