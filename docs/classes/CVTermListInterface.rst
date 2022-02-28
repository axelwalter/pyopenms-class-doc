CVTermListInterface
===================

.. py:class:: CVTermListInterface


   Bases: :py:class:`object`


Cython implementation of _CVTermListInterface


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1CVTermListInterface.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: CVTermListInterface.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)
Adds a CV term




.. py:method:: CVTermListInterface.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: CVTermListInterface.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] & cv_term_map)
Merges the given map into the member map, no duplicate checking




.. py:method:: CVTermListInterface.empty


Cython signature: bool empty()




.. py:method:: CVTermListInterface.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()




.. py:method:: CVTermListInterface.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: CVTermListInterface.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: CVTermListInterface.hasCVTerm


Cython signature: bool hasCVTerm(const String & accession)
Checks whether the term has a value




.. py:method:: CVTermListInterface.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: CVTermListInterface.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: CVTermListInterface.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: CVTermListInterface.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: CVTermListInterface.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & cv_term)




.. py:method:: CVTermListInterface.replaceCVTerms


- Cython signature: void replaceCVTerms(Map[String,libcpp_vector[CVTerm]] & cv_terms)
- Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] & cv_terms, const String & accession)




.. py:method:: CVTermListInterface.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)




.. py:method:: CVTermListInterface.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




