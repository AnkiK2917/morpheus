# Generated by Django 5.1.4 on 2024-12-30 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='required',
        ),
        migrations.AddField(
            model_name='formfield',
            name='options',
            field=models.TextField(blank=True, help_text='Comma-separated options for checkbox/radio.'),
        ),
        migrations.AlterField(
            model_name='customform',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('text', 'Text Input'), ('textarea', 'Textarea'), ('checkbox', 'Checkbox'), ('radio', 'Radio Button')], max_length=20),
        ),
    ]