from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

from users.models import CustomUser
from catalog.models import Product


class Command(BaseCommand):
    help = 'Creating a user group and adding a user to the group'

    def handle(self, *args, **kwargs):
        user_email = 'plussa-les@mail.ru'
        user = CustomUser.objects.get(email=user_email)
        content_type = ContentType.objects.get_for_model(Product)
        unpublish_perm = Permission.objects.get(codename='can_unpublish_product', content_type=content_type)
        delete_perm = Permission.objects.get(codename='can_delete_product', content_type=content_type)
        product_moderators, created = Group.objects.get_or_create(name='Product_moderators')

        if created and user:
            product_moderators.permissions.add(unpublish_perm, delete_perm)
            user.groups.add(product_moderators)
            self.stdout.write(self.style.SUCCESS(f'Successfully created group {product_moderators.name}, added to the group user {user_email}'))
        else:
            self.stdout.write(self.style.WARNING(f'Group {product_moderators.name} already exists or user {user_email} not found.'))

