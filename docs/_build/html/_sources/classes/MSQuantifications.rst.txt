MSQuantifications
=================

.. py:class:: MSQuantifications


   Bases: :py:class:`object`


Cython implementation of _MSQuantifications


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSQuantifications.html
 -- Inherits from ['ExperimentalSettings']




.. py:attribute:: MSQuantifications.QUANT_TYPES


alias of :py:class:`pyopenms.pyopenms_5.__QUANT_TYPES`


.. py:method:: MSQuantifications.addConsensusMap


Cython signature: void addConsensusMap(ConsensusMap m)




.. py:method:: MSQuantifications.assignUIDs


Cython signature: void assignUIDs()




.. py:method:: MSQuantifications.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: MSQuantifications.getAnalysisSummary


Cython signature: AnalysisSummary getAnalysisSummary()




.. py:method:: MSQuantifications.getAssays


Cython signature: libcpp_vector[Assay] getAssays()




.. py:method:: MSQuantifications.getComment


Cython signature: String getComment()
Returns the free-text comment




.. py:method:: MSQuantifications.getConsensusMaps


Cython signature: libcpp_vector[ConsensusMap] getConsensusMaps()




.. py:method:: MSQuantifications.getContacts


Cython signature: libcpp_vector[ContactPerson] getContacts()
Returns a reference to the list of contact persons




.. py:method:: MSQuantifications.getDataProcessingList


Cython signature: libcpp_vector[DataProcessing] getDataProcessingList()




.. py:method:: MSQuantifications.getDateTime


Cython signature: DateTime getDateTime()
Returns the date the experiment was performed




.. py:method:: MSQuantifications.getFeatureMaps


Cython signature: libcpp_vector[FeatureMap] getFeatureMaps()




.. py:method:: MSQuantifications.getFractionIdentifier


Cython signature: String getFractionIdentifier()
Returns fraction identifier




.. py:method:: MSQuantifications.getHPLC


Cython signature: HPLC getHPLC()
Returns a reference to the description of the HPLC run




.. py:method:: MSQuantifications.getIdentifier


Cython signature: String getIdentifier()
Retrieve document identifier (e.g. an LSID)




.. py:method:: MSQuantifications.getInstrument


Cython signature: Instrument getInstrument()
Returns a reference to the MS instrument description




.. py:method:: MSQuantifications.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: MSQuantifications.getLoadedFilePath


Cython signature: String getLoadedFilePath()
Returns the file_name which is the absolute path to the file loaded




.. py:method:: MSQuantifications.getLoadedFileType


Cython signature: int getLoadedFileType()
Returns the file_type (e.g. featureXML, consensusXML, mzData, mzXML, mzML, ...) of the file loaded




.. py:method:: MSQuantifications.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: MSQuantifications.getProteinIdentifications


Cython signature: libcpp_vector[ProteinIdentification] getProteinIdentifications()
Returns a reference to the protein ProteinIdentification vector




.. py:method:: MSQuantifications.getSample


Cython signature: Sample getSample()
Returns a reference to the sample description




.. py:method:: MSQuantifications.getSourceFiles


Cython signature: libcpp_vector[SourceFile] getSourceFiles()
Returns a reference to the source data file




.. py:method:: MSQuantifications.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: MSQuantifications.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: MSQuantifications.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: MSQuantifications.registerExperiment




.. py:method:: MSQuantifications.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: MSQuantifications.setAnalysisSummaryQuantType


Cython signature: void setAnalysisSummaryQuantType(QUANT_TYPES r)




.. py:method:: MSQuantifications.setComment


Cython signature: void setComment(String comment)
Sets the free-text comment




.. py:method:: MSQuantifications.setConsensusMaps


Cython signature: void setConsensusMaps(libcpp_vector[ConsensusMap])




.. py:method:: MSQuantifications.setContacts


Cython signature: void setContacts(libcpp_vector[ContactPerson] contacts)
Sets the list of contact persons




.. py:method:: MSQuantifications.setDataProcessingList


Cython signature: void setDataProcessingList(libcpp_vector[DataProcessing] dpl)




.. py:method:: MSQuantifications.setDateTime


Cython signature: void setDateTime(DateTime date_time)
Sets the date the experiment was performed




.. py:method:: MSQuantifications.setFractionIdentifier


Cython signature: void setFractionIdentifier(String fraction_identifier)
Sets the fraction identifier




.. py:method:: MSQuantifications.setHPLC


Cython signature: void setHPLC(HPLC hplc)
Sets the description of the HPLC run




.. py:method:: MSQuantifications.setIdentifier


Cython signature: void setIdentifier(String id)
Sets document identifier (e.g. an LSID)




.. py:method:: MSQuantifications.setInstrument


Cython signature: void setInstrument(Instrument instrument)
Sets the MS instrument description




.. py:method:: MSQuantifications.setLoadedFilePath


Cython signature: void setLoadedFilePath(String file_name)
Sets the file_name according to absolute path of the file loaded, preferably done whilst loading




.. py:method:: MSQuantifications.setLoadedFileType


Cython signature: void setLoadedFileType(String file_name)
Sets the file_type according to the type of the file loaded from, preferably done whilst loading




.. py:method:: MSQuantifications.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: MSQuantifications.setProteinIdentifications


Cython signature: void setProteinIdentifications(libcpp_vector[ProteinIdentification] protein_identifications)
Sets the protein ProteinIdentification vector




.. py:method:: MSQuantifications.setSample


Cython signature: void setSample(Sample sample)
Sets the sample description




.. py:method:: MSQuantifications.setSourceFiles


Cython signature: void setSourceFiles(libcpp_vector[SourceFile] source_files)
Sets the source data file




