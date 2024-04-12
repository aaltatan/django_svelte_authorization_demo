from ninja import Router
from .models import Customer
from typing import List
from ninja.security import django_auth, django_auth_superuser
from .schemas import CustomerSchemaOut
from django.http import HttpRequest
from core.permissions import SessionAuthHasPerms, Perms, only_for


has = Perms()
router = Router(tags=["customers"])


@router.get("/", response=List[CustomerSchemaOut])
def get_all_customers(request: HttpRequest):
    return Customer.objects.all()


@router.get("/admin-only", auth=django_auth_superuser)
def admin_only_route(request: HttpRequest):
    return {"admin": "this message will appear only for admins"}


@router.get(
    "/has-param-only", 
    auth=SessionAuthHasPerms(
        permissions_list=only_for('customer', has.VIEW | has.ADD)
    )
)
def has_param_only_route(request: HttpRequest):
    return {"has_param": "this message will appear only for has_param"}


@router.get("/authenticated-only", auth=django_auth)
def authenticated_only_route(request: HttpRequest):
    return {"authenticated": "this message will appear only for authenticated users"}


