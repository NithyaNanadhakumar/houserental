# Generated by Django 4.1.5 on 2023-02-20 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_ownerreg'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.userreg')),
            ],
        ),
    ]
