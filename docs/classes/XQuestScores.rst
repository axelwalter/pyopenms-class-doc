XQuestScores
============

.. py:class:: XQuestScores


   Bases: :py:class:`object`


Cython implementation of _XQuestScores


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1XQuestScores.html




.. py:method:: XQuestScores.logOccupancyProb


Cython signature: double logOccupancyProb(MSSpectrum theoretical_spec, size_t matched_size, double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm)


Compute the logOccupancyProb score, similar to the match_odds, a score based on the probability of getting the given number of matched peaks by chance
-----
:param theoretical_spec: Theoretical spectrum, sorted by position
:param matched_size: Number of matched peaks between experimental and theoretical spectra
:param fragment_mass_tolerance: The tolerance of the alignment
:param fragment_mass_tolerance_unit: The tolerance unit of the alignment, true = ppm, false = Da




.. py:method:: XQuestScores.matchOddsScore


Cython signature: double matchOddsScore(MSSpectrum & theoretical_spec, double fragment_mass_tolerance, bool fragment_mass_tolerance_unit_ppm, bool is_xlink_spectrum, size_t n_charges)


Compute the match-odds score, a score based on the probability of getting the given number of matched peaks by chance
-----
:param theoretical_spec: Theoretical spectrum, sorted by position
:param matched_size: Alignment between the theoretical and the experimental spectra
:param fragment_mass_tolerance: Fragment mass tolerance of the alignment
:param fragment_mass_tolerance_unit_ppm: Fragment mass tolerance unit of the alignment, true = ppm, false = Da
:param is_xlink_spectrum: Type of cross-link, true = cross-link, false = mono-link
:param n_charges: Number of considered charges in the theoretical spectrum




.. py:method:: XQuestScores.matchedCurrentChain


Cython signature: double matchedCurrentChain(libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_common, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_xlinks, MSSpectrum & spectrum_common_peaks, MSSpectrum & spectrum_xlink_peaks)




.. py:method:: XQuestScores.preScore


         - Cython signature: float preScore(size_t matched_alpha, size_t ions_alpha, size_t matched_beta, size_t ions_beta)


Compute a simple and fast to compute pre-score for a cross-link spectrum match
-----
:param matched_alpha: Number of experimental peaks matched to theoretical linear ions from the alpha peptide
:param ions_alpha: Number of theoretical ions from the alpha peptide
:param matched_beta: Number of experimental peaks matched to theoretical linear ions from the beta peptide
:param ions_beta: Number of theoretical ions from the beta peptide
         - Cython signature: float preScore(size_t matched_alpha, size_t ions_alpha)


Compute a simple and fast to compute pre-score for a mono-link spectrum match
-----
:param matched_alpha: Number of experimental peaks matched to theoretical linear ions from the alpha peptide
:param ions_alpha: Number of theoretical ions from the alpha peptide




.. py:method:: XQuestScores.totalMatchedCurrent


Cython signature: double totalMatchedCurrent(libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_common_alpha, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_common_beta, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_xlinks_alpha, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_xlinks_beta, MSSpectrum & spectrum_common_peaks, MSSpectrum & spectrum_xlink_peaks)




.. py:method:: XQuestScores.weightedTICScore


Cython signature: double weightedTICScore(size_t alpha_size, size_t beta_size, double intsum_alpha, double intsum_beta, double total_current, bool type_is_cross_link)




.. py:method:: XQuestScores.weightedTICScoreXQuest


Cython signature: double weightedTICScoreXQuest(size_t alpha_size, size_t beta_size, double intsum_alpha, double intsum_beta, double total_current, bool type_is_cross_link)




.. py:method:: XQuestScores.xCorrelation


Cython signature: libcpp_vector[double] xCorrelation(MSSpectrum & spec1, MSSpectrum & spec2, int maxshift, double tolerance)




.. py:method:: XQuestScores.xCorrelationPrescore


Cython signature: double xCorrelationPrescore(MSSpectrum & spec1, MSSpectrum & spec2, double tolerance)




.. py:module:: pyopenms.pyopenms_6




