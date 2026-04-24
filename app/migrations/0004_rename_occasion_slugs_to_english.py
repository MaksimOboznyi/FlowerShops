from django.db import migrations


OCCASION_SLUG_RENAMES = {
    'svadba': 'wedding',
    'den-rozhdeniya': 'birthday',
    'bez-povoda': 'no_reason',
}


def rename_forward(apps, schema_editor):
    Occasion = apps.get_model('app', 'Occasion')
    for old_slug, new_slug in OCCASION_SLUG_RENAMES.items():
        Occasion.objects.filter(slug=old_slug).update(slug=new_slug)


def rename_backward(apps, schema_editor):
    Occasion = apps.get_model('app', 'Occasion')
    for old_slug, new_slug in OCCASION_SLUG_RENAMES.items():
        Occasion.objects.filter(slug=new_slug).update(slug=old_slug)


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_bouquet_height_bouquet_width'),
    ]

    operations = [
        migrations.RunPython(rename_forward, rename_backward),
    ]
