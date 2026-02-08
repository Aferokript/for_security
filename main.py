import os
from tkinter.font import names

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard


def print_active_key():
    active_passcards = Passcard.objects.filter(is_active=True)
    return active_passcards.count()

def main():
    key = print_active_key()

    print(f'Количество активных пропусков: {key}')
    print('Количество пропусков:', Passcard.objects.count())

if __name__ == '__main__':
    main()