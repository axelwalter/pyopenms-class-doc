FeatureFindingMetabo
====================

.. py:class:: FeatureFindingMetabo


   Bases: :py:class:`object`


Cython implementation of _FeatureFindingMetabo


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureFindingMetabo.html
 -- Inherits from ['ProgressLogger', 'DefaultParamHandler']




.. py:method:: FeatureFindingMetabo.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: FeatureFindingMetabo.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: FeatureFindingMetabo.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: FeatureFindingMetabo.getName


Cython signature: String getName()
Returns the name




.. py:method:: FeatureFindingMetabo.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: FeatureFindingMetabo.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: FeatureFindingMetabo.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: FeatureFindingMetabo.run


Cython signature: void run(libcpp_vector[Kernel_MassTrace] input_mtraces, FeatureMap & output_featmap, libcpp_vector[libcpp_vector[MSChromatogram]] & output_chromatograms)




.. py:method:: FeatureFindingMetabo.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: FeatureFindingMetabo.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: FeatureFindingMetabo.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: FeatureFindingMetabo.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: FeatureFindingMetabo.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




