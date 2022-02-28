Configuration
=============

.. py:class:: Configuration


   Bases: :py:class:`object`


Cython implementation of _Configuration


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::TargetedExperimentHelper::RetentionTime::RTUnit_1_1Configuration.html
 -- Inherits from ['CVTermList']




.. py:method:: Configuration.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)
Adds a CV term




.. py:method:: Configuration.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: Configuration.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)
Merges the given map into the member map, no duplicate checking




.. py:attribute:: Configuration.contact_ref




.. py:method:: Configuration.empty


Cython signature: bool empty()




.. py:method:: Configuration.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()
Returns the accession string of the term




.. py:method:: Configuration.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: Configuration.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: Configuration.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:attribute:: Configuration.instrument_ref




.. py:method:: Configuration.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: Configuration.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: Configuration.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: Configuration.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: Configuration.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)
Replaces the specified CV term




.. py:method:: Configuration.replaceCVTerms


Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)




.. py:method:: Configuration.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)
Sets the CV terms




.. py:method:: Configuration.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:attribute:: Configuration.validations




