PeakIntensityPredictor
======================

.. py:class:: PeakIntensityPredictor


   Bases: :py:class:`object`


Cython implementation of _PeakIntensityPredictor


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakIntensityPredictor.html


 Predict peak heights of peptides based on Local Linear Map model
 -----
 This class can be used for predictions of peptide peak heights
 (referred to as intensities) from a peptide sequence
 by a Local Linear Map (LLM) model
 A general introduction to the Peak Intensity Predictor (PIP)
 can be found in the PIP Tutorial
 -----
 The predictor performs only on the peptides sequences as an AASequence representation. Every sequence is
 transformed to an 18 dimensional data vector representing certain
 chemical characteristics and is loaded into the trained LocalLinearMap model to
 find the predicted peptides peak intensity
 -----
 Every predictor object calls the appropriate LocalLinearMap model, transforms
 the given sequences and creates a vector space in which the LocalLinearMap
 performs




.. py:method:: PeakIntensityPredictor.predict


         - Cython signature: double predict(AASequence & sequence)
           Returns predicted peak heights (intensities) of a single peptide


         - Cython signature: double predict(AASequence & sequence, libcpp_vector[double] & add_info)


Returns predicted peak heights (intensities) of a single peptide
-----
Some additional information for each peptide is returned in `add_info`
For each peptide a row with the following components is returned:
- 0: x coordinates of associated cluster (first column)
- 1: y coordinates of associated cluster (2nd column)
- 2: error (RMSE) of the peptide to the associated next prototype (cluster center)
         - Cython signature: libcpp_vector[double] predict(libcpp_vector[AASequence] & sequences)
         - Cython signature: libcpp_vector[double] predict(libcpp_vector[AASequence] & sequences, libcpp_vector[libcpp_vector[double]] & add_info)




