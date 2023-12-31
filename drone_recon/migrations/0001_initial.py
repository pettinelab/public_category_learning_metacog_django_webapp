# Generated by Django 3.1.8 on 2023-03-02 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_trials', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('session_completed', models.BooleanField(default=False)),
                ('questionnaire_completed', models.BooleanField(default=False)),
                ('task_completed', models.BooleanField(default=False)),
                ('tutorial_completed', models.BooleanField(default=False)),
                ('total_reward', models.IntegerField(default=0)),
                ('total_payment', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('payment_issued', models.BooleanField(default=False)),
                ('final_performance', models.DecimalField(decimal_places=5, max_digits=6, null=True)),
                ('payment_token', models.CharField(max_length=40)),
                ('external_study_ID', models.CharField(default='', max_length=100)),
                ('external_session_ID', models.CharField(default='', max_length=100)),
                ('strategy', models.CharField(default='', max_length=1000)),
                ('strategy_radio', models.CharField(default='', max_length=30)),
                ('perceived_difficulty', models.CharField(default='', max_length=10)),
                ('task', models.CharField(default='', max_length=100)),
                ('substances', models.JSONField(blank=True, default=list, null=True)),
                ('sleep_quality', models.IntegerField(blank=True, null=True)),
                ('sleep_quantity', models.IntegerField(blank=True, null=True)),
                ('passed_attention_check', models.BooleanField(default=False)),
                ('project', models.CharField(default='', max_length=40)),
                ('timezone', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stimulus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('use', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_ID', models.CharField(max_length=64)),
                ('external_source', models.CharField(max_length=64)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.CharField(default='', max_length=20)),
                ('gender', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=20)),
                ('is_bot', models.BooleanField(default=False)),
                ('psych_history', models.JSONField(blank=True, default=list, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=2)),
                ('confidence', models.FloatField(blank=True, default=None, null=True)),
                ('reward', models.BooleanField(null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('block', models.CharField(max_length=100)),
                ('reward_probs_record', models.JSONField(default=dict)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trials', to='drone_recon.session')),
                ('stimulus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trials', to='drone_recon.stimulus')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='drone_recon.subject'),
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prolific_study_id', models.CharField(default='', max_length=100)),
                ('time', models.DateTimeField()),
                ('task', models.CharField(default='', max_length=100)),
                ('notes', models.CharField(default='', max_length=1000)),
                ('source', models.CharField(default='', max_length=100)),
                ('accepted', models.BooleanField(default=None, null=True)),
                ('session', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruitment', to='drone_recon.session')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recruitment', to='drone_recon.subject')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionnaireQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionnaire_name', models.CharField(max_length=100)),
                ('subscale', models.CharField(blank=True, max_length=100, null=True)),
                ('possible_answers', models.JSONField(default=dict)),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.IntegerField()),
                ('questionnaire_question_number', models.IntegerField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_q', to='drone_recon.session')),
            ],
        ),
    ]
