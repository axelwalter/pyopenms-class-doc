MRMTransitionGroupPicker
========================

.. py:class:: MRMTransitionGroupPicker


   Bases: :py:class:`object`


Cython implementation of _MRMTransitionGroupPicker


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMTransitionGroupPicker.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: MRMTransitionGroupPicker.createMRMFeature


Cython signature: MRMFeature createMRMFeature(LightMRMTransitionGroupCP transition_group, libcpp_vector[MSChromatogram] & picked_chroms, libcpp_vector[MSChromatogram] & smoothed_chroms, const int chr_idx, const int peak_idx)




.. py:method:: MRMTransitionGroupPicker.findLargestPeak


Cython signature: void findLargestPeak(libcpp_vector[MSChromatogram] & picked_chroms, int & chr_idx, int & peak_idx)




.. py:method:: MRMTransitionGroupPicker.findWidestPeakIndices


Cython signature: void findWidestPeakIndices(libcpp_vector[MSChromatogram] & picked_chroms, int & chrom_idx, int & point_idx)




.. py:method:: MRMTransitionGroupPicker.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MRMTransitionGroupPicker.getName


Cython signature: String getName()
Returns the name




.. py:method:: MRMTransitionGroupPicker.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MRMTransitionGroupPicker.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MRMTransitionGroupPicker.pickTransitionGroup


- Cython signature: void pickTransitionGroup(LightMRMTransitionGroupCP transition_group)
- Cython signature: void pickTransitionGroup(MRMTransitionGroupCP transition_group)




.. py:method:: MRMTransitionGroupPicker.remove_overlapping_features


Cython signature: void remove_overlapping_features(libcpp_vector[MSChromatogram] & picked_chroms, double best_left, double best_right)




.. py:method:: MRMTransitionGroupPicker.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MRMTransitionGroupPicker.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




