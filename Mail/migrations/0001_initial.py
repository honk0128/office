# Generated by Django 3.2.18 on 2023-04-17 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Document', '0001_initial'),
        ('Emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('Mail_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Mail_Title', models.CharField(max_length=50)),
                ('Mail_contents', models.CharField(max_length=500)),
                ('Mail_Create_Time', models.DateTimeField(auto_now=True)),
                ('Mail_Isread', models.BooleanField(default=False)),
                ('Mail_Docs', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Document.document')),
                ('Mail_Files', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Document.file')),
                ('Mail_Receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Mail_Reciever', to='Emp.employee')),
                ('Mail_Sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Mail_Sender', to='Emp.employee')),
            ],
        ),
    ]
