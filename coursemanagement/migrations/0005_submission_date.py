# Generated by Django 4.1.6 on 2023-03-08 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coursemanagement', '0004_rename_due_date_assignment_deadline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]