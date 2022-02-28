PeakPickerHiRes
===============

.. py:class:: PeakPickerHiRes


   Bases: :py:class:`object`


Cython implementation of _PeakPickerHiRes


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakPickerHiRes.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: PeakPickerHiRes.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: PeakPickerHiRes.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PeakPickerHiRes.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: PeakPickerHiRes.getName


Cython signature: String getName()
Returns the name




.. py:method:: PeakPickerHiRes.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PeakPickerHiRes.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PeakPickerHiRes.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: PeakPickerHiRes.pick


- Cython signature: void pick(MSSpectrum & input, MSSpectrum & output)
- Cython signature: void pick(MSChromatogram & input, MSChromatogram & output)




.. py:method:: PeakPickerHiRes.pickExperiment


         - Cython signature: void pickExperiment(MSExperiment & input, MSExperiment & output, bool check_spectrum_type)


Applies the peak-picking algorithm to a map (MSExperiment). This
method picks peaks for each scan in the map consecutively. The resulting
picked peaks are written to the output map
-----
:param input: Input map in profile mode
:param output: Output map with picked peaks
:param check_spectrum_type: If set, checks spectrum type and throws an exception if a centroided spectrum is passed
         - Cython signature: void pickExperiment(MSExperiment & input, MSExperiment & output, libcpp_vector[libcpp_vector[PeakBoundary]] & boundaries_spec, libcpp_vector[libcpp_vector[PeakBoundary]] & boundaries_chrom, bool check_spectrum_type)




.. py:method:: PeakPickerHiRes.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: PeakPickerHiRes.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PeakPickerHiRes.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: PeakPickerHiRes.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: PeakPickerHiRes.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




