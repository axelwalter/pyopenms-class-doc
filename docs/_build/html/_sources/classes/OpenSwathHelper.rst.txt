OpenSwathHelper
===============

.. py:class:: OpenSwathHelper


   Bases: :py:class:`object`


Cython implementation of _OpenSwathHelper


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OpenSwathHelper.html




.. py:method:: OpenSwathHelper.checkSwathMapAndSelectTransitions


Cython signature: bool checkSwathMapAndSelectTransitions(MSExperiment & exp, TargetedExperiment & targeted_exp, TargetedExperiment & transition_exp_used, double min_upper_edge_dist)




.. py:method:: OpenSwathHelper.computePrecursorId


Cython signature: String computePrecursorId(const String & transition_group_id, int isotope)


Computes unique precursor identifier
-----
Uses transition_group_id and isotope number to compute a unique precursor
id of the form "groupID_Precursor_ix" where x is the isotope number, e.g.
the monoisotopic precursor would become "groupID_Precursor_i0"
-----
:param transition_group_id: Unique id of the transition group (peptide/compound)
:param isotope: Precursor isotope number
:returns: Unique precursor identifier




.. py:method:: OpenSwathHelper.estimateRTRange


Cython signature: libcpp_pair[double,double] estimateRTRange(LightTargetedExperiment exp)


Computes the min and max retention time value
-----
Estimate the retention time span of a targeted experiment by returning the min/max values in retention time as a pair
-----
:returns: A std `pair` that contains (min,max)




