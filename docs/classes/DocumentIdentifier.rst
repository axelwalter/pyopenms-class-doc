DocumentIdentifier
==================

.. py:class:: DocumentIdentifier


   Bases: :py:class:`object`


Cython implementation of _DocumentIdentifier


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1DocumentIdentifier.html




.. py:method:: DocumentIdentifier.getIdentifier


Cython signature: String getIdentifier()
Retrieve document identifier (e.g. an LSID)




.. py:method:: DocumentIdentifier.getLoadedFilePath


Cython signature: String getLoadedFilePath()
Returns the file_name which is the absolute path to the file loaded




.. py:method:: DocumentIdentifier.getLoadedFileType


Cython signature: int getLoadedFileType()
Returns the file_type (e.g. featureXML, consensusXML, mzData, mzXML, mzML, ...) of the file loaded




.. py:method:: DocumentIdentifier.setIdentifier


Cython signature: void setIdentifier(String id)
Sets document identifier (e.g. an LSID)




.. py:method:: DocumentIdentifier.setLoadedFilePath


Cython signature: void setLoadedFilePath(String file_name)
Sets the file_name according to absolute path of the file loaded, preferably done whilst loading




.. py:method:: DocumentIdentifier.setLoadedFileType


Cython signature: void setLoadedFileType(String file_name)
Sets the file_type according to the type of the file loaded from, preferably done whilst loading




