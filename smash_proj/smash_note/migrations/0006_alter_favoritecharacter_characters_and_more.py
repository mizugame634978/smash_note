# Generated by Django 4.1.7 on 2023-05-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smash_note', '0005_favoritecharactercharacters_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecharacter',
            name='characters',
            field=models.ManyToManyField(blank=True, to='smash_note.character'),
        ),
        migrations.DeleteModel(
            name='FavoriteCharacterCharacters',
        ),
    ]
