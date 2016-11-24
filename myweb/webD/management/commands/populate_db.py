from django.core.management.base import BaseCommand
from webD.models import AllArticles

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):
        newarticle = AllArticles(Name='Pfaffian systems of A-hypergeometric equations I', Link='http://www.sciencedirect.com/science/article/pii/S0001870816314153')
        newarticle.save()

    def handle(self, *args, **options):
        self._create_tags()
