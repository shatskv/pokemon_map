# Generated by Django 3.1.14 on 2022-07-26 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20220722_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='for_pokemon', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]