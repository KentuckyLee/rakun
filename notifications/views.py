from django.shortcuts import render
from Context.ContextView import Authantication
from notifications.forms import SendNotificationForm
from notifications.service import NotificationService
from users.services import UsersService
from django.contrib import messages

__ALL_USERS = '1'
__ALL_PERSONNEL = '2'
__ALL_PARENT = '3'

def index(request):
    try:
        pass
    except Exception as e:
        print(e)

def send_notifications(request):
    try:
        context = Authantication.getInstance().getUser()
        notification_form = SendNotificationForm(data=request.POST or None, request=request.COOKIES.get('company_id'))
        if notification_form.is_valid():
            form_data = notification_form.cleaned_data
            assigned_user_list = list()
            for i in form_data['user_list']:
                if i == __ALL_USERS:
                    get_users = UsersService().get_all_user({'company_id': request.COOKIES.get('company_id')})
                    for u in get_users:
                        assigned_user_list.append(u.meta.id)
                    break
                elif i == __ALL_PERSONNEL:
                    get_users = UsersService().get_all_personnel({'company_id': request.COOKIES.get('company_id')})
                    for u in get_users:
                        assigned_user_list.append(u.meta.id)
                elif i == __ALL_PARENT:
                    get_users = UsersService().get_all_parent({'company_id': request.COOKIES.get('company_id')})
                    for u in get_users:
                        assigned_user_list.append(u.meta.id)
                else:
                    assigned_user_list.append(i)
            data = {
                'created_user_id': context['user_id'],
                'assigned_user_id': assigned_user_list,
                'company_id': request.COOKIES.get('company_id'),
                'content': form_data['text']
            }
            send_notification = NotificationService().save_notification(data)
            if send_notification:
                messages.success(request, 'Bildiriminiz başarıyla gönderilmiştir.')
            else:
                messages.warning(request, 'Teknik bir hata oluştu.')
        context['send_notifications_form'] = notification_form
        return render(request, 'rakun/notifications/send_notifications.html', context)
    except Exception as e:
        print(e)
