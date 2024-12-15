from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from .forms import MessageForm
from django.contrib.auth import get_user_model  

User = get_user_model() 

@login_required
def chat_list(request):
    chats = Chat.objects.filter(participants=request.user)
    processed_chats = []

    for chat in chats:
        # Get the other participant (exclude the current user)
        other_participant = chat.participants.exclude(id=request.user.id).first()
        processed_chats.append({
            'id': chat.id,
            'other_user': other_participant.username if other_participant else 'Unknown',
        })

    context = {
        'chats': processed_chats,
    }
    return render(request, 'chat/chat_list.html', context)

@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id, participants=request.user)
    messages = chat.messages.order_by('timestamp')
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.sender = request.user
            message.save()
            return redirect('chat_detail', chat_id=chat.id)

    return render(request, 'chat/chat_detail.html', {'chat': chat, 'messages': messages, 'form': form})

@login_required
def create_chat(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    chat = Chat.objects.filter(participants=request.user).filter(participants=target_user).distinct()
    if chat.exists():
        return redirect('chat_detail', chat_id=chat.first().id)

    new_chat = Chat.objects.create()
    new_chat.participants.add(request.user, target_user)
    return redirect('chat_detail', chat_id=new_chat.id)