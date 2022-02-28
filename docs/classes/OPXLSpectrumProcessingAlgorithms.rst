OPXLSpectrumProcessingAlgorithms
================================

.. py:class:: OPXLSpectrumProcessingAlgorithms


   Bases: :py:class:`object`


Cython implementation of _OPXLSpectrumProcessingAlgorithms


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OPXLSpectrumProcessingAlgorithms.html




.. py:method:: OPXLSpectrumProcessingAlgorithms.getSpectrumAlignmentFastCharge


Cython signature: void getSpectrumAlignmentFastCharge(libcpp_vector[libcpp_pair[size_t,size_t]] & alignment, double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm, const MSSpectrum & theo_spectrum, const MSSpectrum & exp_spectrum, const IntegerDataArray & theo_charges, const IntegerDataArray & exp_charges, FloatDataArray & ppm_error_array, double intensity_cutoff)




.. py:method:: OPXLSpectrumProcessingAlgorithms.getSpectrumAlignmentSimple


Cython signature: void getSpectrumAlignmentSimple(libcpp_vector[libcpp_pair[size_t,size_t]] & alignment, double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm, const libcpp_vector[SimplePeak] & theo_spectrum, const MSSpectrum & exp_spectrum, const IntegerDataArray & exp_charges)




.. py:method:: OPXLSpectrumProcessingAlgorithms.mergeAnnotatedSpectra


Cython signature: MSSpectrum mergeAnnotatedSpectra(MSSpectrum & first_spectrum, MSSpectrum & second_spectrum)




.. py:method:: OPXLSpectrumProcessingAlgorithms.preprocessSpectra


Cython signature: MSExperiment preprocessSpectra(MSExperiment & exp, double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm, size_t peptide_min_size, int min_precursor_charge, int max_precursor_charge, bool deisotope, bool labeled)




