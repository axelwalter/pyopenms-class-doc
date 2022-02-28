MasstraceCorrelator
===================

.. py:class:: MasstraceCorrelator


   Bases: :py:class:`object`


Cython implementation of _MasstraceCorrelator


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MasstraceCorrelator.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: MasstraceCorrelator.createPseudoSpectra


Cython signature: void createPseudoSpectra(const ConsensusMap & map_, MSExperiment & pseudo_spectra, size_t min_peak_nr, double min_correlation, int max_lag, double max_rt_apex_difference)


Compute pseudo-spectra from a set of (MS2) masstraces
-----
This function will take a set of masstraces (consensus map) as input and
produce a vector of pseudo spectra as output (pseudo_spectra result
vector).
-----
It basically makes an all-vs-all comparison of all masstraces against
each other and scores them on how similar they are in their mass traces.
-----
This assumes that the consensus feature is only from one (SWATH) map
This assumes that the consensus map is sorted by intensity




.. py:method:: MasstraceCorrelator.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MasstraceCorrelator.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MasstraceCorrelator.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MasstraceCorrelator.getName


Cython signature: String getName()
Returns the name




.. py:method:: MasstraceCorrelator.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MasstraceCorrelator.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MasstraceCorrelator.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MasstraceCorrelator.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MasstraceCorrelator.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MasstraceCorrelator.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: MasstraceCorrelator.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MasstraceCorrelator.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




