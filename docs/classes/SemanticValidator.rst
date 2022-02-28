SemanticValidator
=================

.. py:class:: SemanticValidator


   Bases: :py:class:`object`


Cython implementation of _SemanticValidator


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::Internal_1_1SemanticValidator.html




.. py:method:: SemanticValidator.locateTerm


Cython signature: bool locateTerm(String path, SemanticValidator_CVTerm & parsed_term)
Checks if a CVTerm is allowed in a given path




.. py:method:: SemanticValidator.setAccessionAttribute


Cython signature: void setAccessionAttribute(String accession)
Sets the name of the attribute for accessions in the CV parameter tag name (default 'accession')




.. py:method:: SemanticValidator.setCheckTermValueTypes


Cython signature: void setCheckTermValueTypes(bool check)
Sets if CV term value types should be check (enabled by default)




.. py:method:: SemanticValidator.setCheckUnits


Cython signature: void setCheckUnits(bool check)
Sets if CV term units should be check (disabled by default)




.. py:method:: SemanticValidator.setNameAttribute


Cython signature: void setNameAttribute(String name)
Sets the name of the attribute for accessions in the CV parameter tag name (default 'name')




.. py:method:: SemanticValidator.setTag


Cython signature: void setTag(String tag)
Sets the CV parameter tag name (default 'cvParam')




.. py:method:: SemanticValidator.setUnitAccessionAttribute


Cython signature: void setUnitAccessionAttribute(String accession)
Sets the name of the unit accession attribute (default 'unitAccession')




.. py:method:: SemanticValidator.setUnitNameAttribute


Cython signature: void setUnitNameAttribute(String name)
Sets the name of the unit name attribute (default 'unitName')




.. py:method:: SemanticValidator.setValueAttribute


Cython signature: void setValueAttribute(String value)
Sets the name of the attribute for accessions in the CV parameter tag name (default 'value')




.. py:method:: SemanticValidator.validate


Cython signature: bool validate(String filename, StringList errors, StringList warnings)




