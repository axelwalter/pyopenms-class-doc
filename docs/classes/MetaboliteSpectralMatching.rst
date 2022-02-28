MetaboliteSpectralMatching
==========================

.. py:class:: MetaboliteSpectralMatching


   Bases: :py:class:`object`


Cython implementation of _MetaboliteSpectralMatching


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaboliteSpectralMatching.html
 -- Inherits from ['ProgressLogger', 'DefaultParamHandler']




.. py:method:: MetaboliteSpectralMatching.computeHyperScore


Cython signature: double computeHyperScore(double fragment_mass_error, bool fragment_mass_tolerance_unit_ppm, MSSpectrum exp_spectrum, MSSpectrum db_spectrum, libcpp_vector[PeptideHit_PeakAnnotation] & annotations, double mz_lower_bound)




.. py:method:: MetaboliteSpectralMatching.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MetaboliteSpectralMatching.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MetaboliteSpectralMatching.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MetaboliteSpectralMatching.getName


Cython signature: String getName()
Returns the name




.. py:method:: MetaboliteSpectralMatching.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MetaboliteSpectralMatching.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MetaboliteSpectralMatching.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MetaboliteSpectralMatching.run


Cython signature: void run(MSExperiment & exp, MSExperiment & speclib, MzTab & mz_tab)




.. py:method:: MetaboliteSpectralMatching.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MetaboliteSpectralMatching.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MetaboliteSpectralMatching.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: MetaboliteSpectralMatching.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MetaboliteSpectralMatching.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




