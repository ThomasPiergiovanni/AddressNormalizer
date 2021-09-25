""" DB management command
"""
from django.core.management.base import BaseCommand

from normalizer.management.engine.normalizer_manager import NormalizerManager



class Command(BaseCommand):
    """ Normalize address string
    """
    help = "Normalize address string"

    def __init__(self):
        super().__init__()
        self.normalizer_manager = NormalizerManager()

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.normalizer_manager.normalize()