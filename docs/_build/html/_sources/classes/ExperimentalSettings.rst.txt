ExperimentalSettings
====================

.. py:class:: ExperimentalSettings


   Bases: :py:class:`object`


Cython implementation of _ExperimentalSettings


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ExperimentalSettings.html
 -- Inherits from ['DocumentIdentifier', 'MetaInfoInterface']


 Description of the experimental settings, provides meta-information
 about an LC-MS/MS injection.




.. py:method:: ExperimentalSettings.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: ExperimentalSettings.getComment


Cython signature: String getComment()
Returns the free-text comment




.. py:method:: ExperimentalSettings.getContacts


Cython signature: libcpp_vector[ContactPerson] getContacts()
Returns a reference to the list of contact persons




.. py:method:: ExperimentalSettings.getDateTime


Cython signature: DateTime getDateTime()
Returns the date the experiment was performed




.. py:method:: ExperimentalSettings.getFractionIdentifier


Cython signature: String getFractionIdentifier()
Returns fraction identifier




.. py:method:: ExperimentalSettings.getHPLC


Cython signature: HPLC getHPLC()
Returns a reference to the description of the HPLC run




.. py:method:: ExperimentalSettings.getIdentifier


Cython signature: String getIdentifier()
Retrieve document identifier (e.g. an LSID)




.. py:method:: ExperimentalSettings.getInstrument


Cython signature: Instrument getInstrument()
Returns a reference to the MS instrument description




.. py:method:: ExperimentalSettings.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: ExperimentalSettings.getLoadedFilePath


Cython signature: String getLoadedFilePath()
Returns the file_name which is the absolute path to the file loaded




.. py:method:: ExperimentalSettings.getLoadedFileType


Cython signature: int getLoadedFileType()
Returns the file_type (e.g. featureXML, consensusXML, mzData, mzXML, mzML, ...) of the file loaded




.. py:method:: ExperimentalSettings.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: ExperimentalSettings.getProteinIdentifications


Cython signature: libcpp_vector[ProteinIdentification] getProteinIdentifications()
Returns a reference to the protein ProteinIdentification vector




.. py:method:: ExperimentalSettings.getSample


Cython signature: Sample getSample()
Returns a reference to the sample description




.. py:method:: ExperimentalSettings.getSourceFiles


Cython signature: libcpp_vector[SourceFile] getSourceFiles()
Returns a reference to the source data file




.. py:method:: ExperimentalSettings.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: ExperimentalSettings.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: ExperimentalSettings.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: ExperimentalSettings.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: ExperimentalSettings.setComment


Cython signature: void setComment(String comment)
Sets the free-text comment




.. py:method:: ExperimentalSettings.setContacts


Cython signature: void setContacts(libcpp_vector[ContactPerson] contacts)
Sets the list of contact persons




.. py:method:: ExperimentalSettings.setDateTime


Cython signature: void setDateTime(DateTime date_time)
Sets the date the experiment was performed




.. py:method:: ExperimentalSettings.setFractionIdentifier


Cython signature: void setFractionIdentifier(String fraction_identifier)
Sets the fraction identifier




.. py:method:: ExperimentalSettings.setHPLC


Cython signature: void setHPLC(HPLC hplc)
Sets the description of the HPLC run




.. py:method:: ExperimentalSettings.setIdentifier


Cython signature: void setIdentifier(String id)
Sets document identifier (e.g. an LSID)




.. py:method:: ExperimentalSettings.setInstrument


Cython signature: void setInstrument(Instrument instrument)
Sets the MS instrument description




.. py:method:: ExperimentalSettings.setLoadedFilePath


Cython signature: void setLoadedFilePath(String file_name)
Sets the file_name according to absolute path of the file loaded, preferably done whilst loading




.. py:method:: ExperimentalSettings.setLoadedFileType


Cython signature: void setLoadedFileType(String file_name)
Sets the file_type according to the type of the file loaded from, preferably done whilst loading




.. py:method:: ExperimentalSettings.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: ExperimentalSettings.setProteinIdentifications


Cython signature: void setProteinIdentifications(libcpp_vector[ProteinIdentification] protein_identifications)
Sets the protein ProteinIdentification vector




.. py:method:: ExperimentalSettings.setSample


Cython signature: void setSample(Sample sample)
Sets the sample description




.. py:method:: ExperimentalSettings.setSourceFiles


Cython signature: void setSourceFiles(libcpp_vector[SourceFile] source_files)
Sets the source data file




