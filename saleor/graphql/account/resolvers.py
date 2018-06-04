from ...account import models


def resolve_users(info):
    return models.User.objects.all()
