# Generated by Django 4.2.13 on 2025-07-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0008_library_alter_book_options_remove_book_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add book'), ('can_change_book', 'Can change book'), ('can_delete_book', 'Can delete book')]},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_library',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Unknown Author', max_length=100),
        ),
        migrations.AddField(
            model_name='library',
            name='location',
            field=models.CharField(default='Unknown Location', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='No bio'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='library',
            name='name',
            field=models.CharField(default='Default Library', max_length=100),
        ),
    ]
