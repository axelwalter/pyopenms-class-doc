MRMTransitionGroupCP
====================

.. py:class:: MRMTransitionGroupCP


   Bases: :py:class:`object`


Cython implementation of _MRMTransitionGroup[_MSChromatogram,_ReactionMonitoringTransition]


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMTransitionGroup[_MSChromatogram,_ReactionMonitoringTransition].html




.. py:method:: MRMTransitionGroupCP.addChromatogram


Cython signature: void addChromatogram(MSChromatogram chromatogram, String key)




.. py:method:: MRMTransitionGroupCP.addFeature


Cython signature: void addFeature(MRMFeature feature)




.. py:method:: MRMTransitionGroupCP.addPrecursorChromatogram


Cython signature: void addPrecursorChromatogram(MSChromatogram chromatogram, String key)




.. py:method:: MRMTransitionGroupCP.addTransition


Cython signature: void addTransition(ReactionMonitoringTransition transition, String key)




.. py:method:: MRMTransitionGroupCP.chromatogramIdsMatch


Cython signature: bool chromatogramIdsMatch()




.. py:method:: MRMTransitionGroupCP.getBestFeature


Cython signature: MRMFeature getBestFeature()




.. py:method:: MRMTransitionGroupCP.getChromatogram


Cython signature: MSChromatogram getChromatogram(String key)




.. py:method:: MRMTransitionGroupCP.getChromatograms


Cython signature: libcpp_vector[MSChromatogram] getChromatograms()




.. py:method:: MRMTransitionGroupCP.getFeatures


Cython signature: libcpp_vector[MRMFeature] getFeatures()




.. py:method:: MRMTransitionGroupCP.getFeaturesMuteable


Cython signature: libcpp_vector[MRMFeature] getFeaturesMuteable()




.. py:method:: MRMTransitionGroupCP.getLibraryIntensity


Cython signature: void getLibraryIntensity(libcpp_vector[double] result)




.. py:method:: MRMTransitionGroupCP.getPrecursorChromatogram


Cython signature: MSChromatogram getPrecursorChromatogram(String key)




.. py:method:: MRMTransitionGroupCP.getPrecursorChromatograms


Cython signature: libcpp_vector[MSChromatogram] getPrecursorChromatograms()




.. py:method:: MRMTransitionGroupCP.getTransition


Cython signature: ReactionMonitoringTransition getTransition(String key)




.. py:method:: MRMTransitionGroupCP.getTransitionGroupID


Cython signature: String getTransitionGroupID()




.. py:method:: MRMTransitionGroupCP.getTransitions


Cython signature: libcpp_vector[ReactionMonitoringTransition] getTransitions()




.. py:method:: MRMTransitionGroupCP.getTransitionsMuteable


Cython signature: libcpp_vector[ReactionMonitoringTransition] getTransitionsMuteable()




.. py:method:: MRMTransitionGroupCP.hasChromatogram


Cython signature: bool hasChromatogram(String key)




.. py:method:: MRMTransitionGroupCP.hasPrecursorChromatogram


Cython signature: bool hasPrecursorChromatogram(String key)




.. py:method:: MRMTransitionGroupCP.hasTransition


Cython signature: bool hasTransition(String key)




.. py:method:: MRMTransitionGroupCP.isInternallyConsistent


Cython signature: bool isInternallyConsistent()




.. py:method:: MRMTransitionGroupCP.setTransitionGroupID


Cython signature: void setTransitionGroupID(String tr_gr_id)




.. py:method:: MRMTransitionGroupCP.size


Cython signature: size_t size()




.. py:method:: MRMTransitionGroupCP.subset


Cython signature: MRMTransitionGroupCP subset(libcpp_vector[libcpp_utf8_string] tr_ids)




