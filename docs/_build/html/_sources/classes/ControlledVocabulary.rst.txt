ControlledVocabulary
====================

.. py:class:: ControlledVocabulary


   Bases: :py:class:`object`


Cython implementation of _ControlledVocabulary


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ControlledVocabulary.html




.. py:method:: ControlledVocabulary.exists


Cython signature: bool exists(String id)
Returns true if the term is in the CV. Returns false otherwise.




.. py:method:: ControlledVocabulary.getAllChildTerms


Cython signature: void getAllChildTerms(libcpp_set[String] terms, String parent)
Writes all child terms recursively into terms




.. py:method:: ControlledVocabulary.getTerm


Cython signature: CVTerm_ControlledVocabulary getTerm(String id)
Returns a term specified by ID




.. py:method:: ControlledVocabulary.getTermByName


Cython signature: CVTerm_ControlledVocabulary getTermByName(String name, String desc)
Returns a term specified by name




.. py:method:: ControlledVocabulary.hasTermWithName


Cython signature: bool hasTermWithName(String name)
Returns true if a term with the given name is in the CV. Returns false otherwise




.. py:method:: ControlledVocabulary.isChildOf


Cython signature: bool isChildOf(String child, String parent)
Returns True if `child` is a child of `parent`




.. py:method:: ControlledVocabulary.loadFromOBO


Cython signature: void loadFromOBO(String name, String filename)
Loads the CV from an OBO file




.. py:method:: ControlledVocabulary.name


Cython signature: String name()
Returns the CV name (set in the load method)




