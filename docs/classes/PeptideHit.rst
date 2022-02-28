PeptideHit
==========

.. py:class:: PeptideHit


   Bases: :py:class:`object`


Cython implementation of _PeptideHit


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeptideHit.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: PeptideHit.addAnalysisResults


Cython signature: void addAnalysisResults(PeptideHit_AnalysisResult aresult)
Add information on (search engine) sub scores associated with this PSM




.. py:method:: PeptideHit.addPeptideEvidence


Cython signature: void addPeptideEvidence(PeptideEvidence)
Adds information on a peptide that is (potentially) identified by this PSM




.. py:method:: PeptideHit.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: PeptideHit.extractProteinAccessionsSet


Cython signature: libcpp_set[String] extractProteinAccessionsSet()
Extracts the set of non-empty protein accessions from peptide evidences




.. py:method:: PeptideHit.getAnalysisResults


Cython signature: libcpp_vector[PeptideHit_AnalysisResult] getAnalysisResults()
Returns information on (search engine) sub scores associated with this PSM




.. py:method:: PeptideHit.getCharge


Cython signature: int getCharge()
Returns the charge of the peptide




.. py:method:: PeptideHit.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: PeptideHit.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: PeptideHit.getPeakAnnotations


Cython signature: libcpp_vector[PeptideHit_PeakAnnotation] getPeakAnnotations()
Returns the fragment annotations




.. py:method:: PeptideHit.getPeptideEvidences


Cython signature: libcpp_vector[PeptideEvidence] getPeptideEvidences()
Returns information on peptides (potentially) identified by this PSM




.. py:method:: PeptideHit.getRank


Cython signature: unsigned int getRank()
Returns the PSM rank




.. py:method:: PeptideHit.getScore


Cython signature: float getScore()
Returns the PSM score




.. py:method:: PeptideHit.getSequence


Cython signature: AASequence getSequence()
Returns the peptide sequence without trailing or following spaces




.. py:method:: PeptideHit.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: PeptideHit.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: PeptideHit.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: PeptideHit.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: PeptideHit.setAnalysisResults


Cython signature: void setAnalysisResults(libcpp_vector[PeptideHit_AnalysisResult] aresult)
Sets information on (search engine) sub scores associated with this PSM




.. py:method:: PeptideHit.setCharge


Cython signature: void setCharge(int)
Sets the charge of the peptide




.. py:method:: PeptideHit.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: PeptideHit.setPeakAnnotations


Cython signature: void setPeakAnnotations(libcpp_vector[PeptideHit_PeakAnnotation])
Sets the fragment annotations




.. py:method:: PeptideHit.setPeptideEvidences


Cython signature: void setPeptideEvidences(libcpp_vector[PeptideEvidence])
Sets information on peptides (potentially) identified by this PSM




.. py:method:: PeptideHit.setRank


Cython signature: void setRank(unsigned int)
Sets the PSM rank




.. py:method:: PeptideHit.setScore


Cython signature: void setScore(double)
Sets the PSM score




.. py:method:: PeptideHit.setSequence


Cython signature: void setSequence(AASequence)
Sets the peptide sequence




