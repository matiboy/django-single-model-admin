DJANGO SINGLE MODEL ADMIN
===

[![PyPI Version](https://img.shields.io/pypi/v/singlemodeladmin.svg)][pypi]
[![Build Status](http://img.shields.io/travis/AMeng/django-single-model-admin.svg)][travis]

[travis]: http://travis-ci.org/AMeng/django-single-model-admin
[pypi]: https://pypi.python.org/pypi/singlemodeladmin

A subclass of Django's ModelAdmin for use with models that are only meant to have one record. This is useful for things like site-wide settings

Usage:
---

Subclass `SingleModelAdmin` instead of Django's `ModelAdmin`

```python
from singlemodeladmin import SingleModelAdmin

class MyModelAdmin(SingleModelAdmin):
    list_display = [ ... ]
    search_fields = [ ... ]
```

Installation:
---
```
pip install singlemodeladmin
```

Behavior:
---

- If there is only one object, the changelist will redirect to that object.
- If there are no objects, the changelist will redirect to the add form.
- If there are multiple objects, the changelist is displayed with a warning
- Attempting to add a new record when there is already one will result in a warning and a redirect away from the add form.
