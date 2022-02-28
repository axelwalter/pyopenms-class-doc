MzQuantMLFile
=============

.. py:class:: MzQuantMLFile


   Bases: :py:class:`object`


Cython implementation of _MzQuantMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MzQuantMLFile.html




.. py:method:: MzQuantMLFile.isSemanticallyValid


Cython signature: bool isSemanticallyValid(String filename, StringList & errors, StringList & warnings)


Checks if a file is valid with respect to the mapping file and the controlled vocabulary
-----
:param filename: File name of the file to be checked
:param errors: Errors during the validation are returned in this output parameter
:param warnings: Warnings during the validation are returned in this output parameter
-----
:raises:
  Exception: UnableToCreateFile is thrown if the file could not be created




.. py:method:: MzQuantMLFile.load


Cython signature: void load(String filename, MSQuantifications & msq)


Loads a map from a MzQuantML file
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




.. py:method:: MzQuantMLFile.store


Cython signature: void store(String filename, MSQuantifications & msq)


Stores a map in a MzQuantML file
-----
:raises:
  Exception: UnableToCreateFile is thrown if the file could not be created




