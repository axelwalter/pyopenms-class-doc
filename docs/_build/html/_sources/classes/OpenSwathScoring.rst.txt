OpenSwathScoring
================

.. py:class:: OpenSwathScoring


   Bases: :py:class:`object`


Cython implementation of _OpenSwathScoring


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OpenSwathScoring.html




.. py:method:: OpenSwathScoring.getNormalized_library_intensities_


Cython signature: void getNormalized_library_intensities_(libcpp_vector[LightTransition] transitions, libcpp_vector[double] normalized_library_intensity)




.. py:method:: OpenSwathScoring.initialize


Cython signature: void initialize(double rt_normalization_factor, int add_up_spectra, double spacing_for_spectra_resampling, double drift_extra, OpenSwath_Scores_Usage su, libcpp_string spectrum_addition_method)


Initialize the scoring object
-----
Sets the parameters for the scoring
-----
:param rt_normalization_factor: Specifies the range of the normalized retention time space
:param add_up_spectra: How many spectra to add up (default 1)
:param spacing_for_spectra_resampling: Spacing factor for spectra addition
:param su: Which scores to actually compute
:param spectrum_addition_method: Method to use for spectrum addition (valid: "simple", "resample")




