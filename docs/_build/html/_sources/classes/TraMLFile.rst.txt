TraMLFile
=========

.. py:class:: TraMLFile


   Bases: :py:class:`object`


Cython implementation of _TraMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TraMLFile.html




.. py:method:: TraMLFile.isSemanticallyValid


Cython signature: bool isSemanticallyValid(String filename, StringList & errors, StringList & warnings)


Checks if a file is valid with respect to the mapping file and the controlled vocabulary
-----
:param filename: File name of the file to be checked
:param errors: Errors during the validation are returned in this output parameter
:param warnings: Warnings during the validation are returned in this output parameter




.. py:method:: TraMLFile.load


Cython signature: void load(String filename, TargetedExperiment & id)
Loads a map from a TraML file




.. py:method:: TraMLFile.store


Cython signature: void store(String filename, TargetedExperiment & id)
Stores a map in a TraML file




