FileTypes
=========

.. py:class:: FileTypes


   Bases: :py:class:`object`


Cython implementation of _FileTypes


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FileTypes.html




.. py:method:: FileTypes.nameToType


Cython signature: FileType nameToType(String name)


Converts a file type name into a Type
-----
:param name: A case-insensitive name (e.g. FASTA or Fasta, etc.)




.. py:method:: FileTypes.typeToMZML


Cython signature: String typeToMZML(FileType t)
Returns the mzML name




.. py:method:: FileTypes.typeToName


Cython signature: String typeToName(FileType t)
Returns the name/extension of the type




