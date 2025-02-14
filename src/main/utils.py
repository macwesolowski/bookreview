import os
from django.utils.text import slugify


def book_cover_upload_path(instance, filename):
    book_slug = slugify(instance.tytul)
    ext = os.path.splitext(filename[1])
    return f'books/{book_slug}/cover{ext}'
