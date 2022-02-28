MzXMLFile
=========

.. py:class:: MzXMLFile


   Bases: :py:class:`object`


Cython implementation of _MzXMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MzXMLFile.html
 -- Inherits from ['ProgressLogger']




.. py:method:: MzXMLFile.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MzXMLFile.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MzXMLFile.getOptions


Cython signature: PeakFileOptions getOptions()
Returns the options for loading/storing




.. py:method:: MzXMLFile.load


Cython signature: void load(String filename, MSExperiment & exp)


Loads a MSExperiment from a MzXML file
-----
:param exp: MSExperiment




.. py:method:: MzXMLFile.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MzXMLFile.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MzXMLFile.setOptions


Cython signature: void setOptions(PeakFileOptions)
Sets options for loading/storing




.. py:method:: MzXMLFile.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MzXMLFile.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: MzXMLFile.store


Cython signature: void store(String filename, MSExperiment & exp)


Stores a MSExperiment in a MzXML file
-----
:param exp: MSExperiment




.. py:method:: MzXMLFile.transform




