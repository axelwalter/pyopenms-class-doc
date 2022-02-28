RichPeak2D
==========

.. py:class:: RichPeak2D


   Bases: :py:class:`object`


Cython implementation of _RichPeak2D


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1RichPeak2D.html
 -- Inherits from ['Peak2D', 'UniqueIdInterface', 'MetaInfoInterface']




.. py:method:: RichPeak2D.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: RichPeak2D.clearUniqueId


Cython signature: size_t clearUniqueId()
Clear the unique id. The new unique id will be invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: RichPeak2D.ensureUniqueId


Cython signature: size_t ensureUniqueId()
Assigns a valid unique id, but only if the present one is invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: RichPeak2D.getIntensity


Cython signature: float getIntensity()
Returns the data point intensity (height)




.. py:method:: RichPeak2D.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: RichPeak2D.getMZ


Cython signature: double getMZ()
Returns the m/z coordinate (index 1)




.. py:method:: RichPeak2D.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: RichPeak2D.getRT


Cython signature: double getRT()
Returns the RT coordinate (index 0)




.. py:method:: RichPeak2D.getUniqueId


Cython signature: size_t getUniqueId()
Returns the unique id




.. py:method:: RichPeak2D.hasInvalidUniqueId


Cython signature: size_t hasInvalidUniqueId()
Returns whether the unique id is invalid. Returns 1 if the unique id is invalid, 0 otherwise




.. py:method:: RichPeak2D.hasValidUniqueId


Cython signature: size_t hasValidUniqueId()
Returns whether the unique id is valid. Returns 1 if the unique id is valid, 0 otherwise




.. py:method:: RichPeak2D.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: RichPeak2D.isValid


Cython signature: bool isValid(uint64_t unique_id)
Returns true if the unique_id is valid, false otherwise




.. py:method:: RichPeak2D.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: RichPeak2D.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: RichPeak2D.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: RichPeak2D.setIntensity


Cython signature: void setIntensity(float)
Returns the data point intensity (height)




.. py:method:: RichPeak2D.setMZ


Cython signature: void setMZ(double)
Returns the m/z coordinate (index 1)




.. py:method:: RichPeak2D.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: RichPeak2D.setRT


Cython signature: void setRT(double)
Returns the RT coordinate (index 0)




.. py:method:: RichPeak2D.setUniqueId


Cython signature: void setUniqueId(uint64_t rhs)
Assigns a new, valid unique id. Always returns 1




