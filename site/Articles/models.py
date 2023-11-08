from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.TextField()
    categorie = models.TextField()
    lien = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='articles/photos/', null=True, blank=True)
    pdf = models.FileField(upload_to='articles/pdfs/',null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modification = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.titre

