MapAlignmentAlgorithmSpectrumAlignment
======================================

.. py:class:: MapAlignmentAlgorithmSpectrumAlignment


   Bases: :py:class:`object`


Cython implementation of _MapAlignmentAlgorithmSpectrumAlignment


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MapAlignmentAlgorithmSpectrumAlignment.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.align


Cython signature: void align(libcpp_vector[MSExperiment] &, libcpp_vector[TransformationDescription] &)
Align peak maps




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.getName


Cython signature: String getName()
Returns the name




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MapAlignmentAlgorithmSpectrumAlignment.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




