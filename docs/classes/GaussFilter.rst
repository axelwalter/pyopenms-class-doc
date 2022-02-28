GaussFilter
===========

.. py:class:: GaussFilter


   Bases: :py:class:`object`


Cython implementation of _GaussFilter


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1GaussFilter.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: GaussFilter.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: GaussFilter.filter


- Cython signature: void filter(MSSpectrum & spectrum)
  Smoothes an MSSpectrum containing profile data


- Cython signature: void filter(MSChromatogram & chromatogram)




.. py:method:: GaussFilter.filterExperiment


Cython signature: void filterExperiment(MSExperiment & exp)
Smoothes an MSExperiment containing profile data




.. py:method:: GaussFilter.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: GaussFilter.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: GaussFilter.getName


Cython signature: String getName()
Returns the name




.. py:method:: GaussFilter.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: GaussFilter.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: GaussFilter.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: GaussFilter.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: GaussFilter.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: GaussFilter.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: GaussFilter.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: GaussFilter.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




