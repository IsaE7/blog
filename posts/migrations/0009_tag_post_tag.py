# Generated by Django 5.0.7 on 2024-08-11 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_category_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='posts.tag'),
        ),
    ]
