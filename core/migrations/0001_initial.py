# Generated by Django 2.1.7 on 2019-03-09 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtype', models.CharField(choices=[('PP', 'Passport'), ('ID', 'Identity card'), ('OT', 'Others')], max_length=2)),
                ('doc_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='documents',
            field=models.ManyToManyField(to='core.Document'),
        ),
    ]
