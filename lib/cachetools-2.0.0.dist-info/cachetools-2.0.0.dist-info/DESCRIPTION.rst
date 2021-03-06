cachetools
========================================================================

This module provides various memoizing collections and decorators,
including variants of the Python 3 Standard Library `@lru_cache`_
function decorator.

.. code-block:: pycon

   >>> from cachetools import LRUCache
   >>> cache = LRUCache(maxsize=2)
   >>> cache.update([('first', 1), ('second', 2)])
   >>> cache
   LRUCache([('second', 2), ('first', 1)], maxsize=2, currsize=2)
   >>> cache['third'] = 3
   >>> cache
   LRUCache([('second', 2), ('third', 3)], maxsize=2, currsize=2)
   >>> cache['second']
   2
   >>> cache['fourth'] = 4
   >>> cache
   LRUCache([('second', 2), ('fourth', 4)], maxsize=2, currsize=2)

For the purpose of this module, a *cache* is a mutable_ mapping_ of a
fixed maximum size.  When the cache is full, i.e. by adding another
item the cache would exceed its maximum size, the cache must choose
which item(s) to discard based on a suitable `cache algorithm`_.  In
general, a cache's size is the total size of its items, and an item's
size is a property or function of its value, e.g. the result of
``sys.getsizeof(value)``.  For the trivial but common case that each
item counts as ``1``, a cache's size is equal to the number of its
items, or ``len(cache)``.

Multiple cache classes based on different caching algorithms are
implemented, and decorators for easily memoizing function and method
calls are provided, too.


Installation
------------------------------------------------------------------------

Install cachetools using pip::

    pip install cachetools


Project Resources
------------------------------------------------------------------------

.. image:: http://img.shields.io/pypi/v/cachetools.svg?style=flat
   :target: https://pypi.python.org/pypi/cachetools/
   :alt: Latest PyPI version

.. image:: http://img.shields.io/travis/tkem/cachetools/master.svg?style=flat
   :target: https://travis-ci.org/tkem/cachetools/
   :alt: Travis CI build status

.. image:: http://img.shields.io/coveralls/tkem/cachetools/master.svg?style=flat
   :target: https://coveralls.io/r/tkem/cachetools
   :alt: Test coverage

- `Documentation`_
- `Issue Tracker`_
- `Source Code`_
- `Change Log`_


License
------------------------------------------------------------------------

Copyright (c) 2014-2016 Thomas Kemmer.

Licensed under the `MIT License`_.


.. _@lru_cache: http://docs.python.org/3/library/functools.html#functools.lru_cache
.. _mutable: http://docs.python.org/dev/glossary.html#term-mutable
.. _mapping: http://docs.python.org/dev/glossary.html#term-mapping
.. _cache algorithm: http://en.wikipedia.org/wiki/Cache_algorithms

.. _Documentation: http://pythonhosted.org/cachetools/
.. _Issue Tracker: https://github.com/tkem/cachetools/issues/
.. _Source Code: https://github.com/tkem/cachetools/
.. _Change Log: https://github.com/tkem/cachetools/blob/master/CHANGES.rst
.. _MIT License: http://raw.github.com/tkem/cachetools/master/LICENSE


