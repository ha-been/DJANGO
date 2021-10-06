# Generated by Django 3.2.7 on 2021-10-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinemas',
            fields=[
                ('cine_id', models.AutoField(primary_key=True, serialize=False)),
                ('cine_name', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('current_movies', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'cinemas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('member_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('member_pw', models.CharField(blank=True, max_length=255, null=True)),
                ('member_name', models.CharField(blank=True, max_length=255, null=True)),
                ('member_tel', models.CharField(blank=True, max_length=255, null=True)),
                ('resident_num', models.CharField(blank=True, max_length=255, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('like_genre', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'members',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(blank=True, max_length=255, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('actor', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=255, null=True)),
                ('age_limit', models.CharField(blank=True, max_length=255, null=True)),
                ('story', models.TextField(blank=True, null=True)),
                ('open_date', models.DateField(blank=True, null=True)),
                ('close_date', models.DateField(blank=True, null=True)),
                ('poster_src', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'movies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieSchedules',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('cine_name', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_name', models.CharField(blank=True, max_length=255, null=True)),
                ('house_num', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_time', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie_schedules',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MymovieRe',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('re_pw', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('cont', models.TextField(blank=True, null=True)),
                ('like_genre', models.CharField(blank=True, max_length=255, null=True)),
                ('bip', models.CharField(blank=True, max_length=255, null=True)),
                ('bdate', models.DateTimeField(blank=True, null=True)),
                ('readcnt', models.IntegerField(blank=True, null=True)),
                ('gnum', models.IntegerField(blank=True, null=True)),
                ('onum', models.IntegerField(blank=True, null=True)),
                ('nested', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mymovie_re',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nonmembers',
            fields=[
                ('nm_id', models.AutoField(primary_key=True, serialize=False)),
                ('nm_birth', models.DateField(blank=True, null=True)),
                ('nm_tel', models.CharField(blank=True, max_length=255, null=True)),
                ('nm_pw', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'nonmembers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('ticket_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ticket_date', models.DateTimeField(blank=True, null=True)),
                ('cine_name', models.CharField(blank=True, max_length=255, null=True)),
                ('seat', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tickets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TicketsNm',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_date', models.DateTimeField(blank=True, null=True)),
                ('cine_name', models.CharField(blank=True, max_length=255, null=True)),
                ('seat', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_id', models.IntegerField(blank=True, null=True)),
                ('movie_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tickets_nm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Voc',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('voc_pw', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('cont', models.TextField(blank=True, null=True)),
                ('voc_type', models.CharField(blank=True, max_length=255, null=True)),
                ('bip', models.CharField(blank=True, max_length=255, null=True)),
                ('bdate', models.DateTimeField(blank=True, null=True)),
                ('readcnt', models.IntegerField(blank=True, null=True)),
                ('gnum', models.IntegerField(blank=True, null=True)),
                ('onum', models.IntegerField(blank=True, null=True)),
                ('nested', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'voc',
                'managed': False,
            },
        ),
    ]
