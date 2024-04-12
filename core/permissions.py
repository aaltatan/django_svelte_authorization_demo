from typing import Any, Optional
from django.conf import settings
from django.http import HttpRequest
from ninja.security.apikey import APIKeyCookie
from dataclasses import dataclass


@dataclass
class Perms:
    VIEW: int = 8
    ADD: int = 4
    CHANGE: int = 2
    DELETE: int = 1


class SessionAuthHasPerms(APIKeyCookie):
    "Reusing Django session authentication"

    def __init__(self, csrf: bool = True, permissions_list: list[str] = []) -> None:
        super().__init__(csrf)
        self.permissions_list = permissions_list

    param_name: str = settings.SESSION_COOKIE_NAME

    def authenticate(self, request: HttpRequest, key: Optional[str]) -> Optional[Any]:
        has_perm: bool = request.user.has_perms(self.permissions_list)
        if request.user.is_authenticated and has_perm:
            return request.user

        return None
    

def only_for(
    single_name: str,
    permissions: int = 15,
    app_name: str | None = None,
    default_perms: list[str] = ["view", "add", "change", "delete"]
) -> list[str]:
    """ generate a list of django's model authorization """

    if app_name is None:
        app_name = single_name + "s"

    decimal: list[int] = [
      int(n) for n in list(bin(permissions)[2:].rjust(len(default_perms), "0"))
    ]

    return [
        f"{app_name}.{perm}_{single_name}"
        for dec, perm in zip(decimal, default_perms)
        if dec
    ]
