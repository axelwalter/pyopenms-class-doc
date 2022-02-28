PeakPickerCWT
=============

.. py:class:: PeakPickerCWT


   Bases: :py:class:`object`


Cython implementation of _PeakPickerCWT


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakPickerCWT.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: PeakPickerCWT.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: PeakPickerCWT.estimatePeakWidth


Cython signature: double estimatePeakWidth(MSExperiment & input)


Estimates average peak width that can then be used for peak picking
-----
The spectra with the highest TICs are used to estimate an average peak width that
can be used as the peak_width parameter for picking the complete data set.
Typically, the number of peaks increases with decreasing peak width until a plateau
is reached. The beginning of this plateau is our estimate for the peak width.
This estimate is averaged over several spectra




.. py:method:: PeakPickerCWT.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PeakPickerCWT.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: PeakPickerCWT.getName


Cython signature: String getName()
Returns the name




.. py:method:: PeakPickerCWT.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PeakPickerCWT.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PeakPickerCWT.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: PeakPickerCWT.pick


Cython signature: void pick(MSSpectrum & input, MSSpectrum & output)


Applies the peak picking algorithm to a single spectrum
-----
Picks the peaks in the input spectrum and writes the resulting peaks to the output container




.. py:method:: PeakPickerCWT.pickExperiment


Cython signature: void pickExperiment(MSExperiment & input, MSExperiment & output)


Picks the peaks in an MSExperiment
-----
Picks the peaks successive in every scan in the spectrum range. The detected peaks are stored in the output MSExperiment




.. py:method:: PeakPickerCWT.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: PeakPickerCWT.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PeakPickerCWT.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: PeakPickerCWT.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: PeakPickerCWT.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




