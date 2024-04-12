from itertools import groupby
from collections import UserDict, defaultdict
from icecream import ic

def run():
    permissions: list[str] = [
        "auth.view_user",
        "contenttypes.view_contenttype",
        "admin.change_logentry",
        "auth.change_group",
        "admin.delete_logentry",
        "auth.add_permission",
        "auth.change_permission",
        "sessions.change_session",
        "customers.change_customer",
        "auth.view_permission",
        "contenttypes.delete_contenttype",
        "auth.delete_user",
        "contenttypes.add_contenttype",
        "customers.delete_customer",
        "auth.view_group",
        "auth.add_group",
        "auth.change_user",
        "customers.view_customer",
        "sessions.view_session",
        "auth.add_user",
        "sessions.add_session",
        "admin.add_logentry",
        "customers.add_customer",
        "auth.delete_permission",
        "admin.view_logentry",
        "auth.delete_group",
        "contenttypes.change_contenttype",
        "sessions.delete_session",
    ]

    default_perms: dict[str, int] = {
        'view': 8,
        'add': 4,
        'change': 2,
        'delete': 1,
    }

    perms_dict: dict[str, list[str]] =  {}
    for p in permissions:
        model, perm = p.split('.')
        perm = perm.split('_')[0]
        perm = default_perms[perm]
        perms_dict[model] = perms_dict.get(model, []) + [perm]

    ic(perms_dict)
