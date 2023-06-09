# Generated by Django 4.1.7 on 2023-05-09 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smash_note', '0004_favoritecharacter_delete_favoritecharacter2'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCharacterCharacters',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smash_note.character')),
                ('favoritecharacter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smash_note.favoritecharacter')),
            ],
            options={
                'db_table': 'smash_note_favoritecharacter_characters',
            },
        ),
        migrations.AlterField(
            model_name='favoritecharacter',
            name='characters',
            field=models.ManyToManyField(blank=True, through='smash_note.FavoriteCharacterCharacters', to='smash_note.character'),
        ),
    ]
