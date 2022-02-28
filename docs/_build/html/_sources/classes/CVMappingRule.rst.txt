CVMappingRule
=============

.. py:class:: CVMappingRule


   Bases: :py:class:`object`


Cython implementation of _CVMappingRule


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1CVMappingRule.html




.. py:attribute:: CVMappingRule.CombinationsLogic


alias of :py:class:`pyopenms.pyopenms_5.__CombinationsLogic`


.. py:attribute:: CVMappingRule.RequirementLevel


alias of :py:class:`pyopenms.pyopenms_5.__RequirementLevel`


.. py:method:: CVMappingRule.addCVTerm


Cython signature: void addCVTerm(CVMappingTerm cv_terms)
Adds a term to the allowed terms




.. py:method:: CVMappingRule.getCVTerms


Cython signature: libcpp_vector[CVMappingTerm] getCVTerms()
Returns the allowed terms




.. py:method:: CVMappingRule.getCombinationsLogic


Cython signature: CombinationsLogic getCombinationsLogic()
Returns the combinations operator of the rule




.. py:method:: CVMappingRule.getElementPath


Cython signature: String getElementPath()
Returns the path of the DOM element, where this rule is allowed




.. py:method:: CVMappingRule.getIdentifier


Cython signature: String getIdentifier()
Returns the identifier of the rule




.. py:method:: CVMappingRule.getRequirementLevel


Cython signature: RequirementLevel getRequirementLevel()
Returns the requirement level of this rule




.. py:method:: CVMappingRule.getScopePath


Cython signature: String getScopePath()
Returns the scope path of the rule




.. py:method:: CVMappingRule.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVMappingTerm] cv_terms)
Sets the terms which are allowed




.. py:method:: CVMappingRule.setCombinationsLogic


Cython signature: void setCombinationsLogic(CombinationsLogic combinations_logic)
Sets the combination operator of the rule




.. py:method:: CVMappingRule.setElementPath


Cython signature: void setElementPath(String element_path)
Sets the path of the DOM element, where this rule is allowed




.. py:method:: CVMappingRule.setIdentifier


Cython signature: void setIdentifier(String identifier)
Sets the identifier of the rule




.. py:method:: CVMappingRule.setRequirementLevel


Cython signature: void setRequirementLevel(RequirementLevel level)
Sets the requirement level of this rule




.. py:method:: CVMappingRule.setScopePath


Cython signature: void setScopePath(String path)
Sets the scope path of the rule




