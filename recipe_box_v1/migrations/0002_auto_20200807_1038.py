# Generated by Django 3.1 on 2020-08-07 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_box_v1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('time_required', models.CharField(max_length=15)),
                ('instruction', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_box_v1.author')),
            ],
        ),
        migrations.RemoveField(
            model_name='recipemodel',
            name='recipe_author',
        ),
        migrations.DeleteModel(
            name='AuthorModel',
        ),
        migrations.DeleteModel(
            name='RecipeModel',
        ),
    ]
