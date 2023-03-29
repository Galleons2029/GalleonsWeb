from django.shortcuts import render

from .models import Topic
# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries.
    The function accepts the value captured by the expression /<int:topic_id>/
    and assigns it to topic_id.
    """
    topic = Topic.objects.get(id=topic_id)   # retrieve the topic
    entries = topic.entry_set.order_by('-date_added')
    # sign"-" sorts the results in reverse order,
    # display the most recent entries first.
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
