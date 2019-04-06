from rakun_elastic.document import NotificationsDocument
from elasticsearch_dsl.query import Q
from datetime import datetime


class NotificationService(object):

    def save_notification(self, d):
        try:
            print('.................notifications/services/save_notification function called')
            if d.values() is not None:
                d['is_read'] = 0
                d['created_date'] = datetime.now()
                save_notification = NotificationsDocument(**d).save()
                if save_notification:
                    return True
                else:
                    raise Exception('error while notification registering')
            else:
                raise Exception('dictionary is null')
        except Exception as e:
            print(e)

    def get_all_notifications(self):
        try:
            print('.................notifications/services/save_notification function called')
            query = NotificationsDocument.search().sort('-created_date')
            result = query.execute()
            print(result)
            if result.hits.total != 0:
                return result[0:5]
            else:
                return None
        except Exception as e:
            print(e)
