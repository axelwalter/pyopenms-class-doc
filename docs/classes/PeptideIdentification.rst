PeptideIdentification
=====================

.. py:class:: PeptideIdentification


   Bases: :py:class:`object`


Cython implementation of _PeptideIdentification


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeptideIdentification.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: PeptideIdentification.assignRanks


Cython signature: void assignRanks()




.. py:method:: PeptideIdentification.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: PeptideIdentification.empty


Cython signature: bool empty()




.. py:method:: PeptideIdentification.getBaseName


Cython signature: String getBaseName()




.. py:method:: PeptideIdentification.getExperimentLabel


Cython signature: String getExperimentLabel()




.. py:method:: PeptideIdentification.getHits


Cython signature: libcpp_vector[PeptideHit] getHits()
Returns the peptide hits as const




.. py:method:: PeptideIdentification.getIdentifier


Cython signature: String getIdentifier()




.. py:method:: PeptideIdentification.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: PeptideIdentification.getMZ


Cython signature: double getMZ()




.. py:method:: PeptideIdentification.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: PeptideIdentification.getRT


Cython signature: double getRT()




.. py:method:: PeptideIdentification.getReferencingHits


Cython signature: libcpp_vector[PeptideHit] getReferencingHits(libcpp_vector[PeptideHit], libcpp_set[String] &)
Returns all peptide hits which reference to a given protein accession (i.e. filter by protein accession)




.. py:method:: PeptideIdentification.getScoreType


Cython signature: String getScoreType()




.. py:method:: PeptideIdentification.getSignificanceThreshold


Cython signature: double getSignificanceThreshold()
Returns the peptide significance threshold value




.. py:method:: PeptideIdentification.hasMZ


Cython signature: bool hasMZ()




.. py:method:: PeptideIdentification.hasRT


Cython signature: bool hasRT()




.. py:method:: PeptideIdentification.insertHit


Cython signature: void insertHit(PeptideHit)
Appends a peptide hit




.. py:method:: PeptideIdentification.isHigherScoreBetter


Cython signature: bool isHigherScoreBetter()




.. py:method:: PeptideIdentification.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: PeptideIdentification.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: PeptideIdentification.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: PeptideIdentification.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: PeptideIdentification.setBaseName


Cython signature: void setBaseName(String)




.. py:method:: PeptideIdentification.setExperimentLabel


Cython signature: void setExperimentLabel(String)




.. py:method:: PeptideIdentification.setHigherScoreBetter


Cython signature: void setHigherScoreBetter(bool)




.. py:method:: PeptideIdentification.setHits


Cython signature: void setHits(libcpp_vector[PeptideHit])
Sets the peptide hits




.. py:method:: PeptideIdentification.setIdentifier


Cython signature: void setIdentifier(String)




.. py:method:: PeptideIdentification.setMZ


Cython signature: void setMZ(double)




.. py:method:: PeptideIdentification.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: PeptideIdentification.setRT


Cython signature: void setRT(double)




.. py:method:: PeptideIdentification.setScoreType


Cython signature: void setScoreType(String)




.. py:method:: PeptideIdentification.setSignificanceThreshold


Cython signature: void setSignificanceThreshold(double value)
Setting of the peptide significance threshold value




.. py:method:: PeptideIdentification.sort


Cython signature: void sort()




.. py:method:: PeptideIdentification.sortByRank


Cython signature: void sortByRank()




