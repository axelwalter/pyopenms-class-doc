MapAlignmentAlgorithmKD
=======================

.. py:class:: MapAlignmentAlgorithmKD


   Bases: :py:class:`object`


Cython implementation of _MapAlignmentAlgorithmKD


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MapAlignmentAlgorithmKD.html


 An efficient reference-free feature map alignment algorithm for unlabeled data
 -----
 This algorithm uses a kd-tree to efficiently compute conflict-free connected components (CCC)
 in a compatibility graph on feature data. This graph is comprised of nodes corresponding
 to features and edges connecting features f and f' iff both are within each other's tolerance
 windows (wrt. RT and m/z difference). CCCs are those CCs that do not contain multiple features
 from the same input map, and whose features all have the same charge state
 -----
 All CCCs above a user-specified minimum size are considered true sets of corresponding features
 and based on these, LOWESS transformations are computed for each input map such that the average
 deviation from the mean retention time within all CCCs is minimized




.. py:method:: MapAlignmentAlgorithmKD.addRTFitData


Cython signature: void addRTFitData(KDTreeFeatureMaps & kd_data)
Compute data points needed for RT transformation in the current `kd_data`, add to `fit_data_`




.. py:method:: MapAlignmentAlgorithmKD.fitLOWESS


Cython signature: void fitLOWESS()
Fit LOWESS to fit_data_, store final models in `transformations_`




.. py:method:: MapAlignmentAlgorithmKD.transform


Cython signature: void transform(KDTreeFeatureMaps & kd_data)
Transform RTs for `kd_data`




