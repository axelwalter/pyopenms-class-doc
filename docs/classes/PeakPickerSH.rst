PeakPickerSH
============

.. py:class:: PeakPickerSH


   Bases: :py:class:`object`


Cython implementation of _PeakPickerSH


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakPickerSH.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: PeakPickerSH.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: PeakPickerSH.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PeakPickerSH.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: PeakPickerSH.getName


Cython signature: String getName()
Returns the name




.. py:method:: PeakPickerSH.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PeakPickerSH.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PeakPickerSH.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: PeakPickerSH.pick


Cython signature: void pick(MSSpectrum & input_, MSSpectrum & output, float fWindowWidth)
Applies the peak-picking algorithm to one spectrum




.. py:method:: PeakPickerSH.pickExperiment


Cython signature: void pickExperiment(MSExperiment & input_, MSExperiment & output)
Applies the peak-picking algorithm to a map (MSExperiment)




.. py:method:: PeakPickerSH.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: PeakPickerSH.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PeakPickerSH.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: PeakPickerSH.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: PeakPickerSH.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




