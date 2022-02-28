CVTerm_ControlledVocabulary
===========================

.. py:class:: CVTerm_ControlledVocabulary


   Bases: :py:class:`object`


Cython implementation of _CVTerm_ControlledVocabulary


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1CVTerm_ControlledVocabulary.html




.. py:attribute:: CVTerm_ControlledVocabulary.children




.. py:attribute:: CVTerm_ControlledVocabulary.description




.. py:method:: CVTerm_ControlledVocabulary.getXRefTypeName


Cython signature: String getXRefTypeName(XRefType_CVTerm_ControlledVocabulary type)




.. py:attribute:: CVTerm_ControlledVocabulary.id




.. py:method:: CVTerm_ControlledVocabulary.isHigherBetterScore


Cython signature: bool isHigherBetterScore(CVTerm_ControlledVocabulary term)




.. py:attribute:: CVTerm_ControlledVocabulary.name




.. py:attribute:: CVTerm_ControlledVocabulary.obsolete




.. py:attribute:: CVTerm_ControlledVocabulary.parents




.. py:attribute:: CVTerm_ControlledVocabulary.synonyms




.. py:method:: CVTerm_ControlledVocabulary.toXMLString


- Cython signature: String toXMLString(String ref, String value)
  Get mzidentml formatted string. i.e. a cvparam xml element, ref should be the name of the ControlledVocabulary (i.e. cv.name()) containing the CVTerm (e.g. PSI-MS for the psi-ms.obo - gets loaded in all cases like that??), value can be empty if not available


- Cython signature: String toXMLString(String ref, DataValue value)
  Get mzidentml formatted string. i.e. a cvparam xml element, ref should be the name of the ControlledVocabulary (i.e. cv.name()) containing the CVTerm (e.g. PSI-MS for the psi-ms.obo - gets loaded in all cases like that??), value can be empty if not available




.. py:attribute:: CVTerm_ControlledVocabulary.units




.. py:attribute:: CVTerm_ControlledVocabulary.unparsed




.. py:attribute:: CVTerm_ControlledVocabulary.xref_binary




.. py:attribute:: CVTerm_ControlledVocabulary.xref_type




