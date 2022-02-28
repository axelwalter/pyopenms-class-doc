CVTermList
==========

.. py:class:: CVTermList


   Bases: :py:class:`object`


Cython implementation of _CVTermList


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1CVTermList.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: CVTermList.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)
Adds a CV term




.. py:method:: CVTermList.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: CVTermList.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)
Merges the given map into the member map, no duplicate checking




.. py:method:: CVTermList.empty


Cython signature: bool empty()




.. py:method:: CVTermList.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()
Returns the accession string of the term




.. py:method:: CVTermList.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: CVTermList.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: CVTermList.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:method:: CVTermList.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: CVTermList.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: CVTermList.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: CVTermList.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: CVTermList.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)
Replaces the specified CV term




.. py:method:: CVTermList.replaceCVTerms


Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)




.. py:method:: CVTermList.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)
Sets the CV terms




.. py:method:: CVTermList.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




