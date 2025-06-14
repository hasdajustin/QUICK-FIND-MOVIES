import pandas as pd
from django.core.management.base import BaseCommand
from core.models import Movie

class Command(BaseCommand):
    msg = "import movies form excel"

    def handle(self, *args, **kwargs):
        df = pd.read_excel("movies.xlsx")
        for _, row in df.iterrows():
            Movie.objects.update_or_create(
                title = row["title"],
                defaults = {
                    'genre': row['genre'],
                    'year': int(row['year']),
                    'director': row['director'],
                    'country': row['country'],
                }
            )
        self.stdout.write(self.style.SUCCESS("movies imorted successfully!"))