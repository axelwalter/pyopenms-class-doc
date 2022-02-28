ChromatogramExtractorAlgorithm
==============================

.. py:class:: ChromatogramExtractorAlgorithm


   Bases: :py:class:`object`


Cython implementation of _ChromatogramExtractorAlgorithm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ChromatogramExtractorAlgorithm.html
 -- Inherits from ['ProgressLogger']




.. py:method:: ChromatogramExtractorAlgorithm.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: ChromatogramExtractorAlgorithm.extractChromatograms


Cython signature: void extractChromatograms(shared_ptr[SpectrumAccessOpenMS] input, libcpp_vector[shared_ptr[OSChromatogram]] & output, libcpp_vector[ExtractionCoordinates] extraction_coordinates, double mz_extraction_window, bool ppm, double im_extraction_window, String filter)


Extract chromatograms at the m/z and RT defined by the ExtractionCoordinates
-----
:param: input Input spectral map
:param output: Output chromatograms (XICs)
:param extraction_coordinates: Extracts around these coordinates (from
 rt_start to rt_end in seconds - extracts the whole chromatogram if
 rt_end - rt_start < 0).
:param mz_extraction_window: Extracts a window of this size in m/z
dimension in Th or ppm (e.g. a window of 50 ppm means an extraction of
25 ppm on either side)
:param ppm: Whether mz_extraction_window is in ppm or in Th
:param filter: Which function to apply in m/z space (currently "tophat" only)




.. py:method:: ChromatogramExtractorAlgorithm.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: ChromatogramExtractorAlgorithm.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: ChromatogramExtractorAlgorithm.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: ChromatogramExtractorAlgorithm.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: ChromatogramExtractorAlgorithm.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




