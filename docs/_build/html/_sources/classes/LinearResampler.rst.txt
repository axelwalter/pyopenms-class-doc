LinearResampler
===============

.. py:class:: LinearResampler


   Bases: :py:class:`object`


Cython implementation of _LinearResampler


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1LinearResampler.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: LinearResampler.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: LinearResampler.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: LinearResampler.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: LinearResampler.getName


Cython signature: String getName()
Returns the name




.. py:method:: LinearResampler.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: LinearResampler.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: LinearResampler.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: LinearResampler.raster


Cython signature: void raster(MSSpectrum & input)
Applies the resampling algorithm to an MSSpectrum




.. py:method:: LinearResampler.rasterExperiment


Cython signature: void rasterExperiment(MSExperiment & input)
Resamples the data in an MSExperiment




.. py:method:: LinearResampler.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: LinearResampler.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: LinearResampler.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: LinearResampler.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: LinearResampler.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




