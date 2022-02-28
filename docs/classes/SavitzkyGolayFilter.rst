SavitzkyGolayFilter
===================

.. py:class:: SavitzkyGolayFilter


   Bases: :py:class:`object`


Cython implementation of _SavitzkyGolayFilter


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SavitzkyGolayFilter.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: SavitzkyGolayFilter.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: SavitzkyGolayFilter.filter


Cython signature: void filter(MSSpectrum & spectrum)
Removed the noise from an MSSpectrum containing profile data




.. py:method:: SavitzkyGolayFilter.filterExperiment


Cython signature: void filterExperiment(MSExperiment & exp)
Removed the noise from an MSExperiment containing profile data




.. py:method:: SavitzkyGolayFilter.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: SavitzkyGolayFilter.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: SavitzkyGolayFilter.getName


Cython signature: String getName()
Returns the name




.. py:method:: SavitzkyGolayFilter.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: SavitzkyGolayFilter.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: SavitzkyGolayFilter.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: SavitzkyGolayFilter.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: SavitzkyGolayFilter.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: SavitzkyGolayFilter.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: SavitzkyGolayFilter.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: SavitzkyGolayFilter.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




