# Generated by Django 4.0.6 on 2024-08-30 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('Image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.BigIntegerField()),
                ('email_id', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('Speciality', models.CharField(max_length=50)),
                ('About', models.TextField(null=True)),
                ('DOB', models.CharField(max_length=50)),
                ('Image', models.ImageField(null=True, upload_to='images/')),
                ('Department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.department')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(editable=False, max_length=20, null=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.IntegerField(null=True)),
                ('DOB', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(null=True)),
                ('blood_gp', models.CharField(max_length=50, null=True)),
                ('note', models.TextField(null=True)),
                ('medicines', models.TextField(null=True)),
                ('number_of_session', models.CharField(max_length=50, null=True)),
                ('Followup', models.CharField(max_length=100, null=True)),
                ('Proposedtreatmentplan', models.CharField(max_length=100, null=True)),
                ('Treatment', models.CharField(max_length=100, null=True)),
                ('Srothusinvolved', models.CharField(max_length=100, null=True)),
                ('Dhathupredominence', models.CharField(max_length=100, null=True)),
                ('Doshapredominence', models.CharField(max_length=100, null=True)),
                ('Amanirama', models.CharField(max_length=100, null=True)),
                ('Regularmedications', models.CharField(max_length=100, null=True)),
                ('PastMedicalandsurgicalhistory', models.CharField(max_length=100, null=True)),
                ('Historyofpresentingcomplaints', models.CharField(max_length=100, null=True)),
                ('Presentingcomplaints', models.CharField(max_length=100, null=True)),
                ('Menstrualhistory', models.CharField(max_length=100, null=True)),
                ('Allergies', models.CharField(max_length=100, null=True)),
                ('Sleep', models.CharField(max_length=100, null=True)),
                ('Digestion', models.CharField(max_length=100, null=True)),
                ('Clinicaldetails', models.CharField(max_length=100, null=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.admin')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomNumber', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Treatment', models.CharField(max_length=50)),
                ('Department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.department')),
            ],
        ),
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Therapy', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.BigIntegerField()),
                ('email_id', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('Room', models.CharField(max_length=50, null=True)),
                ('About', models.TextField(null=True)),
                ('Image', models.ImageField(null=True, upload_to='media/images/')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.admin')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.therapy')),
                ('treatment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.treatment')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Note', models.TextField(null=True)),
                ('Date', models.DateField()),
                ('number_of_session', models.IntegerField()),
                ('starting_Time', models.TimeField()),
                ('ending_Time', models.TimeField()),
                ('Therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.therapist')),
                ('Therapy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.therapy')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.admin')),
                ('patientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.patient')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.status')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.status'),
        ),
        migrations.AddField(
            model_name='patient',
            name='therapy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.therapy'),
        ),
        migrations.AddField(
            model_name='patient',
            name='treatment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.treatment'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Lid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.login'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.admin'),
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField()),
                ('reg_time', models.TimeField()),
                ('about', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.doctor')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.admin')),
                ('patientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.patient')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.status')),
                ('treatment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.treatment')),
            ],
        ),
        migrations.AddField(
            model_name='admin',
            name='Lid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.login'),
        ),
        migrations.CreateModel(
            name='SessionStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_number', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('attended', 'Attended')], default='pending', max_length=50)),
                ('session_date', models.DateField(blank=True, null=True)),
                ('starting_Time', models.TimeField(blank=True, null=True)),
                ('ending_Time', models.TimeField(blank=True, null=True)),
                ('session_group', models.IntegerField()),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='Booking.schedule')),
            ],
            options={
                'unique_together': {('schedule', 'session_number')},
            },
        ),
    ]