ProteinIdentification
=====================

.. py:class:: ProteinIdentification


   Bases: :py:class:`object`


Cython implementation of _ProteinIdentification


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProteinIdentification.html
 -- Inherits from ['MetaInfoInterface']




.. py:attribute:: ProteinIdentification.PeakMassType


alias of :py:class:`pyopenms.pyopenms_5.__PeakMassType`


.. py:method:: ProteinIdentification.addPrimaryMSRunPath


- Cython signature: void addPrimaryMSRunPath(StringList & s)
- Cython signature: void addPrimaryMSRunPath(StringList & s, bool raw)




.. py:method:: ProteinIdentification.assignRanks


Cython signature: void assignRanks()
Sorts the protein hits by score and assigns ranks (best score has rank 1)




.. py:method:: ProteinIdentification.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: ProteinIdentification.computeCoverage


Cython signature: void computeCoverage(libcpp_vector[PeptideIdentification] pep_ids)
Compute the coverage (in percent) of all ProteinHits given PeptideHits




.. py:method:: ProteinIdentification.getDateTime


Cython signature: DateTime getDateTime()
Returns the date of the protein identification run




.. py:method:: ProteinIdentification.getHits


Cython signature: libcpp_vector[ProteinHit] getHits()
Returns the protein hits




.. py:method:: ProteinIdentification.getIdentifier


Cython signature: String getIdentifier()
Returns the identifier




.. py:method:: ProteinIdentification.getIndistinguishableProteins


Cython signature: libcpp_vector[ProteinGroup] getIndistinguishableProteins()
Returns the indistinguishable proteins




.. py:method:: ProteinIdentification.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: ProteinIdentification.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: ProteinIdentification.getPrimaryMSRunPath


- Cython signature: void getPrimaryMSRunPath(StringList & output)
- Cython signature: void getPrimaryMSRunPath(StringList & output, bool raw)




.. py:method:: ProteinIdentification.getProteinGroups


Cython signature: libcpp_vector[ProteinGroup] getProteinGroups()
Returns the protein groups




.. py:method:: ProteinIdentification.getScoreType


Cython signature: String getScoreType()
Returns the protein score type




.. py:method:: ProteinIdentification.getSearchEngine


Cython signature: String getSearchEngine()
Returns the type of search engine used




.. py:method:: ProteinIdentification.getSearchEngineVersion


Cython signature: String getSearchEngineVersion()
Returns the search engine version




.. py:method:: ProteinIdentification.getSearchParameters


Cython signature: SearchParameters getSearchParameters()
Returns the search parameters




.. py:method:: ProteinIdentification.getSignificanceThreshold


Cython signature: double getSignificanceThreshold()
Returns the protein significance threshold value




.. py:method:: ProteinIdentification.insertHit


Cython signature: void insertHit(ProteinHit input)
Appends a protein hit




.. py:method:: ProteinIdentification.insertIndistinguishableProteins


Cython signature: void insertIndistinguishableProteins(ProteinGroup group)
Appends new indistinguishable proteins




.. py:method:: ProteinIdentification.insertProteinGroup


Cython signature: void insertProteinGroup(ProteinGroup group)
Appends a new protein group




.. py:method:: ProteinIdentification.isHigherScoreBetter


Cython signature: bool isHigherScoreBetter()
Returns true if a higher score represents a better score




.. py:method:: ProteinIdentification.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: ProteinIdentification.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: ProteinIdentification.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: ProteinIdentification.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: ProteinIdentification.setDateTime


Cython signature: void setDateTime(DateTime date)
Sets the date of the protein identification run




.. py:method:: ProteinIdentification.setHigherScoreBetter


Cython signature: void setHigherScoreBetter(bool higher_is_better)
Sets the orientation of the score (is higher better?)




.. py:method:: ProteinIdentification.setHits


Cython signature: void setHits(libcpp_vector[ProteinHit] hits)
Sets the protein hits




.. py:method:: ProteinIdentification.setIdentifier


Cython signature: void setIdentifier(String id_)
Sets the identifier




.. py:method:: ProteinIdentification.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: ProteinIdentification.setPrimaryMSRunPath


         - Cython signature: void setPrimaryMSRunPath(StringList & s)


Set the file paths to the primary MS runs (usually the mzML files obtained after data conversion from raw files)
-----
:param raw: Store paths to the raw files (or equivalent) rather than mzMLs
         - Cython signature: void setPrimaryMSRunPath(StringList & s, bool raw)




.. py:method:: ProteinIdentification.setScoreType


Cython signature: void setScoreType(String type)
Sets the protein score type




.. py:method:: ProteinIdentification.setSearchEngine


Cython signature: void setSearchEngine(String search_engine)
Sets the search engine type




.. py:method:: ProteinIdentification.setSearchEngineVersion


Cython signature: void setSearchEngineVersion(String search_engine_version)
Sets the search engine version




.. py:method:: ProteinIdentification.setSearchParameters


Cython signature: void setSearchParameters(SearchParameters search_parameters)
Sets the search parameters




.. py:method:: ProteinIdentification.setSignificanceThreshold


Cython signature: void setSignificanceThreshold(double value)
Sets the protein significance threshold value




.. py:method:: ProteinIdentification.sort


Cython signature: void sort()
Sorts the protein hits according to their score




