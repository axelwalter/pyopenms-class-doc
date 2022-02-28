TargetedExperiment_Interpretation
=================================

.. py:class:: TargetedExperiment_Interpretation


   Bases: :py:class:`object`


Cython implementation of _TargetedExperiment_Interpretation


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::TargetedExperimentHelper::RetentionTime::RTUnit_1_1TargetedExperiment_Interpretation.html




.. py:method:: TargetedExperiment_Interpretation.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)




.. py:method:: TargetedExperiment_Interpretation.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)




.. py:method:: TargetedExperiment_Interpretation.empty


Cython signature: bool empty()




.. py:method:: TargetedExperiment_Interpretation.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()




.. py:method:: TargetedExperiment_Interpretation.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)




.. py:method:: TargetedExperiment_Interpretation.getKeysAsIntegers


Cython signature: void getKeysAsIntegers(libcpp_vector[unsigned int] & keys)




.. py:method:: TargetedExperiment_Interpretation.getMetaValue


- Cython signature: DataValue getMetaValue(unsigned int)
- Cython signature: DataValue getMetaValue(String)




.. py:method:: TargetedExperiment_Interpretation.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:attribute:: TargetedExperiment_Interpretation.iontype




.. py:method:: TargetedExperiment_Interpretation.metaValueExists


- Cython signature: bool metaValueExists(String)
- Cython signature: bool metaValueExists(unsigned int)




.. py:attribute:: TargetedExperiment_Interpretation.ordinal




.. py:attribute:: TargetedExperiment_Interpretation.rank




.. py:method:: TargetedExperiment_Interpretation.removeMetaValue


- Cython signature: void removeMetaValue(String)
- Cython signature: void removeMetaValue(unsigned int)




.. py:method:: TargetedExperiment_Interpretation.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)




.. py:method:: TargetedExperiment_Interpretation.replaceCVTerms


- Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)
- Cython signature: void replaceCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)




.. py:method:: TargetedExperiment_Interpretation.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)




.. py:method:: TargetedExperiment_Interpretation.setMetaValue


- Cython signature: void setMetaValue(unsigned int, DataValue)
- Cython signature: void setMetaValue(String, DataValue)




