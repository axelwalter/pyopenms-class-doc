DigestionEnzyme
===============

.. py:class:: DigestionEnzyme


   Bases: :py:class:`object`


Cython implementation of _DigestionEnzyme


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1DigestionEnzyme.html


   Base class for digestion enzymes




.. py:method:: DigestionEnzyme.addSynonym


Cython signature: void addSynonym(const String & synonym)
Adds a synonym




.. py:method:: DigestionEnzyme.getName


Cython signature: String getName()
Returns the name of the enzyme




.. py:method:: DigestionEnzyme.getRegEx


Cython signature: String getRegEx()
Returns the cleavage regex




.. py:method:: DigestionEnzyme.getRegExDescription


Cython signature: String getRegExDescription()
Returns the regex description




.. py:method:: DigestionEnzyme.getSynonyms


Cython signature: libcpp_set[String] getSynonyms()
Returns the synonyms




.. py:method:: DigestionEnzyme.setName


Cython signature: void setName(const String & name)
Sets the name of the enzyme




.. py:method:: DigestionEnzyme.setRegEx


Cython signature: void setRegEx(const String & cleavage_regex)
Sets the cleavage regex




.. py:method:: DigestionEnzyme.setRegExDescription


Cython signature: void setRegExDescription(const String & value)
Sets the regex description




.. py:method:: DigestionEnzyme.setSynonyms


Cython signature: void setSynonyms(libcpp_set[String] & synonyms)
Sets the synonyms




.. py:method:: DigestionEnzyme.setValueFromFile


Cython signature: bool setValueFromFile(String key, String value)
Sets the value of a member variable based on an entry from an input file




