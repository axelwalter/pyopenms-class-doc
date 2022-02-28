IndexedMzMLFileLoader
=====================

.. py:class:: IndexedMzMLFileLoader


   Bases: :py:class:`object`


Cython implementation of _IndexedMzMLFileLoader


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IndexedMzMLFileLoader.html




.. py:method:: IndexedMzMLFileLoader.getOptions


Cython signature: PeakFileOptions getOptions()
Returns the options for loading/storing




.. py:method:: IndexedMzMLFileLoader.load


Cython signature: bool load(String, OnDiscMSExperiment &)


Load a file
-----
Tries to parse the file, success needs to be checked with the return value
-----
:param filename: Filename determines where the file is located
:param exp: Object which will contain the data after the call
:returns: Indicates whether parsing was successful (if it is false, the file most likely was not an mzML or not indexed)




.. py:method:: IndexedMzMLFileLoader.setOptions


Cython signature: void setOptions(PeakFileOptions)
Returns the options for loading/storing




.. py:method:: IndexedMzMLFileLoader.store


         - Cython signature: void store(String, OnDiscMSExperiment &)


Store a file from an on-disc data-structure
-----
:param filename: Filename determines where the file will be stored
:param exp: MS data to be stored
         - Cython signature: void store(String, MSExperiment &)


Store a file from an in-memory data-structure
-----
:param filename: Filename determines where the file will be stored
:param exp: MS data to be stored




