import random
import string

from todo.models import Todo


class GeneratorUuid():

    def generate(self):
        return ''.join(random.choices(
            string.ascii_letters + string.digits, k=8
        ))

    def check(self, code):
        return Todo.objects.filter(uuid=code).exists()

    def created(self):
        generated = self.generate()
        while self.check(generated):
            generated = self.generate()
        return generated
