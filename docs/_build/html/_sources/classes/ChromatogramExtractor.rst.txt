ChromatogramExtractor
=====================

.. py:class:: ChromatogramExtractor


   Bases: :py:class:`object`


Cython implementation of _ChromatogramExtractor


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ChromatogramExtractor.html
 -- Inherits from ['ProgressLogger']




.. py:method:: ChromatogramExtractor.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: ChromatogramExtractor.extractChromatograms


Cython signature: void extractChromatograms(MSExperiment & input, MSExperiment & output, TargetedExperiment & transition_exp, double extract_window, bool ppm, TransformationDescription trafo, double rt_extraction_window, String filter)
Extract chromatograms at the m/z and RT defined by the ExtractionCoordinates




.. py:method:: ChromatogramExtractor.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: ChromatogramExtractor.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: ChromatogramExtractor.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: ChromatogramExtractor.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: ChromatogramExtractor.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




