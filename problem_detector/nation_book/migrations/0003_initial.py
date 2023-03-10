# Generated by Django 4.1.5 on 2023-03-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nation_book', '0002_delete_problems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=200)),
                ('problem_desc', models.CharField(max_length=500)),
                ('problem_img', models.ImageField(upload_to='problem_img')),
                ('problem_id', models.IntegerField(default=0)),
            ],
        ),
    ]
