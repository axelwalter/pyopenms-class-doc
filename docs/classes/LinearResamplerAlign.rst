LinearResamplerAlign
====================

.. py:class:: LinearResamplerAlign


   Bases: :py:class:`object`


Cython implementation of _LinearResamplerAlign


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1LinearResamplerAlign.html
 -- Inherits from ['LinearResampler']




.. py:method:: LinearResamplerAlign.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: LinearResamplerAlign.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: LinearResamplerAlign.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: LinearResamplerAlign.getName


Cython signature: String getName()
Returns the name




.. py:method:: LinearResamplerAlign.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: LinearResamplerAlign.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: LinearResamplerAlign.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: LinearResamplerAlign.raster


Cython signature: void raster(MSSpectrum & input)
Applies the resampling algorithm to an MSSpectrum




.. py:method:: LinearResamplerAlign.rasterExperiment


Cython signature: void rasterExperiment(MSExperiment & input)
Resamples the data in an MSExperiment




.. py:method:: LinearResamplerAlign.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: LinearResamplerAlign.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: LinearResamplerAlign.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: LinearResamplerAlign.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: LinearResamplerAlign.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




