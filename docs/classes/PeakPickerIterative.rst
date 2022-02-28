PeakPickerIterative
===================

.. py:class:: PeakPickerIterative


   Bases: :py:class:`object`


Cython implementation of _PeakPickerIterative


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakPickerIterative.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: PeakPickerIterative.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: PeakPickerIterative.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PeakPickerIterative.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: PeakPickerIterative.getName


Cython signature: String getName()
Returns the name




.. py:method:: PeakPickerIterative.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PeakPickerIterative.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PeakPickerIterative.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: PeakPickerIterative.pick


Cython signature: void pick(MSSpectrum & input, MSSpectrum & output)


This will pick one single spectrum. The PeakPickerHiRes is used to
generate seeds, these seeds are then used to re-center the mass and
compute peak width and integrated intensity of the peak
-----
Finally, other peaks that would fall within the primary peak are
discarded
-----
The output are the remaining peaks




.. py:method:: PeakPickerIterative.pickExperiment


Cython signature: void pickExperiment(MSExperiment & input, MSExperiment & output)




.. py:method:: PeakPickerIterative.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: PeakPickerIterative.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PeakPickerIterative.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: PeakPickerIterative.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: PeakPickerIterative.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




