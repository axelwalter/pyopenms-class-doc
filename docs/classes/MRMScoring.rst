MRMScoring
==========

.. py:class:: MRMScoring


   Bases: :py:class:`object`


Cython implementation of _MRMScoring


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenSwath_1_1MRMScoring.html




.. py:method:: MRMScoring.calcMIPrecursorCombinedScore


Cython signature: double calcMIPrecursorCombinedScore()




.. py:method:: MRMScoring.calcMIPrecursorContrastScore


Cython signature: double calcMIPrecursorContrastScore()




.. py:method:: MRMScoring.calcMIPrecursorScore


Cython signature: double calcMIPrecursorScore()




.. py:method:: MRMScoring.calcMIScore


Cython signature: double calcMIScore()




.. py:method:: MRMScoring.calcMIWeightedScore


Cython signature: double calcMIWeightedScore(const libcpp_vector[double] & normalized_library_intensity)




.. py:method:: MRMScoring.calcRTScore


Cython signature: double calcRTScore(LightCompound & peptide, double normalized_experimental_rt)




.. py:method:: MRMScoring.calcSeparateMIContrastScore


Cython signature: libcpp_vector[double] calcSeparateMIContrastScore()




.. py:method:: MRMScoring.calcSeparateXcorrContrastCoelutionScore


Cython signature: libcpp_vector[double] calcSeparateXcorrContrastCoelutionScore()
Calculate the separate cross-correlation contrast score




.. py:method:: MRMScoring.calcSeparateXcorrContrastShapeScore


Cython signature: libcpp_vector[double] calcSeparateXcorrContrastShapeScore()
Calculate the separate cross-correlation contrast shape score




.. py:method:: MRMScoring.calcXcorrCoelutionScore


Cython signature: double calcXcorrCoelutionScore()
Calculate the cross-correlation coelution score. The score is a distance where zero indicates perfect coelution




.. py:method:: MRMScoring.calcXcorrCoelutionWeightedScore


Cython signature: double calcXcorrCoelutionWeightedScore(libcpp_vector[double] & normalized_library_intensity)


Calculate the weighted cross-correlation coelution score
-----
The score is a distance where zero indicates perfect coelution. The
score is weighted by the transition intensities, non-perfect coelution
in low-intensity transitions should thus become less important




.. py:method:: MRMScoring.calcXcorrPrecursorContrastCoelutionScore


Cython signature: double calcXcorrPrecursorContrastCoelutionScore()


Calculate the precursor cross-correlation contrast score against the transitions
-----
The score is a distance where zero indicates perfect coelution




.. py:method:: MRMScoring.calcXcorrPrecursorContrastShapeScore


Cython signature: double calcXcorrPrecursorContrastShapeScore()
Calculate the precursor cross-correlation shape score against the transitions




.. py:method:: MRMScoring.calcXcorrShapeScore


Cython signature: double calcXcorrShapeScore()


Calculate the cross-correlation shape score
-----
The score is a correlation measure where 1 indicates perfect correlation
and 0 means no correlation.




.. py:method:: MRMScoring.calcXcorrShapeWeightedScore


Cython signature: double calcXcorrShapeWeightedScore(libcpp_vector[double] & normalized_library_intensity)


Calculate the weighted cross-correlation shape score
-----
The score is a correlation measure where 1 indicates perfect correlation
and 0 means no correlation. The score is weighted by the transition
intensities, non-perfect coelution in low-intensity transitions should
thus become less important




.. py:method:: MRMScoring.getMIMatrix


Cython signature: MatrixDouble getMIMatrix()




