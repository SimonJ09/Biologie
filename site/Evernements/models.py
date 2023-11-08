from django.db import models

class Evenement(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='evenements/pdfs/', null=True, blank=True)
    pdf = models.FileField(upload_to='evenements/photos/', null=True, blank=True)
    date_debut = models.DateTimeField(null=True, blank=True)
    date_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nom

