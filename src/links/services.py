import string
import random
from links.models import Link

def generate_short_code(length=6, max_attempts=10):
    chars = string.ascii_letters + string.digits
    attempts = 0
    while attempts < max_attempts:
        code = ''.join(random.choices(chars, k=length))
        if not Link.objects.filter(short_code=code).exists():
            return code
        attempts += 1
    return generate_short_code(length=length + 1)

