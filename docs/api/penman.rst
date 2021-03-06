
penman
======

.. automodule:: penman

For basic usage, and to retain some backward compatibility with early
versions, some functionality is available from the top-level
:mod:`penman` module. For the rest, please use the standard API
available via the submodules.

.. _submodules:

Submodules
----------

Data Structures
'''''''''''''''

- :doc:`penman.epigraph` -- Base classes for epigraphical markers
- :doc:`penman.graph` -- Classes for pure graphs
- :doc:`penman.model` -- Class for defining semantic models
- :doc:`penman.models` -- Pre-defined models
- :doc:`penman.surface` -- Classes for surface alignments
- :doc:`penman.tree` -- Classes for trees

Serialization
'''''''''''''

- :doc:`penman.codec` -- Codec class for reading and writing PENMAN data
- :doc:`penman.layout` -- Conversion between trees and graphs
- :doc:`penman.lexer` -- Low-level parsing of PENMAN data

Other
'''''

- :doc:`penman.exceptions` -- Exception classes
- :doc:`penman.interface` -- Functional interface to a codec
- :doc:`penman.transform` -- Graph and tree transformation functions


Module Constants
----------------

.. data:: penman.__version__

   The software version string.

.. data:: penman.__version_info__

   The software version as a tuple.


Classes
-------

.. class:: Triple

   Alias of :exc:`penman.graph.Triple`.

.. class:: Graph

   Alias of :exc:`penman.graph.Graph`.

.. class:: PENMANCodec

   Alias of :exc:`penman.codec.PENMANCodec`.


Module Functions
----------------

.. function:: decode

   Alias of :exc:`penman.interface.decode`.

.. function:: loads

   Alias of :exc:`penman.interface.loads`.

.. function:: load

   Alias of :exc:`penman.interface.load`.

.. function:: encode

   Alias of :exc:`penman.interface.encode`.

.. function:: dumps

   Alias of :exc:`penman.interface.dumps`.

.. function:: dump

   Alias of :exc:`penman.interface.dump`.


Exceptions
----------

.. exception:: PenmanError

   Alias of :exc:`penman.exceptions.PenmanError`.

.. exception:: DecodeError

   Alias of :exc:`penman.exceptions.DecodeError`.
