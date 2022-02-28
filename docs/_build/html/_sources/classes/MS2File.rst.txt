MS2File
=======

.. py:class:: MS2File


   Bases: :py:class:`object`


Cython implementation of _MS2File


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MS2File.html
 -- Inherits from ['ProgressLogger']




.. py:method:: MS2File.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MS2File.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MS2File.load


Cython signature: void load(const String & filename, MSExperiment & exp)




.. py:method:: MS2File.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MS2File.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MS2File.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MS2File.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




