
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_auto_20200828_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='savers',
            field=models.ManyToManyField(blank=True, related_name='saved', to=settings.AUTH_USER_MODEL),
        ),
    ]
