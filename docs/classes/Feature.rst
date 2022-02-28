Feature
=======

.. py:class:: Feature


   Bases: :py:class:`object`


Cython implementation of _Feature


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Feature.html
 -- Inherits from ['UniqueIdInterface', 'RichPeak2D']


 An LC-MS feature
 -----
 The Feature class is used to describe the two-dimensional signal caused by an
 analyte. It can store a charge state and a list of peptide identifications
 (for peptides). The area occupied by the Feature in the LC-MS data set is
 represented by a list of convex hulls (one for each isotopic peak). There is
 also a convex hull for the entire Feature. The model description can store
 the parameters of a two-dimensional theoretical model of the underlying
 signal in LC-MS. Currently, non-peptide compounds are also represented as
 features




.. py:method:: Feature.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: Feature.clearUniqueId


Cython signature: size_t clearUniqueId()
Clear the unique id. The new unique id will be invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: Feature.encloses


Cython signature: bool encloses(double rt, double mz)


Returns if the mass trace convex hulls of the feature enclose the position specified by `rt` and `mz`
-----
:param rt: Sequence to digest
:param mz: Digestion products




.. py:method:: Feature.ensureUniqueId


Cython signature: size_t ensureUniqueId()
Assigns a valid unique id, but only if the present one is invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: Feature.getAnnotationState


Cython signature: AnnotationState getAnnotationState()




.. py:method:: Feature.getCharge


Cython signature: int getCharge()




.. py:method:: Feature.getConvexHull


Cython signature: ConvexHull2D getConvexHull()




.. py:method:: Feature.getConvexHulls


Cython signature: libcpp_vector[ConvexHull2D] getConvexHulls()




.. py:method:: Feature.getIntensity


Cython signature: float getIntensity()
Returns the data point intensity (height)




.. py:method:: Feature.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: Feature.getMZ


Cython signature: double getMZ()
Returns the m/z coordinate (index 1)




.. py:method:: Feature.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: Feature.getOverallQuality


Cython signature: float getOverallQuality()
Model and quality methods




.. py:method:: Feature.getPeptideIdentifications


Cython signature: libcpp_vector[PeptideIdentification] getPeptideIdentifications()
Returns a reference to the PeptideIdentification vector




.. py:method:: Feature.getQuality


Cython signature: float getQuality(size_t index)
Returns the quality in dimension c




.. py:method:: Feature.getRT


Cython signature: double getRT()
Returns the RT coordinate (index 0)




.. py:method:: Feature.getSubordinates


Cython signature: libcpp_vector[Feature] getSubordinates()
Returns the subordinate features




.. py:method:: Feature.getUniqueId


Cython signature: size_t getUniqueId()
Returns the unique id




.. py:method:: Feature.getWidth


Cython signature: float getWidth()




.. py:method:: Feature.hasInvalidUniqueId


Cython signature: size_t hasInvalidUniqueId()
Returns whether the unique id is invalid. Returns 1 if the unique id is invalid, 0 otherwise




.. py:method:: Feature.hasValidUniqueId


Cython signature: size_t hasValidUniqueId()
Returns whether the unique id is valid. Returns 1 if the unique id is valid, 0 otherwise




.. py:method:: Feature.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: Feature.isValid


Cython signature: bool isValid(uint64_t unique_id)
Returns true if the unique_id is valid, false otherwise




.. py:method:: Feature.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: Feature.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: Feature.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: Feature.setCharge


Cython signature: void setCharge(int q)




.. py:method:: Feature.setConvexHulls


Cython signature: void setConvexHulls(libcpp_vector[ConvexHull2D])




.. py:method:: Feature.setIntensity


Cython signature: void setIntensity(float)
Returns the data point intensity (height)




.. py:method:: Feature.setMZ


Cython signature: void setMZ(double)
Returns the m/z coordinate (index 1)




.. py:method:: Feature.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: Feature.setOverallQuality


Cython signature: void setOverallQuality(float q)
Sets the overall quality




.. py:method:: Feature.setPeptideIdentifications


Cython signature: void setPeptideIdentifications(libcpp_vector[PeptideIdentification] & peptides)
Sets the PeptideIdentification vector




.. py:method:: Feature.setQuality


Cython signature: void setQuality(size_t index, float q)
Sets the quality in dimension c




.. py:method:: Feature.setRT


Cython signature: void setRT(double)
Returns the RT coordinate (index 0)




.. py:method:: Feature.setSubordinates


Cython signature: void setSubordinates(libcpp_vector[Feature])
Returns the subordinate features




.. py:method:: Feature.setUniqueId


Cython signature: void setUniqueId(uint64_t rhs)
Assigns a new, valid unique id. Always returns 1




.. py:method:: Feature.setWidth


Cython signature: void setWidth(float q)




