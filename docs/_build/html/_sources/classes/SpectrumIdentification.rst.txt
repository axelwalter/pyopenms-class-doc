SpectrumIdentification
======================

.. py:class:: SpectrumIdentification


   Bases: :py:class:`object`


Cython implementation of _SpectrumIdentification


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumIdentification.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: SpectrumIdentification.addHit


Cython signature: void addHit(IdentificationHit & hit)
Adds a single identification hit to the hits




.. py:method:: SpectrumIdentification.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: SpectrumIdentification.getHits


Cython signature: libcpp_vector[IdentificationHit] getHits()
Returns the identification hits of this spectrum identification




.. py:method:: SpectrumIdentification.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: SpectrumIdentification.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: SpectrumIdentification.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: SpectrumIdentification.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: SpectrumIdentification.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: SpectrumIdentification.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: SpectrumIdentification.setHits


Cython signature: void setHits(libcpp_vector[IdentificationHit] & hits)
Sets the identification hits of this spectrum identification (corresponds to single peptide hit in the list)




.. py:method:: SpectrumIdentification.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




