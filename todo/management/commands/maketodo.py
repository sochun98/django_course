from django.core.management import BaseCommand
from todo.models import Todo
from random import choice
import sys

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 101):
            # Todo.objects.create(name=f"테스트 todo {i}", complete=choice([True, False]))
            # todo = Todo.objects.create(name=f"테스트 todo {i}")
            todo, created = Todo.objects.get_or_create(name=f"테스트 todo {i}")
            if created:
                print(f"{i}번째 todo 생성 완료")
            else:
                print(f"{i}번째 todo 이미 존재")
        
        sys.stdout.write(self.style.SUCCESS("make todo end :)"))