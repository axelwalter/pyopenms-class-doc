LocalLinearMap
==============

.. py:class:: LocalLinearMap


   Bases: :py:class:`object`


Cython implementation of _LocalLinearMap


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1LocalLinearMap.html


 Trained Local Linear Map (LLM) model for peak intensity prediction
 -----
 This class offers a model for predictions of peptide peak heights
 (referred to as intensities) by a Local Linear Map (LLM) model and
 is the basis of PeakIntensityPredictor
 -----
 A general introduction to the Peak Intensity Predictor (PIP)
 can be found in the PIP Tutorial
 -----
 The model trained needs two files for storing the position of the
 codebook vectors and the linear mappings (codebooks.data, linearMapping.data)
 This is the default model used by PeakIntensityPredictor




.. py:method:: LocalLinearMap.getCodebooks


Cython signature: MatrixDouble getCodebooks()
Returns position of the codebook vectors (18-dim)




.. py:method:: LocalLinearMap.getLLMParam


Cython signature: LLMParam getLLMParam()
Returns parameters of the LocalLinearMap model




.. py:method:: LocalLinearMap.getMatrixA


Cython signature: MatrixDouble getMatrixA()
Returns linear mappings of the codebooks




.. py:method:: LocalLinearMap.getVectorWout


Cython signature: libcpp_vector[double] getVectorWout()
Returns linear bias




.. py:method:: LocalLinearMap.normalizeVector


Cython signature: void normalizeVector(libcpp_vector[double] & aaIndexVariables)
Calculates and returns the normalized amino acid index variables from string representation of peptide




