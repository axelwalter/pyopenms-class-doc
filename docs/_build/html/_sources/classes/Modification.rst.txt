Modification
============

.. py:class:: Modification


   Bases: :py:class:`object`


Cython implementation of _Modification


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Modification.html
 -- Inherits from ['SampleTreatment']




.. py:attribute:: Modification.Modification_SpecificityType


alias of :py:class:`pyopenms.pyopenms_2.__Modification_SpecificityType`


.. py:method:: Modification.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: Modification.getAffectedAminoAcids


Cython signature: String getAffectedAminoAcids()
Returns a string containing the one letter code of the amino acids that are affected by the reagent (default "")




.. py:method:: Modification.getComment


Cython signature: String getComment()
Returns the description of the sample treatment




.. py:method:: Modification.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: Modification.getMass


Cython signature: double getMass()
Returns the mass change (default 0.0)




.. py:method:: Modification.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: Modification.getReagentName


Cython signature: String getReagentName()
Returns the name of the reagent that was used (default "")




.. py:method:: Modification.getSpecificityType


Cython signature: Modification_SpecificityType getSpecificityType()
Returns the specificity of the reagent (default AA)




.. py:method:: Modification.getType


Cython signature: String getType()
Returns the treatment type




.. py:method:: Modification.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: Modification.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: Modification.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: Modification.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: Modification.setAffectedAminoAcids


Cython signature: void setAffectedAminoAcids(const String & affected_amino_acids)
Returns a string containing the one letter code of the amino acids that are affected by the reagent. Do not separate them by space, tab or comma!




.. py:method:: Modification.setComment


Cython signature: void setComment(const String & comment)
Sets the description of the sample treatment




.. py:method:: Modification.setMass


Cython signature: void setMass(double mass)
Sets the mass change




.. py:method:: Modification.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: Modification.setReagentName


Cython signature: void setReagentName(const String & reagent_name)
Sets the name of the reagent that was used




.. py:method:: Modification.setSpecificityType


Cython signature: void setSpecificityType(Modification_SpecificityType & specificity_type)
Sets the specificity of the reagent




