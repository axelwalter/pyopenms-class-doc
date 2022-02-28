TargetedExperiment_Instrument
=============================

.. py:class:: TargetedExperiment_Instrument


   Bases: :py:class:`object`


Cython implementation of _TargetedExperiment_Instrument


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::TargetedExperimentHelper::RetentionTime::RTUnit_1_1TargetedExperiment_Instrument.html




.. py:method:: TargetedExperiment_Instrument.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)




.. py:method:: TargetedExperiment_Instrument.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)




.. py:method:: TargetedExperiment_Instrument.empty


Cython signature: bool empty()




.. py:method:: TargetedExperiment_Instrument.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()




.. py:method:: TargetedExperiment_Instrument.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)




.. py:method:: TargetedExperiment_Instrument.getKeysAsIntegers


Cython signature: void getKeysAsIntegers(libcpp_vector[unsigned int] & keys)




.. py:method:: TargetedExperiment_Instrument.getMetaValue


- Cython signature: DataValue getMetaValue(unsigned int)
- Cython signature: DataValue getMetaValue(String)




.. py:method:: TargetedExperiment_Instrument.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:attribute:: TargetedExperiment_Instrument.id




.. py:method:: TargetedExperiment_Instrument.metaValueExists


- Cython signature: bool metaValueExists(String)
- Cython signature: bool metaValueExists(unsigned int)




.. py:method:: TargetedExperiment_Instrument.removeMetaValue


- Cython signature: void removeMetaValue(String)
- Cython signature: void removeMetaValue(unsigned int)




.. py:method:: TargetedExperiment_Instrument.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)




.. py:method:: TargetedExperiment_Instrument.replaceCVTerms


- Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)
- Cython signature: void replaceCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)




.. py:method:: TargetedExperiment_Instrument.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)




.. py:method:: TargetedExperiment_Instrument.setMetaValue


- Cython signature: void setMetaValue(unsigned int, DataValue)
- Cython signature: void setMetaValue(String, DataValue)




