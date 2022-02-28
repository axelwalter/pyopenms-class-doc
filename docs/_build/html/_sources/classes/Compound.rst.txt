Compound
========

.. py:class:: Compound


   Bases: :py:class:`object`


Cython implementation of _Compound


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::TargetedExperimentHelper::RetentionTime::RTUnit_1_1Compound.html
 -- Inherits from ['CVTermList']




.. py:method:: Compound.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)
Adds a CV term




.. py:method:: Compound.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: Compound.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)
Merges the given map into the member map, no duplicate checking




.. py:method:: Compound.empty


Cython signature: bool empty()




.. py:method:: Compound.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()
Returns the accession string of the term




.. py:method:: Compound.getChargeState


Cython signature: int getChargeState()
Returns the peptide or compound charge state




.. py:method:: Compound.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: Compound.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: Compound.getRetentionTime


Cython signature: double getRetentionTime()
Gets compound or peptide retention time




.. py:method:: Compound.getRetentionTimeType


Cython signature: RTType getRetentionTimeType()
Get compound or peptide retentiontime type




.. py:method:: Compound.getRetentionTimeUnit


Cython signature: RTUnit getRetentionTimeUnit()
Get compound or peptide retentiontime type




.. py:method:: Compound.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:method:: Compound.hasCharge


Cython signature: bool hasCharge()
Whether peptide or compound has set charge state




.. py:method:: Compound.hasRetentionTime


Cython signature: bool hasRetentionTime()
Check whether compound or peptide has an annotated retention time




.. py:attribute:: Compound.id




.. py:method:: Compound.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: Compound.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: Compound.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:attribute:: Compound.molecular_formula




.. py:method:: Compound.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: Compound.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)
Replaces the specified CV term




.. py:method:: Compound.replaceCVTerms


Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)




.. py:attribute:: Compound.rts




.. py:method:: Compound.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)
Sets the CV terms




.. py:method:: Compound.setChargeState


Cython signature: void setChargeState(int charge)
Sets the peptide or compound charge state




.. py:method:: Compound.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:attribute:: Compound.smiles_string




.. py:attribute:: Compound.theoretical_mass




