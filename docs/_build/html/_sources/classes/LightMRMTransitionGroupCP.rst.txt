LightMRMTransitionGroupCP
=========================

.. py:class:: LightMRMTransitionGroupCP


   Bases: :py:class:`object`


Cython implementation of _MRMTransitionGroup[_MSChromatogram,_LightTransition]


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMTransitionGroup[_MSChromatogram,_LightTransition].html




.. py:method:: LightMRMTransitionGroupCP.addChromatogram


Cython signature: void addChromatogram(MSChromatogram chromatogram, String key)




.. py:method:: LightMRMTransitionGroupCP.addFeature


Cython signature: void addFeature(MRMFeature feature)




.. py:method:: LightMRMTransitionGroupCP.addPrecursorChromatogram


Cython signature: void addPrecursorChromatogram(MSChromatogram chromatogram, String key)




.. py:method:: LightMRMTransitionGroupCP.addTransition


Cython signature: void addTransition(LightTransition transition, String key)




.. py:method:: LightMRMTransitionGroupCP.chromatogramIdsMatch


Cython signature: bool chromatogramIdsMatch()




.. py:method:: LightMRMTransitionGroupCP.getBestFeature


Cython signature: MRMFeature getBestFeature()




.. py:method:: LightMRMTransitionGroupCP.getChromatogram


Cython signature: MSChromatogram getChromatogram(String key)




.. py:method:: LightMRMTransitionGroupCP.getChromatograms


Cython signature: libcpp_vector[MSChromatogram] getChromatograms()




.. py:method:: LightMRMTransitionGroupCP.getFeatures


Cython signature: libcpp_vector[MRMFeature] getFeatures()




.. py:method:: LightMRMTransitionGroupCP.getFeaturesMuteable


Cython signature: libcpp_vector[MRMFeature] getFeaturesMuteable()




.. py:method:: LightMRMTransitionGroupCP.getLibraryIntensity


Cython signature: void getLibraryIntensity(libcpp_vector[double] result)




.. py:method:: LightMRMTransitionGroupCP.getPrecursorChromatogram


Cython signature: MSChromatogram getPrecursorChromatogram(String key)




.. py:method:: LightMRMTransitionGroupCP.getPrecursorChromatograms


Cython signature: libcpp_vector[MSChromatogram] getPrecursorChromatograms()




.. py:method:: LightMRMTransitionGroupCP.getTransition


Cython signature: LightTransition getTransition(String key)




.. py:method:: LightMRMTransitionGroupCP.getTransitionGroupID


Cython signature: String getTransitionGroupID()




.. py:method:: LightMRMTransitionGroupCP.getTransitions


Cython signature: libcpp_vector[LightTransition] getTransitions()




.. py:method:: LightMRMTransitionGroupCP.getTransitionsMuteable


Cython signature: libcpp_vector[LightTransition] getTransitionsMuteable()




.. py:method:: LightMRMTransitionGroupCP.hasChromatogram


Cython signature: bool hasChromatogram(String key)




.. py:method:: LightMRMTransitionGroupCP.hasPrecursorChromatogram


Cython signature: bool hasPrecursorChromatogram(String key)




.. py:method:: LightMRMTransitionGroupCP.hasTransition


Cython signature: bool hasTransition(String key)




.. py:method:: LightMRMTransitionGroupCP.isInternallyConsistent


Cython signature: bool isInternallyConsistent()




.. py:method:: LightMRMTransitionGroupCP.setTransitionGroupID


Cython signature: void setTransitionGroupID(String tr_gr_id)




.. py:method:: LightMRMTransitionGroupCP.size


Cython signature: size_t size()




.. py:method:: LightMRMTransitionGroupCP.subset


Cython signature: LightMRMTransitionGroupCP subset(libcpp_vector[libcpp_utf8_string] tr_ids)




