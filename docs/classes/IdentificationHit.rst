IdentificationHit
=================

.. py:class:: IdentificationHit


   Bases: :py:class:`object`


Cython implementation of _IdentificationHit


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IdentificationHit.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: IdentificationHit.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: IdentificationHit.getCalculatedMassToCharge


Cython signature: double getCalculatedMassToCharge()
Returns the calculated mass to charge ratio




.. py:method:: IdentificationHit.getCharge


Cython signature: int getCharge()
Returns the charge state




.. py:method:: IdentificationHit.getExperimentalMassToCharge


Cython signature: double getExperimentalMassToCharge()
Returns the experimental mass to charge




.. py:method:: IdentificationHit.getId


Cython signature: String getId()
Returns the id




.. py:method:: IdentificationHit.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: IdentificationHit.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: IdentificationHit.getName


Cython signature: String getName()
Returns the name




.. py:method:: IdentificationHit.getPassThreshold


Cython signature: bool getPassThreshold()
Returns whether the peptide passed the threshold




.. py:method:: IdentificationHit.getRank


Cython signature: int getRank()
Returns the rank of the peptide




.. py:method:: IdentificationHit.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: IdentificationHit.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: IdentificationHit.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: IdentificationHit.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: IdentificationHit.setCalculatedMassToCharge


Cython signature: void setCalculatedMassToCharge(double mz)
Sets the calculated mass to charge ratio




.. py:method:: IdentificationHit.setCharge


Cython signature: void setCharge(int charge)
Sets the charge state of the peptide




.. py:method:: IdentificationHit.setExperimentalMassToCharge


Cython signature: void setExperimentalMassToCharge(double mz)
Sets the experimental mass to charge ratio




.. py:method:: IdentificationHit.setId


Cython signature: void setId(String id)
Sets the identifier




.. py:method:: IdentificationHit.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: IdentificationHit.setName


Cython signature: void setName(String name)
Sets the name




.. py:method:: IdentificationHit.setPassThreshold


Cython signature: void setPassThreshold(bool)
Sets whether the peptide passed the threshold




.. py:method:: IdentificationHit.setRank


Cython signature: void setRank(int rank)
Sets the rank of the peptide




