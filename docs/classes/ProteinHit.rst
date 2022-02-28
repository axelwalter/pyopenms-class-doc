ProteinHit
==========

.. py:class:: ProteinHit


   Bases: :py:class:`object`


Cython implementation of _ProteinHit


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProteinHit.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: ProteinHit.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: ProteinHit.getAccession


Cython signature: String getAccession()
Returns the accession of the protein




.. py:method:: ProteinHit.getCoverage


Cython signature: double getCoverage()
Returns the coverage (in percent) of the protein hit based upon matched peptides




.. py:method:: ProteinHit.getDescription


Cython signature: String getDescription()
Returns the description of the protein




.. py:method:: ProteinHit.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: ProteinHit.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: ProteinHit.getRank


Cython signature: unsigned int getRank()
Returns the rank of the protein hit




.. py:method:: ProteinHit.getScore


Cython signature: float getScore()
Returns the score of the protein hit




.. py:method:: ProteinHit.getSequence


Cython signature: String getSequence()
Returns the protein sequence




.. py:method:: ProteinHit.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: ProteinHit.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: ProteinHit.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: ProteinHit.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: ProteinHit.setAccession


Cython signature: void setAccession(String)
Sets the accession of the protein




.. py:method:: ProteinHit.setCoverage


Cython signature: void setCoverage(double)
Sets the coverage (in percent) of the protein hit based upon matched peptides




.. py:method:: ProteinHit.setDescription


Cython signature: void setDescription(String description)
Sets the description of the protein




.. py:method:: ProteinHit.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: ProteinHit.setRank


Cython signature: void setRank(unsigned int)
Sets the rank




.. py:method:: ProteinHit.setScore


Cython signature: void setScore(float)
Sets the score of the protein hit




.. py:method:: ProteinHit.setSequence


Cython signature: void setSequence(String)
Sets the protein sequence




