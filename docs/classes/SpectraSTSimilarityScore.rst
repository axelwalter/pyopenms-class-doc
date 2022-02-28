SpectraSTSimilarityScore
========================

.. py:class:: SpectraSTSimilarityScore


   Bases: :py:class:`object`


Cython implementation of _SpectraSTSimilarityScore


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectraSTSimilarityScore.html




.. py:method:: SpectraSTSimilarityScore.compute_F


Cython signature: double compute_F(double dot_product, double delta_D, double dot_bias)


Computes the overall all score
-----
:param dot_product: dot_product of a match
:param delta_D: delta_D should be calculated after all dot products for a unidentified spectrum are computed
:param dot_bias
:returns: The SpectraST similarity score




.. py:method:: SpectraSTSimilarityScore.delta_D


Cython signature: double delta_D(double top_hit, double runner_up)


Calculates the normalized distance between top_hit and runner_up
-----
:param top_hit: Is the best score for a given match
:param runner_up: A match with a worse score than top_hit, e.g. the second best score
:returns: normalized distance




.. py:method:: SpectraSTSimilarityScore.dot_bias


Cython signature: double dot_bias(BinnedSpectrum & bin1, BinnedSpectrum & bin2, double dot_product)


Calculates how much of the dot product is dominated by a few peaks
-----
:param dot_product: If -1 this value will be calculated as well.
:param bin1: First spectrum in binned representation
:param bin2: Second spectrum in binned representation




.. py:method:: SpectraSTSimilarityScore.getProductName


Cython signature: String getProductName()
Reimplemented from PeakSpectrumCompareFunctor




.. py:method:: SpectraSTSimilarityScore.preprocess


Cython signature: bool preprocess(MSSpectrum & spec, float remove_peak_intensity_threshold, unsigned int cut_peaks_below, size_t min_peak_number, size_t max_peak_number)


Preprocesses the spectrum
-----
The preprocessing removes peak below a intensity threshold, reject spectra that does
not have enough peaks, and cuts peaks exceeding the max_peak_number most intense peaks
-----
:returns: true if spectrum passes filtering




.. py:method:: SpectraSTSimilarityScore.transform


Cython signature: BinnedSpectrum transform(MSSpectrum & spec)
Spectrum is transformed into a binned spectrum with bin size 1 and spread 1 and the intensities are normalized




