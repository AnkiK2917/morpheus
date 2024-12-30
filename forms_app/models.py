from django.db import models

class CustomForm(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FormField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text Input'),
        ('textarea', 'Textarea'),
        ('checkbox', 'Checkbox'),
        ('radio', 'Radio Button'),
    ]

    form = models.ForeignKey(CustomForm, related_name='fields', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)
    options = models.TextField(blank=True, help_text="Comma-separated options for checkbox/radio.")

    def __str__(self):
        return self.label
