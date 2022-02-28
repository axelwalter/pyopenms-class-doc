CVMappingTerm
=============

.. py:class:: CVMappingTerm


   Bases: :py:class:`object`


Cython implementation of _CVMappingTerm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1CVMappingTerm.html




.. py:method:: CVMappingTerm.getAccession


Cython signature: String getAccession()
Returns the accession string of the term




.. py:method:: CVMappingTerm.getAllowChildren


Cython signature: bool getAllowChildren()
Returns true if the children of this term are allowed to be used




.. py:method:: CVMappingTerm.getCVIdentifierRef


Cython signature: String getCVIdentifierRef()
Returns the CV identifier reference string




.. py:method:: CVMappingTerm.getIsRepeatable


Cython signature: bool getIsRepeatable()
Returns true if this term can be repeated, false otherwise




.. py:method:: CVMappingTerm.getTermName


Cython signature: String getTermName()
Returns the name of the term




.. py:method:: CVMappingTerm.getUseTerm


Cython signature: bool getUseTerm()
Returns true if the term can be used, false if only children are allowed




.. py:method:: CVMappingTerm.getUseTermName


Cython signature: bool getUseTermName()
Returns whether the term name should be used, instead of the accession




.. py:method:: CVMappingTerm.setAccession


Cython signature: void setAccession(String accession)
Sets the accession string of the term




.. py:method:: CVMappingTerm.setAllowChildren


Cython signature: void setAllowChildren(bool allow_children)
Sets whether children of this term are allowed




.. py:method:: CVMappingTerm.setCVIdentifierRef


Cython signature: void setCVIdentifierRef(String cv_identifier_ref)
Sets the CV identifier reference string, e.g. UO for unit obo




.. py:method:: CVMappingTerm.setIsRepeatable


Cython signature: void setIsRepeatable(bool is_repeatable)
Sets whether this term can be repeated




.. py:method:: CVMappingTerm.setTermName


Cython signature: void setTermName(String term_name)
Sets the name of the term




.. py:method:: CVMappingTerm.setUseTerm


Cython signature: void setUseTerm(bool use_term)
Sets whether the term itself can be used (or only its children)




.. py:method:: CVMappingTerm.setUseTermName


Cython signature: void setUseTermName(bool use_term_name)
Sets whether the term name should be used, instead of the accession




