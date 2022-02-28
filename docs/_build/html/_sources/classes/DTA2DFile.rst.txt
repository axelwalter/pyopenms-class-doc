DTA2DFile
=========

.. py:class:: DTA2DFile


   Bases: :py:class:`object`


Cython implementation of _DTA2DFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1DTA2DFile.html
 -- Inherits from ['ProgressLogger']




.. py:method:: DTA2DFile.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: DTA2DFile.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: DTA2DFile.getOptions


Cython signature: PeakFileOptions getOptions()




.. py:method:: DTA2DFile.load


Cython signature: void load(String filename, MSExperiment & peakmap)




.. py:method:: DTA2DFile.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: DTA2DFile.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: DTA2DFile.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: DTA2DFile.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: DTA2DFile.store


Cython signature: void store(String filename, MSExperiment & peakmap)




.. py:method:: DTA2DFile.storeTIC


Cython signature: void storeTIC(String filename, MSExperiment & peakmap)




