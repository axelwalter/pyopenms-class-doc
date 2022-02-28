ConsensusMap
============

.. py:class:: ConsensusMap


   Bases: :py:class:`object`


Cython implementation of _ConsensusMap


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::ConsensusMap_1_1ConsensusMap.html
 -- Inherits from ['UniqueIdInterface', 'DocumentIdentifier', 'RangeManagerRtMzInt', 'MetaInfoInterface']


 A container for consensus elements.
 -----
 A ConsensusMap is a container holding 2-dimensional consensus elements
 (ConsensusFeature) which in turn represent analytes that have been
 quantified across multiple LC-MS/MS experiments. Each analyte in a
 ConsensusFeature is linked to its original LC-MS/MS run, the links are
 maintained by the ConsensusMap class.
 The map is implemented as a vector of elements of type ConsensusFeature.
 -----
 To be consistent, all maps who are referenced by ConsensusFeature objects
 (through a unique id) need to be registered in this class.
 -----
 This class supports direct iteration in Python.




.. py:method:: ConsensusMap.appendColumns


Cython signature: ConsensusMap appendColumns(ConsensusMap)
Add consensus map entries as new columns




.. py:method:: ConsensusMap.appendRows


Cython signature: ConsensusMap appendRows(ConsensusMap)
Add consensus map entries as new rows




.. py:method:: ConsensusMap.clear


- Cython signature: void clear(bool clear_meta_data)
  Clears all data and meta data


- Cython signature: void clear()




.. py:method:: ConsensusMap.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: ConsensusMap.clearRanges


Cython signature: void clearRanges()
Resets all range dimensions as empty




.. py:method:: ConsensusMap.clearUniqueId


Cython signature: size_t clearUniqueId()
Clear the unique id. The new unique id will be invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: ConsensusMap.empty


Cython signature: bool empty()




.. py:method:: ConsensusMap.ensureUniqueId


Cython signature: size_t ensureUniqueId()
Assigns a valid unique id, but only if the present one is invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: ConsensusMap.getColumnHeaders




.. py:method:: ConsensusMap.getDataProcessing


Cython signature: libcpp_vector[DataProcessing] getDataProcessing()
Returns a const reference to the description of the applied data processing




.. py:method:: ConsensusMap.getExperimentType


Cython signature: String getExperimentType()
Non-mutable access to the experiment type




.. py:method:: ConsensusMap.getIdentifier


Cython signature: String getIdentifier()
Retrieve document identifier (e.g. an LSID)




.. py:method:: ConsensusMap.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: ConsensusMap.getLoadedFilePath


Cython signature: String getLoadedFilePath()
Returns the file_name which is the absolute path to the file loaded




.. py:method:: ConsensusMap.getLoadedFileType


Cython signature: int getLoadedFileType()
Returns the file_type (e.g. featureXML, consensusXML, mzData, mzXML, mzML, ...) of the file loaded




.. py:method:: ConsensusMap.getMaxIntensity


Cython signature: double getMaxIntensity()
Returns the maximum intensity




.. py:method:: ConsensusMap.getMaxMZ


Cython signature: double getMaxMZ()
Returns the maximum m/z




.. py:method:: ConsensusMap.getMaxRT


Cython signature: double getMaxRT()
Returns the maximum RT




.. py:method:: ConsensusMap.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: ConsensusMap.getMinIntensity


Cython signature: double getMinIntensity()
Returns the minimum intensity




.. py:method:: ConsensusMap.getMinMZ


Cython signature: double getMinMZ()
Returns the minimum m/z




.. py:method:: ConsensusMap.getMinRT


Cython signature: double getMinRT()
Returns the minimum RT




.. py:method:: ConsensusMap.getPrimaryMSRunPath


Cython signature: void getPrimaryMSRunPath(StringList & toFill)
Returns the MS run path (stored in ColumnHeaders)




.. py:method:: ConsensusMap.getProteinIdentifications


Cython signature: libcpp_vector[ProteinIdentification] getProteinIdentifications()




.. py:method:: ConsensusMap.getUnassignedPeptideIdentifications


Cython signature: libcpp_vector[PeptideIdentification] getUnassignedPeptideIdentifications()




.. py:method:: ConsensusMap.getUniqueId


