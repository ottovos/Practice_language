from django.db import models

# Create your models here.

class Language(models.Model):
    language_text=models.CharField(max_length=200)

    def __str__(self):
        return self.language_text

class Words(models.Model):
    word_text=models.CharField(max_length=200)
    meaning_text = models.CharField(max_length=200)
    language_word = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.word_text







