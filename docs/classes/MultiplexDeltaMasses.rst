MultiplexDeltaMasses
====================

.. py:class:: MultiplexDeltaMasses


   Bases: :py:class:`object`


Cython implementation of _MultiplexDeltaMasses


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MultiplexDeltaMasses.html


 Data structure for mass shift pattern
 -----
 Groups of labelled peptides appear with characteristic mass shifts
 -----
 For example, for an Arg6 labeled SILAC peptide pair we expect to see
 mass shifts of 0 and 6 Da. Or as second example, for a
 peptide pair of a dimethyl labelled sample with a single lysine
 we will see mass shifts of 56 Da and 64 Da.
 28 Da (N-term) + 28 Da (K) and 34 Da (N-term) + 34 Da (K)
 for light and heavy partners respectively
 -----
 The data structure stores the mass shifts and corresponding labels
 for a group of matching peptide features




.. py:method:: MultiplexDeltaMasses.getDeltaMasses


Cython signature: libcpp_vector[MultiplexDeltaMasses_DeltaMass] getDeltaMasses()




