# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-13 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import scholarships.models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0006_auto_20170211_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='eligibilityrequirement',
            name='daca_required',
            field=models.BooleanField(default=False, verbose_name='DACA Required?'),
        ),
        migrations.AddField(
            model_name='eligibilityrequirement',
            name='state',
            field=models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('DC', 'Washington DC')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='amount',
            field=scholarships.models.ScholarshipAmountField(default=0, help_text='Enter the max award amount or 0 for UNKNOWN or 1 for FULL TUITION', verbose_name='Award Amount ($)'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='deadline',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='description',
            field=models.TextField(blank=True, help_text='Short description about the scholarship and any additional requirements'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='status',
            field=models.IntegerField(choices=[(0, 'ARCHIVED'), (1, 'UNVERIFIED'), (2, 'VERIFIED')], default=1, help_text='VERIFIED - Active and verified. UNVERIFIED - Active but not verified. ARCHIVED - Not active.', verbose_name='Scholarship Status'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='website',
            field=models.URLField(blank=True, help_text='Website URL for full scholarship details'),
        ),
    ]
