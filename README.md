# django-forgiving-collectstatic

An extension of the `django.contrib.staticfiles.storage.ManifestStaticFilesStorage` that skips missing files and assets during the `python manage.py collectstatic` command run.

## Installation

Use pip:

```shell
pip install django-forgiving-collectstatic
```

## Usage

Set in your `settings.py`:

```python
STATICFILES_STORAGE = 'django_forgiving_collectstatic.storages.ForgivingManifestStaticFilesStorage'
```

## Credits

Contributed by [Tim Kamanin](https://timonweb.com).