Cython signature: size_t getUniqueId()
Returns the unique id




.. py:method:: ConsensusMap.hasInvalidUniqueId


Cython signature: size_t hasInvalidUniqueId()
Returns whether the unique id is invalid. Returns 1 if the unique id is invalid, 0 otherwise




.. py:method:: ConsensusMap.hasValidUniqueId


Cython signature: size_t hasValidUniqueId()
Returns whether the unique id is valid. Returns 1 if the unique id is valid, 0 otherwise




.. py:method:: ConsensusMap.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: ConsensusMap.isValid


Cython signature: bool isValid(uint64_t unique_id)
Returns true if the unique_id is valid, false otherwise




.. py:method:: ConsensusMap.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: ConsensusMap.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: ConsensusMap.push_back


Cython signature: void push_back(ConsensusFeature spec)




.. py:method:: ConsensusMap.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: ConsensusMap.reserve


Cython signature: void reserve(size_t s)




.. py:method:: ConsensusMap.setColumnHeaders




.. py:method:: ConsensusMap.setDataProcessing


Cython signature: void setDataProcessing(libcpp_vector[DataProcessing])
Sets the description of the applied data processing




.. py:method:: ConsensusMap.setExperimentType


Cython signature: void setExperimentType(String experiment_type)
Mutable access to the experiment type




.. py:method:: ConsensusMap.setIdentifier


Cython signature: void setIdentifier(String id)
Sets document identifier (e.g. an LSID)




.. py:method:: ConsensusMap.setLoadedFilePath


Cython signature: void setLoadedFilePath(String file_name)
Sets the file_name according to absolute path of the file loaded, preferably done whilst loading




.. py:method:: ConsensusMap.setLoadedFileType


Cython signature: void setLoadedFileType(String file_name)
Sets the file_type according to the type of the file loaded from, preferably done whilst loading




.. py:method:: ConsensusMap.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: ConsensusMap.setPrimaryMSRunPath


- Cython signature: void setPrimaryMSRunPath(StringList & s)
  Sets the file paths to the primary MS run (stored in ColumnHeaders)


- Cython signature: void setPrimaryMSRunPath(StringList & s, MSExperiment & e)




.. py:method:: ConsensusMap.setProteinIdentifications


Cython signature: void setProteinIdentifications(libcpp_vector[ProteinIdentification])
Sets the protein identifications




.. py:method:: ConsensusMap.setUnassignedPeptideIdentifications


Cython signature: void setUnassignedPeptideIdentifications(libcpp_vector[PeptideIdentification])
Sets the unassigned peptide identifications




.. py:method:: ConsensusMap.setUniqueId


Cython signature: void setUniqueId(uint64_t rhs)
Assigns a new, valid unique id. Always returns 1




.. py:method:: ConsensusMap.setUniqueIds




.. py:method:: ConsensusMap.size


Cython signature: int size()




.. py:method:: ConsensusMap.sortByIntensity


- Cython signature: void sortByIntensity(bool reverse)
  Sorts the peaks according to ascending intensity.


- Cython signature: void sortByIntensity()




.. py:method:: ConsensusMap.sortByMZ


Cython signature: void sortByMZ()
Sorts the peaks according to m/z position




.. py:method:: ConsensusMap.sortByMaps


Cython signature: void sortByMaps()
Sorts with respect to the sets of maps covered by the consensus features (lexicographically)




.. py:method:: ConsensusMap.sortByPosition


Cython signature: void sortByPosition()
Lexicographically sorts the peaks by their position (First RT then m/z)




.. py:method:: ConsensusMap.sortByQuality


- Cython signature: void sortByQuality(bool reverse)
  Sorts the peaks according to ascending quality.


- Cython signature: void sortByQuality()




.. py:method:: ConsensusMap.sortByRT


Cython signature: void sortByRT()
Sorts the peaks according to RT position




.. py:method:: ConsensusMap.sortBySize


Cython signature: void sortBySize()
Sorts with respect to the size (number of elements)




.. py:method:: ConsensusMap.sortPeptideIdentificationsByMapIndex


Cython signature: void sortPeptideIdentificationsByMapIndex()
Sorts PeptideIdentifications of consensus features with respect to their map index.




.. py:method:: ConsensusMap.updateRanges


Cython signature: void updateRanges()




