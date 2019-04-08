from rakun_elastic.document import StudentDocument
from elasticsearch_dsl.query import Q
from datetime import datetime


class StudentService(object):

    def save_student(self, d):
        print('...............students/service/save_student function called.')
        try:
            if d.values() is not None:
                d['status_id'] = 1
                d['image_url'] = 'undefined'
                d['student_height'] = 0
                d['student_weight'] = 0
                d['created_date'] = datetime.now()
                d['update_date'] = datetime.now()
                new_student = StudentDocument(**d)
                save = new_student.save()
                if save:
                    return new_student
                else:
                    raise Exception('error while student registering')
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_all_student(self, d):
        print('...............students/service/get_all_student function called.')
        try:
            if d.values() is not None:
                request = StudentDocument.\
                    search().\
                    query(
                        Q('match_phrase', status_id=1) &
                        Q('match_phrase', company_id=d['company_id'])
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

    def find_by_id(self, d):
        try:
            print('...............students/service/find_by_id function called.')
            if d.values() is not None:
                query = StudentDocument.\
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

    def find_by_parent_id_and_company_id(self, d):
        try:
            print('.................Student/services/find_by_parent_id_and_company_id function called')
            if d.values() is not None:
                request = StudentDocument. \
                    search(). \
                    query(
                        Q('match_phrase', parent_id=d['parent_id']) &
                        Q('match_phrase', company_id=d['company_id']) &
                        Q('match_phrase', status_id=1)
                    )
                result = request.execute()
                print(result)
                if result.hits.total != 0:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def personnel_students(self, d):
        try:
            print('.................parents/services/personnel_students function called')
            if d.values() is not None:
                result = list()
                print('d: ', d)
                for class_room in d['class_room']:
                    request = StudentDocument.\
                        search().\
                        query(
                            Q('match_phrase', class_room=class_room) &
                            Q('match_phrase', company_id=d['company_id']) &
                            Q('match_phrase', status_id=1)
                        )
                    result.append(request.execute())
                    print('pers_student: ', result)
                if result is not None:
                    return result
                else:
                    return None
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)