BaseFeature
===========

.. py:class:: BaseFeature


   Bases: :py:class:`object`


Cython implementation of _BaseFeature


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1BaseFeature.html
 -- Inherits from ['UniqueIdInterface', 'RichPeak2D']




.. py:method:: BaseFeature.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: BaseFeature.clearUniqueId


Cython signature: size_t clearUniqueId()
Clear the unique id. The new unique id will be invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: BaseFeature.ensureUniqueId


Cython signature: size_t ensureUniqueId()
Assigns a valid unique id, but only if the present one is invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: BaseFeature.getAnnotationState


Cython signature: AnnotationState getAnnotationState()
State of peptide identifications attached to this feature. If one ID has multiple hits, the output depends on the top-hit only




.. py:method:: BaseFeature.getCharge


Cython signature: int getCharge()
Returns the charge state




.. py:method:: BaseFeature.getIntensity


Cython signature: float getIntensity()
Returns the data point intensity (height)




.. py:method:: BaseFeature.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: BaseFeature.getMZ


Cython signature: double getMZ()
Returns the m/z coordinate (index 1)




.. py:method:: BaseFeature.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: BaseFeature.getPeptideIdentifications


Cython signature: libcpp_vector[PeptideIdentification] getPeptideIdentifications()
Returns the PeptideIdentification vector




.. py:method:: BaseFeature.getQuality


Cython signature: float getQuality()
Returns the overall quality




.. py:method:: BaseFeature.getRT


Cython signature: double getRT()
Returns the RT coordinate (index 0)




.. py:method:: BaseFeature.getUniqueId


Cython signature: size_t getUniqueId()
Returns the unique id




.. py:method:: BaseFeature.getWidth


Cython signature: float getWidth()
Returns the features width (full width at half max, FWHM)




.. py:method:: BaseFeature.hasInvalidUniqueId


Cython signature: size_t hasInvalidUniqueId()
Returns whether the unique id is invalid. Returns 1 if the unique id is invalid, 0 otherwise




.. py:method:: BaseFeature.hasValidUniqueId


Cython signature: size_t hasValidUniqueId()
Returns whether the unique id is valid. Returns 1 if the unique id is valid, 0 otherwise




.. py:method:: BaseFeature.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: BaseFeature.isValid


Cython signature: bool isValid(uint64_t unique_id)
Returns true if the unique_id is valid, false otherwise




.. py:method:: BaseFeature.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: BaseFeature.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: BaseFeature.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: BaseFeature.setCharge


Cython signature: void setCharge(int q)
Sets the charge state




.. py:method:: BaseFeature.setIntensity


Cython signature: void setIntensity(float)
Returns the data point intensity (height)




.. py:method:: BaseFeature.setMZ


Cython signature: void setMZ(double)
Returns the m/z coordinate (index 1)




.. py:method:: BaseFeature.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: BaseFeature.setPeptideIdentifications


Cython signature: void setPeptideIdentifications(libcpp_vector[PeptideIdentification] & peptides)
Sets the PeptideIdentification vector




.. py:method:: BaseFeature.setQuality


Cython signature: void setQuality(float q)
Sets the overall quality




.. py:method:: BaseFeature.setRT


Cython signature: void setRT(double)
Returns the RT coordinate (index 0)




.. py:method:: BaseFeature.setUniqueId


Cython signature: void setUniqueId(uint64_t rhs)
Assigns a new, valid unique id. Always returns 1




.. py:method:: BaseFeature.setWidth


Cython signature: void setWidth(float q)
Sets the width of the feature (FWHM)




