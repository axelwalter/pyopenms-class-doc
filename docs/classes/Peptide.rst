Peptide
=======

.. py:class:: Peptide


   Bases: :py:class:`object`


Cython implementation of _Peptide


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::TargetedExperimentHelper::RetentionTime::RTUnit_1_1Peptide.html
 -- Inherits from ['CVTermList']




.. py:method:: Peptide.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)
Adds a CV term




.. py:method:: Peptide.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: Peptide.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)
Merges the given map into the member map, no duplicate checking




.. py:method:: Peptide.empty


Cython signature: bool empty()




.. py:attribute:: Peptide.evidence




.. py:method:: Peptide.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()
Returns the accession string of the term




.. py:method:: Peptide.getChargeState


Cython signature: int getChargeState()
Returns the peptide or compound charge state




.. py:method:: Peptide.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: Peptide.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: Peptide.getPeptideGroupLabel


Cython signature: String getPeptideGroupLabel()
Get the peptide group label




.. py:method:: Peptide.getRetentionTime


Cython signature: double getRetentionTime()
Gets compound or peptide retention time




.. py:method:: Peptide.getRetentionTimeType


Cython signature: RTType getRetentionTimeType()
Get compound or peptide retentiontime type




.. py:method:: Peptide.getRetentionTimeUnit


Cython signature: RTUnit getRetentionTimeUnit()
Get compound or peptide retentiontime unit (minute/seconds)




.. py:method:: Peptide.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:method:: Peptide.hasCharge


Cython signature: bool hasCharge()
Whether product has set charge state




.. py:method:: Peptide.hasRetentionTime


Cython signature: bool hasRetentionTime()
Gets compound or peptide retention time




.. py:attribute:: Peptide.id




.. py:method:: Peptide.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: Peptide.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: Peptide.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:attribute:: Peptide.mods




.. py:attribute:: Peptide.protein_refs




.. py:method:: Peptide.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: Peptide.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)
Replaces the specified CV term




.. py:method:: Peptide.replaceCVTerms


Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)




.. py:attribute:: Peptide.rts




.. py:attribute:: Peptide.sequence




.. py:method:: Peptide.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)
Sets the CV terms




.. py:method:: Peptide.setChargeState


Cython signature: void setChargeState(int charge)
Sets the peptide or compound charge states




.. py:method:: Peptide.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: Peptide.setPeptideGroupLabel


Cython signature: void setPeptideGroupLabel(String label)
Sets the peptide group label




