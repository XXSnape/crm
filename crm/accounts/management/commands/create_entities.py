from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from crm.config import config


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.filter(username=config.USERS.ADMIN_USERNAME).exists():
            return
        User.objects.create_superuser(
            username=config.USERS.ADMIN_USERNAME,
            password=config.USERS.ADMIN_PASSWORD,
        )
        operators_group = Group(name="operators")
        marketers_group = Group(name="marketers")
        managers_group = Group(name="managers")
        Group.objects.bulk_create([operators_group, marketers_group, managers_group])

        operator_permissions = Permission.objects.filter(
            codename__in=["add_lead", "change_lead", "delete_lead", "view_lead"]
        )
        marketer_permissions = Permission.objects.filter(
            codename__in=[
                "add_product",
                "change_product",
                "delete_product",
                "view_product",
                "add_ads",
                "change_ads",
                "delete_ads",
                "view_ads",
            ]
        )

        manager_permissions = Permission.objects.filter(
            codename__in=[
                "add_contract",
                "change_contract",
                "delete_contract",
                "view_contract",
                "add_customer",
                "change_customer",
                "delete_customer",
                "view_customer",
            ]
        )
        operators_group.permissions.set(operator_permissions)
        marketers_group.permissions.set(marketer_permissions)
        managers_group.permissions.set(manager_permissions | operator_permissions)
        operator = User(
            username=config.USERS.OPERATOR_USERNAME,
            password=make_password(config.USERS.OPERATOR_PASSWORD),
        )
        marketer = User(
            username=config.USERS.MARKETER_USERNAME,
            password=make_password(config.USERS.MARKETER_PASSWORD),
        )
        manager = User(
            username=config.USERS.MANAGER_USERNAME,
            password=make_password(config.USERS.MANAGER_PASSWORD),
        )
        User.objects.bulk_create([operator, marketer, manager])
        operator.groups.add(operators_group)
        marketer.groups.add(marketers_group)
        manager.groups.add(managers_group)
