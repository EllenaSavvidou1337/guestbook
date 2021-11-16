# Generated by Django 3.2.8 on 2021-10-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='mustermann', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='leave',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]