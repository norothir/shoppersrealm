import django_tables2 as tables
from ostokset.models import Ostos

class OstosTable(tables.Table):
    class meta:
        model = Ostos
        attrs = {"class": "paleblue"}
        
        