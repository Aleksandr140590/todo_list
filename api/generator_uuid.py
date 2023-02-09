import random
import string

from todo.models import ToDo


class GeneratorUuid():
    """Генератор uuid."""

    def generate(self):
        """Генерация восьмизначного кода."""
        return ''.join(random.choices(
            string.ascii_letters + string.digits, k=8
        ))

    def check(self, code):
        """Проверка уникальности сгенерированного кода."""
        return ToDo.objects.filter(uuid=code).exists()

    def created(self):
        """Вывод уникального сгенерированного uuid."""
        generated = self.generate()
        while self.check(generated):
            generated = self.generate()
        return generated
