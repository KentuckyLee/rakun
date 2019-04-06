from django.shortcuts import render
from Context.ContextView import Authantication
from notifications.service import NotificationService

# Create your views here.

def index(request):
    try:
        print('...............dashboard/views/index function called.')
        context = Authantication.getInstance().getUser()
        notifications = NotificationService().get_all_notifications()
        print('notif: ', notifications)
        context['notifications'] = notifications
        context['page'] = ''
        return render(request, 'rakun/layout.html', context)
    except Exception as e:
        print(e)
