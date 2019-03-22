from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'

# class PollsConfig(AppConfig):
#     name = 'polls.python.path.to.your.app.polls'
#     label = 'my.polls'  # <-- this is the important line - change it to anything other than the default, which is the module name ('foo' in this case)