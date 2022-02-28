MsInspectFile
=============

.. py:class:: MsInspectFile


   Bases: :py:class:`object`


Cython implementation of _MsInspectFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MsInspectFile.html




.. py:method:: MsInspectFile.load


Cython signature: void load(const String & filename, FeatureMap & feature_map)


Loads a MsInspect file into a featureXML
-----
The content of the file is stored in `features`
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




.. py:method:: MsInspectFile.store


Cython signature: void store(const String & filename, MSSpectrum & spectrum)
Stores a featureXML as a MsInspect file




