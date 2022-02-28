ConsensusFeature
================

.. py:class:: ConsensusFeature


   Bases: :py:class:`object`


Cython implementation of _ConsensusFeature


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusFeature.html
 -- Inherits from ['UniqueIdInterface', 'BaseFeature']


 A consensus feature spanning multiple LC-MS/MS experiments.
 -----
 A ConsensusFeature represents analytes that have been
 quantified across multiple LC-MS/MS experiments. Each analyte in a
 ConsensusFeature is linked to its original LC-MS/MS run through a
 unique identifier.
 -----
 Get access to the underlying features through getFeatureList()




.. py:method:: ConsensusFeature.addRatio


Cython signature: void addRatio(Ratio r)
Connects a ratio to the ConsensusFeature.




.. py:method:: ConsensusFeature.clear


Cython signature: void clear()




.. py:method:: ConsensusFeature.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: ConsensusFeature.clearUniqueId


Cython signature: size_t clearUniqueId()
Clear the unique id. The new unique id will be invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: ConsensusFeature.computeConsensus


Cython signature: void computeConsensus()
Computes and updates the consensus position, intensity, and charge




.. py:method:: ConsensusFeature.computeDechargeConsensus


Cython signature: void computeDechargeConsensus(FeatureMap, bool)
Computes the uncharged parent RT & mass, assuming the handles are charge variants




.. py:method:: ConsensusFeature.computeMonoisotopicConsensus


Cython signature: void computeMonoisotopicConsensus()
Computes and updates the consensus position, intensity, and charge




.. py:method:: ConsensusFeature.empty


Cython signature: bool empty()




.. py:method:: ConsensusFeature.ensureUniqueId


Cython signature: size_t ensureUniqueId()
Assigns a valid unique id, but only if the present one is invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: ConsensusFeature.getAnnotationState


Cython signature: AnnotationState getAnnotationState()
State of peptide identifications attached to this feature. If one ID has multiple hits, the output depends on the top-hit only




.. py:method:: ConsensusFeature.getCharge


Cython signature: int getCharge()
Returns the charge state




.. py:method:: ConsensusFeature.getFeatureList


Cython signature: libcpp_vector[FeatureHandle] getFeatureList()




.. py:method:: ConsensusFeature.getIntensity


Cython signature: float getIntensity()
Returns the data point intensity (height)




.. py:method:: ConsensusFeature.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: ConsensusFeature.getMZ


Cython signature: double getMZ()
Returns the m/z coordinate (index 1)




.. py:method:: ConsensusFeature.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: ConsensusFeature.getPeptideIdentifications


Cython signature: libcpp_vector[PeptideIdentification] getPeptideIdentifications()
Returns the PeptideIdentification vector




.. py:method:: ConsensusFeature.getQuality


Cython signature: float getQuality()
Returns the overall quality




.. py:method:: ConsensusFeature.getRT


Cython signature: double getRT()
Returns the RT coordinate (index 0)




.. py:method:: ConsensusFeature.getRatios


Cython signature: libcpp_vector[Ratio] getRatios()
Get the ratio vector.




.. py:method:: ConsensusFeature.getUniqueId


Cython signature: size_t getUniqueId()
Returns the unique id




.. py:method:: ConsensusFeature.getWidth


Cython signature: float getWidth()
Returns the features width (full width at half max, FWHM)




.. py:method:: ConsensusFeature.hasInvalidUniqueId


Cython signature: size_t hasInvalidUniqueId()
Returns whether the unique id is invalid. Returns 1 if the unique id is invalid, 0 otherwise




.. py:method:: ConsensusFeature.hasValidUniqueId


Cython signature: size_t hasValidUniqueId()
Returns whether the unique id is valid. Returns 1 if the unique id is valid, 0 otherwise




.. py:method:: ConsensusFeature.insert


- Cython signature: void insert(uint64_t map_idx, Peak2D, uint64_t element_idx)
- Cython signature: void insert(uint64_t map_idx, BaseFeature)
- Cython signature: void insert(uint64_t map_idx, ConsensusFeature)




.. py:method:: ConsensusFeature.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: ConsensusFeature.isValid


Cython signature: bool isValid(uint64_t unique_id)
Returns true if the unique_id is valid, false otherwise




.. py:method:: ConsensusFeature.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: ConsensusFeature.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: ConsensusFeature.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: ConsensusFeature.setCharge


Cython signature: void setCharge(int q)
Sets the charge state




.. py:method:: ConsensusFeature.setIntensity


Cython signature: void setIntensity(float)
Returns the data point intensity (height)




.. py:method:: ConsensusFeature.setMZ


Cython signature: void setMZ(double)
Returns the m/z coordinate (index 1)




.. py:method:: ConsensusFeature.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: ConsensusFeature.setPeptideIdentifications


Cython signature: void setPeptideIdentifications(libcpp_vector[PeptideIdentification] & peptides)
Sets the PeptideIdentification vector




.. py:method:: ConsensusFeature.setQuality


Cython signature: void setQuality(float q)
Sets the overall quality




.. py:method:: ConsensusFeature.setRT


Cython signature: void setRT(double)
Returns the RT coordinate (index 0)




.. py:method:: ConsensusFeature.setRatios


Cython signature: void setRatios(libcpp_vector[Ratio] rs)
Connects the ratios to the ConsensusFeature.




.. py:method:: ConsensusFeature.setUniqueId


Cython signature: void setUniqueId(uint64_t rhs)
Assigns a new, valid unique id. Always returns 1




.. py:method:: ConsensusFeature.setWidth


Cython signature: void setWidth(float q)
Sets the width of the feature (FWHM)




.. py:method:: ConsensusFeature.size


Cython signature: size_t size()




