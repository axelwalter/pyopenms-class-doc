DigestionEnzymeRNA
==================

.. py:class:: DigestionEnzymeRNA


   Bases: :py:class:`object`


Cython implementation of _DigestionEnzymeRNA


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1DigestionEnzymeRNA.html
 -- Inherits from ['DigestionEnzyme']


 Representation of a digestion enzyme for RNA (RNase)
 -----
 The cutting sites of these enzymes are defined using two different mechanisms:
 First, a single regular expression that is applied to strings of unmodified RNA sequence and defines cutting sites via zero-length matches (using lookahead/lookbehind assertions).
 This is the same mechanism that is used for proteases (see ProteaseDigestion).
 However, due to the complex notation involved, this approach is not practical for modification-aware digestion.
 Thus, the second mechanism uses two regular expressions ("cuts after"/"cuts before"), which are applied to the short codes (e.g. "m6A") of sequential ribonucleotides.
 If both expressions match, then there is a cutting site between the two ribonucleotides.
 -----
 There is support for terminal (5'/3') modifications that may be generated on fragments as a result of RNase cleavage.
 A typical example is 3'-phosphate, resulting from cleavage of the phosphate backbone.




.. py:method:: DigestionEnzymeRNA.addSynonym


Cython signature: void addSynonym(const String & synonym)
Adds a synonym




.. py:method:: DigestionEnzymeRNA.getCutsAfterRegEx


Cython signature: String getCutsAfterRegEx()
Returns the "cuts after ..." regular expression




.. py:method:: DigestionEnzymeRNA.getCutsBeforeRegEx


Cython signature: String getCutsBeforeRegEx()
Returns the "cuts before ..." regular expression




.. py:method:: DigestionEnzymeRNA.getFivePrimeGain


Cython signature: String getFivePrimeGain()
Returns the 5' gain




.. py:method:: DigestionEnzymeRNA.getName


Cython signature: String getName()
Returns the name of the enzyme




.. py:method:: DigestionEnzymeRNA.getRegEx


Cython signature: String getRegEx()
Returns the cleavage regex




.. py:method:: DigestionEnzymeRNA.getRegExDescription


Cython signature: String getRegExDescription()
Returns the regex description




.. py:method:: DigestionEnzymeRNA.getSynonyms


Cython signature: libcpp_set[String] getSynonyms()
Returns the synonyms




.. py:method:: DigestionEnzymeRNA.getThreePrimeGain


Cython signature: String getThreePrimeGain()
Returns the 3' gain




.. py:method:: DigestionEnzymeRNA.setCutsAfterRegEx


Cython signature: void setCutsAfterRegEx(String value)
Sets the "cuts after ..." regular expression




.. py:method:: DigestionEnzymeRNA.setCutsBeforeRegEx


Cython signature: void setCutsBeforeRegEx(String value)
Sets the "cuts before ..." regular expression




.. py:method:: DigestionEnzymeRNA.setFivePrimeGain


Cython signature: void setFivePrimeGain(String value)
Sets the 5' gain




.. py:method:: DigestionEnzymeRNA.setName


Cython signature: void setName(const String & name)
Sets the name of the enzyme




.. py:method:: DigestionEnzymeRNA.setRegEx


Cython signature: void setRegEx(const String & cleavage_regex)
Sets the cleavage regex




.. py:method:: DigestionEnzymeRNA.setRegExDescription


Cython signature: void setRegExDescription(const String & value)
Sets the regex description




.. py:method:: DigestionEnzymeRNA.setSynonyms


Cython signature: void setSynonyms(libcpp_set[String] & synonyms)
Sets the synonyms




.. py:method:: DigestionEnzymeRNA.setThreePrimeGain


Cython signature: void setThreePrimeGain(String value)
Sets the 3' gain




.. py:method:: DigestionEnzymeRNA.setValueFromFile


Cython signature: bool setValueFromFile(String key, String value)
Sets the value of a member variable based on an entry from an input file




