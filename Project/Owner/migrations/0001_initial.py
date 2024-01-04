# Generated by Django 4.1.5 on 2023-02-07 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0002_ownerreg'),
        ('Admin', '0015_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rentdet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rentname', models.CharField(max_length=50)),
                ('details', models.TextField(null=True)),
                ('image', models.FileField(upload_to='Ownerphoto/')),
                ('amount', models.CharField(max_length=50, null=True)),
                ('vstatus', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.ownerreg')),
                ('renttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.renttype')),
            ],
        ),
    ]
