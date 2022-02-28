ProgressLogger
==============

.. py:class:: ProgressLogger


   Bases: :py:class:`object`


Cython implementation of _ProgressLogger


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProgressLogger.html


 Base class for all classes that want to report their progress
 -----
 Per default the progress log is disabled. Use setLogType to enable it
 -----
 Use startProgress, setProgress and endProgress for the actual logging




.. py:method:: ProgressLogger.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: ProgressLogger.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: ProgressLogger.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: ProgressLogger.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: ProgressLogger.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: ProgressLogger.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




