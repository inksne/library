# Generated by Django 5.1.3 on 2024-11-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]