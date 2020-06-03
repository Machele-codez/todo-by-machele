# Generated by Django 2.2.7 on 2020-06-01 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField(default=False)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('A', 'critical'), ('B', 'high'), ('C', 'moderate'), ('D', 'low')], max_length=15)),
                ('due_datetime', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.AddConstraint(
            model_name='task',
            constraint=models.UniqueConstraint(fields=('user', 'text'), name='unique_user_task'),
        ),
    ]
