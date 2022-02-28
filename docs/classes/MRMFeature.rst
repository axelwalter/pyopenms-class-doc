MRMFeature
==========

.. py:class:: MRMFeature


   Bases: :py:class:`object`


Cython implementation of _MRMFeature


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFeature.html
 -- Inherits from ['Feature']




.. py:method:: MRMFeature.addFeature


Cython signature: void addFeature(Feature & f, String key)
Adds an feature from a single chromatogram into the feature




.. py:method:: MRMFeature.addPrecursorFeature


Cython signature: void addPrecursorFeature(Feature & f, String key)
Adds a precursor feature from a single chromatogram into the feature




.. py:method:: MRMFeature.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: MRMFeature.clearUniqueId


Cython signature: size_t clearUniqueId()
Clear the unique id. The new unique id will be invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: MRMFeature.encloses


Cython signature: bool encloses(double rt, double mz)


Returns if the mass trace convex hulls of the feature enclose the position specified by `rt` and `mz`
-----
:param rt: Sequence to digest
:param mz: Digestion products




.. py:method:: MRMFeature.ensureUniqueId


Cython signature: size_t ensureUniqueId()
Assigns a valid unique id, but only if the present one is invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: MRMFeature.getAnnotationState


Cython signature: AnnotationState getAnnotationState()




.. py:method:: MRMFeature.getCharge


Cython signature: int getCharge()




.. py:method:: MRMFeature.getConvexHull


Cython signature: ConvexHull2D getConvexHull()




.. py:method:: MRMFeature.getConvexHulls


Cython signature: libcpp_vector[ConvexHull2D] getConvexHulls()




.. py:method:: MRMFeature.getFeature


Cython signature: Feature getFeature(String key)
Returns a specified feature




.. py:method:: MRMFeature.getFeatureIDs


Cython signature: void getFeatureIDs(libcpp_vector[String] & result)
Returns a list of IDs of available features




.. py:method:: MRMFeature.getFeatures


Cython signature: libcpp_vector[Feature] getFeatures()
Returns all the features




.. py:method:: MRMFeature.getIntensity


Cython signature: float getIntensity()
Returns the data point intensity (height)




.. py:method:: MRMFeature.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: MRMFeature.getMZ


Cython signature: double getMZ()
Returns the m/z coordinate (index 1)




.. py:method:: MRMFeature.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: MRMFeature.getOverallQuality


Cython signature: float getOverallQuality()
Model and quality methods




.. py:method:: MRMFeature.getPeptideIdentifications


Cython signature: libcpp_vector[PeptideIdentification] getPeptideIdentifications()
Returns a reference to the PeptideIdentification vector




.. py:method:: MRMFeature.getPrecursorFeature


Cython signature: Feature getPrecursorFeature(String key)
Returns a specified precursor feature




.. py:method:: MRMFeature.getPrecursorFeatureIDs


Cython signature: void getPrecursorFeatureIDs(libcpp_vector[String] & result)
Returns a list of IDs of available precursor features




.. py:method:: MRMFeature.getQuality


Cython signature: float getQuality(size_t index)
Returns the quality in dimension c




.. py:method:: MRMFeature.getRT


Cython signature: double getRT()
Returns the RT coordinate (index 0)




.. py:method:: MRMFeature.getScores


Cython signature: OpenSwath_Scores getScores()
Returns all peakgroup scores




.. py:method:: MRMFeature.getSubordinates


Cython signature: libcpp_vector[Feature] getSubordinates()
Returns the subordinate features




.. py:method:: MRMFeature.getUniqueId


Cython signature: size_t getUniqueId()
Returns the unique id




.. py:method:: MRMFeature.getWidth


Cython signature: float getWidth()




.. py:method:: MRMFeature.hasInvalidUniqueId


Cython signature: size_t hasInvalidUniqueId()
Returns whether the unique id is invalid. Returns 1 if the unique id is invalid, 0 otherwise




.. py:method:: MRMFeature.hasValidUniqueId


Cython signature: size_t hasValidUniqueId()
Returns whether the unique id is valid. Returns 1 if the unique id is valid, 0 otherwise




.. py:method:: MRMFeature.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: MRMFeature.isValid


Cython signature: bool isValid(uint64_t unique_id)
Returns true if the unique_id is valid, false otherwise




.. py:method:: MRMFeature.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: MRMFeature.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: MRMFeature.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: MRMFeature.setCharge


Cython signature: void setCharge(int q)




.. py:method:: MRMFeature.setConvexHulls


Cython signature: void setConvexHulls(libcpp_vector[ConvexHull2D])




.. py:method:: MRMFeature.setIntensity


Cython signature: void setIntensity(float)
Returns the data point intensity (height)




.. py:method:: MRMFeature.setMZ


Cython signature: void setMZ(double)
Returns the m/z coordinate (index 1)




.. py:method:: MRMFeature.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: MRMFeature.setOverallQuality


Cython signature: void setOverallQuality(float q)
Sets the overall quality




.. py:method:: MRMFeature.setPeptideIdentifications


Cython signature: void setPeptideIdentifications(libcpp_vector[PeptideIdentification] & peptides)
Sets the PeptideIdentification vector




.. py:method:: MRMFeature.setQuality


Cython signature: void setQuality(size_t index, float q)
Sets the quality in dimension c




.. py:method:: MRMFeature.setRT


Cython signature: void setRT(double)
Returns the RT coordinate (index 0)




.. py:method:: MRMFeature.setScores


Cython signature: void setScores(OpenSwath_Scores s)
Sets all peakgroup scores




.. py:method:: MRMFeature.setSubordinates


Cython signature: void setSubordinates(libcpp_vector[Feature])
Returns the subordinate features




.. py:method:: MRMFeature.setUniqueId


Cython signature: void setUniqueId(uint64_t rhs)
Assigns a new, valid unique id. Always returns 1




.. py:method:: MRMFeature.setWidth


Cython signature: void setWidth(float q)




