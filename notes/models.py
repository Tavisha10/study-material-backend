from django.db import models

class StudyMaterial(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title