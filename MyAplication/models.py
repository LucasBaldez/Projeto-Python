from django.conf import settings
from django.db import models
from django.utils import timezone

class Fornecedores(models.Model):
    CodigoFornecedor = models.AutoField(primary_key=True)
    NomeFornecedor = models.CharField(max_length=100)
    EmailFornecedor = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.NomeFornecedor