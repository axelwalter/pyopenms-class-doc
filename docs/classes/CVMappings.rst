CVMappings
==========

.. py:class:: CVMappings


   Bases: :py:class:`object`


Cython implementation of _CVMappings


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1CVMappings.html




.. py:method:: CVMappings.addCVReference


Cython signature: void addCVReference(CVReference & cv_reference)
Adds a CV reference




.. py:method:: CVMappings.addMappingRule


Cython signature: void addMappingRule(CVMappingRule & cv_mapping_rule)
Adds a mapping rule




.. py:method:: CVMappings.getCVReferences


Cython signature: libcpp_vector[CVReference] getCVReferences()
Returns the CV references




.. py:method:: CVMappings.getMappingRules


Cython signature: libcpp_vector[CVMappingRule] getMappingRules()
Returns the mapping rules




.. py:method:: CVMappings.hasCVReference


Cython signature: bool hasCVReference(const String & identifier)
Returns true if a CV reference is given




.. py:method:: CVMappings.setCVReferences


Cython signature: void setCVReferences(libcpp_vector[CVReference] & cv_references)
Sets the CV references




.. py:method:: CVMappings.setMappingRules


Cython signature: void setMappingRules(libcpp_vector[CVMappingRule] & cv_mapping_rules)
Sets the mapping rules of the mapping file




