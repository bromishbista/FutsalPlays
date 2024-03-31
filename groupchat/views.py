from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import UserGroups, Message
from .form import GroupChatForm

from django.http import JsonResponse
from .models import *

def group_chat(request, group_id):
    group = get_object_or_404(UserGroups, pk=group_id)
    messages = Message.objects.filter(sender__in=group.users.all())
    return render(request, 'group_chat.html', {'group': group, 'messages': messages})



def post_message(request, group_id):
    group = get_object_or_404(UserGroups, pk=group_id)
    form = GroupChatForm(request.POST)
    if form.is_valid():
        message = Message(sender=request.user, content=form.cleaned_data['message'])
        message.save()
        group.messages.add(message)
    return redirect('group_chat', group_id=group_id)

