RetentionTime
=============

.. py:class:: RetentionTime


   Bases: :py:class:`object`


Cython implementation of _RetentionTime


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::TargetedExperimentHelper::RetentionTime::RTUnit_1_1RetentionTime.html
 -- Inherits from ['CVTermList']




.. py:attribute:: RetentionTime.RTType


alias of :py:class:`pyopenms.pyopenms_7.__RTType`


.. py:attribute:: RetentionTime.RTUnit


alias of :py:class:`pyopenms.pyopenms_7.__RTUnit`


.. py:method:: RetentionTime.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)
Adds a CV term




.. py:method:: RetentionTime.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: RetentionTime.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)
Merges the given map into the member map, no duplicate checking




.. py:method:: RetentionTime.empty


Cython signature: bool empty()




.. py:method:: RetentionTime.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()
Returns the accession string of the term




.. py:method:: RetentionTime.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: RetentionTime.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: RetentionTime.getRT


Cython signature: double getRT()




.. py:method:: RetentionTime.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:method:: RetentionTime.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: RetentionTime.isRTset


Cython signature: bool isRTset()




.. py:method:: RetentionTime.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: RetentionTime.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: RetentionTime.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: RetentionTime.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)
Replaces the specified CV term




.. py:method:: RetentionTime.replaceCVTerms


Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)




.. py:attribute:: RetentionTime.retention_time_type




.. py:attribute:: RetentionTime.retention_time_unit




.. py:method:: RetentionTime.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)
Sets the CV terms




.. py:method:: RetentionTime.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: RetentionTime.setRT


Cython signature: void setRT(double rt)




.. py:attribute:: RetentionTime.software_ref




