SqMassFile
==========

.. py:class:: SqMassFile


   Bases: :py:class:`object`


Cython implementation of _SqMassFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SqMassFile.html


 An class that uses on-disk SQLite database to read and write spectra and chromatograms
 -----
 This class provides functions to read and write spectra and chromatograms
 to disk using a SQLite database and store them in sqMass format. This
 allows users to access, select and filter spectra and chromatograms
 on-demand even in a large collection of data




.. py:method:: SqMassFile.load


Cython signature: void load(const String & filename, MSExperiment & map_)
Read / Write a complete mass spectrometric experiment




.. py:method:: SqMassFile.setConfig


Cython signature: void setConfig(SqMassConfig config)




.. py:method:: SqMassFile.store


Cython signature: void store(const String & filename, MSExperiment & map_)
Store an MSExperiment in sqMass format




