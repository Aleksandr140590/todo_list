import random
import string

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from todo.models import Todo


class Generator_uuid():

    def generate(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    def check(self, code):
        return Todo.objects.filter(uuid=code).exists()

    def created(self):
        generated = self.generate()
        while self.check(generated):
            generated = self.generate()
        return generated


generator = Generator_uuid()


class CreateTodoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('text', 'uuid')
        read_only_fields = ('uuid', 'created', 'active')
        model = Todo

    def create(self, validated_data):
        return Todo.objects.create(**validated_data, uuid=generator.created())


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'








