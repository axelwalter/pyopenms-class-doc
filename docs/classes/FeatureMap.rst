FeatureMap
==========

.. py:class:: FeatureMap


   Bases: :py:class:`object`


Cython implementation of _FeatureMap


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureMap.html
 -- Inherits from ['UniqueIdInterface', 'DocumentIdentifier', 'RangeManagerRtMzInt', 'MetaInfoInterface']


 A container for features.
 -----
 A feature map is a container holding features, which represent
 chemical entities (peptides, proteins, small molecules etc.) found
 in an LC-MS/MS experiment.
 -----
 This class supports direct iteration in Python.




.. py:method:: FeatureMap.clear


- Cython signature: void clear()
  Clears all data and meta data


- Cython signature: void clear(bool clear_meta_data)
  Clears all data and meta data. If 'true' is passed as an argument, all meta data is cleared in addition to the data




.. py:method:: FeatureMap.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: FeatureMap.clearRanges


Cython signature: void clearRanges()
Resets all range dimensions as empty




.. py:method:: FeatureMap.clearUniqueId


Cython signature: size_t clearUniqueId()
Clear the unique id. The new unique id will be invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: FeatureMap.ensureUniqueId


Cython signature: size_t ensureUniqueId()
Assigns a valid unique id, but only if the present one is invalid. Returns 1 if the unique id was changed, 0 otherwise




.. py:method:: FeatureMap.getDataProcessing


Cython signature: libcpp_vector[DataProcessing] getDataProcessing()




.. py:method:: FeatureMap.getIdentifier


Cython signature: String getIdentifier()
Retrieve document identifier (e.g. an LSID)




.. py:method:: FeatureMap.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: FeatureMap.getLoadedFilePath


Cython signature: String getLoadedFilePath()
Returns the file_name which is the absolute path to the file loaded




.. py:method:: FeatureMap.getLoadedFileType


Cython signature: int getLoadedFileType()
Returns the file_type (e.g. featureXML, consensusXML, mzData, mzXML, mzML, ...) of the file loaded




.. py:method:: FeatureMap.getMaxIntensity


Cython signature: double getMaxIntensity()
Returns the maximum intensity




.. py:method:: FeatureMap.getMaxMZ


Cython signature: double getMaxMZ()
Returns the maximum m/z




.. py:method:: FeatureMap.getMaxRT


Cython signature: double getMaxRT()
Returns the maximum RT




.. py:method:: FeatureMap.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: FeatureMap.getMinIntensity


Cython signature: double getMinIntensity()
Returns the minimum intensity




.. py:method:: FeatureMap.getMinMZ


Cython signature: double getMinMZ()
Returns the minimum m/z




.. py:method:: FeatureMap.getMinRT


Cython signature: double getMinRT()
Returns the minimum RT




.. py:method:: FeatureMap.getPrimaryMSRunPath


Cython signature: void getPrimaryMSRunPath(StringList & toFill)
Returns the file path to the first MS run




.. py:method:: FeatureMap.getProteinIdentifications


Cython signature: libcpp_vector[ProteinIdentification] getProteinIdentifications()




.. py:method:: FeatureMap.getUnassignedPeptideIdentifications


Cython signature: libcpp_vector[PeptideIdentification] getUnassignedPeptideIdentifications()




.. py:method:: FeatureMap.getUniqueId


Cython signature: size_t getUniqueId()
Returns the unique id




.. py:method:: FeatureMap.hasInvalidUniqueId


Cython signature: size_t hasInvalidUniqueId()
Returns whether the unique id is invalid. Returns 1 if the unique id is invalid, 0 otherwise




.. py:method:: FeatureMap.hasValidUniqueId


Cython signature: size_t hasValidUniqueId()
Returns whether the unique id is valid. Returns 1 if the unique id is valid, 0 otherwise




.. py:method:: FeatureMap.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: FeatureMap.isValid


Cython signature: bool isValid(uint64_t unique_id)
Returns true if the unique_id is valid, false otherwise




.. py:method:: FeatureMap.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: FeatureMap.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: FeatureMap.push_back


- Cython signature: void push_back(Feature spec)
- Cython signature: void push_back(MRMFeature spec)




.. py:method:: FeatureMap.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: FeatureMap.setDataProcessing


Cython signature: void setDataProcessing(libcpp_vector[DataProcessing])
Sets the description of the applied data processing




.. py:method:: FeatureMap.setIdentifier


Cython signature: void setIdentifier(String id)
Sets document identifier (e.g. an LSID)




.. py:method:: FeatureMap.setLoadedFilePath


Cython signature: void setLoadedFilePath(String file_name)
Sets the file_name according to absolute path of the file loaded, preferably done whilst loading




.. py:method:: FeatureMap.setLoadedFileType


Cython signature: void setLoadedFileType(String file_name)
Sets the file_type according to the type of the file loaded from, preferably done whilst loading




.. py:method:: FeatureMap.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: FeatureMap.setPrimaryMSRunPath


- Cython signature: void setPrimaryMSRunPath(StringList & s)
  Sets the file path to the primary MS run (usually the mzML file obtained after data conversion from raw files)


- Cython signature: void setPrimaryMSRunPath(StringList & s, MSExperiment & e)
  Sets the file path to the primary MS run using the mzML annotated in the MSExperiment argument `e`




.. py:method:: FeatureMap.setProteinIdentifications


Cython signature: void setProteinIdentifications(libcpp_vector[ProteinIdentification])
Sets the protein identifications




.. py:method:: FeatureMap.setUnassignedPeptideIdentifications


Cython signature: void setUnassignedPeptideIdentifications(libcpp_vector[PeptideIdentification])
Sets the unassigned peptide identifications




.. py:method:: FeatureMap.setUniqueId


Cython signature: void setUniqueId(uint64_t rhs)
Assigns a new, valid unique id. Always returns 1




.. py:method:: FeatureMap.setUniqueIds




.. py:method:: FeatureMap.size


Cython signature: int size()




.. py:method:: FeatureMap.sortByIntensity


- Cython signature: void sortByIntensity()
  Sorts the peaks according to ascending intensity


- Cython signature: void sortByIntensity(bool reverse)
  Sorts the peaks according to ascending intensity. Order is reversed if argument is `true` ( reverse = true )




.. py:method:: FeatureMap.sortByMZ


Cython signature: void sortByMZ()
Sorts features by m/z position




.. py:method:: FeatureMap.sortByOverallQuality


Cython signature: void sortByOverallQuality()
Sorts features by ascending overall quality. Order is reversed if argument is `true` ( reverse = true )




.. py:method:: FeatureMap.sortByPosition


Cython signature: void sortByPosition()
Sorts features by position. Lexicographical comparison (first RT then m/z) is done




.. py:method:: FeatureMap.sortByRT


Cython signature: void sortByRT()
Sorts features by RT position




.. py:method:: FeatureMap.swap


Cython signature: void swap(FeatureMap &)




.. py:method:: FeatureMap.swapFeaturesOnly


Cython signature: void swapFeaturesOnly(FeatureMap swapfrom)
Swaps the feature content (plus its range information) of this map




.. py:method:: FeatureMap.updateRanges


Cython signature: void updateRanges()




