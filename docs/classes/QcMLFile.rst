QcMLFile
========

.. py:class:: QcMLFile


   Bases: :py:class:`object`


Cython implementation of _QcMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1QcMLFile.html
 -- Inherits from ['XMLHandler', 'XMLFile', 'ProgressLogger']




.. py:method:: QcMLFile.addRunAttachment


Cython signature: void addRunAttachment(String r, Attachment at)
Adds a attachment to run by the name r




.. py:method:: QcMLFile.addRunQualityParameter


Cython signature: void addRunQualityParameter(String r, QualityParameter qp)
Adds a QualityParameter to run by the name r




.. py:method:: QcMLFile.addSetAttachment


Cython signature: void addSetAttachment(String r, Attachment at)
Adds a attachment to set by the name r




.. py:method:: QcMLFile.addSetQualityParameter


Cython signature: void addSetQualityParameter(String r, QualityParameter qp)
Adds a QualityParameter to set by the name r




.. py:method:: QcMLFile.collectSetParameter


Cython signature: void collectSetParameter(String setname, String qp, libcpp_vector[String] & ret)
Collects the values of given QPs (as CVid) of the given set




.. py:method:: QcMLFile.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: QcMLFile.error


Cython signature: void error(ActionMode mode, const String & msg, unsigned int line, unsigned int column)




.. py:method:: QcMLFile.errorString


Cython signature: String errorString()




.. py:method:: QcMLFile.existsRun


Cython signature: bool existsRun(String filename)
Returns true if the given run id is present in this file, if checkname is true it also checks the names




.. py:method:: QcMLFile.existsRunQualityParameter


Cython signature: void existsRunQualityParameter(String filename, String qpname, libcpp_vector[String] & ids)
Returns the ids of the parameter name given if found in given run empty else




.. py:method:: QcMLFile.existsSet


Cython signature: bool existsSet(String filename)
Returns true if the given set id is present in this file, if checkname is true it also checks the names




.. py:method:: QcMLFile.existsSetQualityParameter


Cython signature: void existsSetQualityParameter(String filename, String qpname, libcpp_vector[String] & ids)
Returns the ids of the parameter name given if found in given set, empty else




.. py:method:: QcMLFile.exportAttachment


Cython signature: String exportAttachment(String filename, String qpname)
Returns a String of a tab separated rows if found empty string else from run/set by the name filename of the qualityparameter by the name qpname




.. py:method:: QcMLFile.exportIDstats


Cython signature: String exportIDstats(const String & filename)




.. py:method:: QcMLFile.exportQP


Cython signature: String exportQP(String filename, String qpname)
Returns a String value in quotation of a QualityParameter by the name qpname in run/set by the name filename




.. py:method:: QcMLFile.exportQPs


Cython signature: String exportQPs(String filename, StringList qpnames)
Returns a String of a tab separated QualityParameter by the name qpname in run/set by the name filename




.. py:method:: QcMLFile.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: QcMLFile.getRunIDs


Cython signature: void getRunIDs(libcpp_vector[String] & ids)
Gives the ids of the registered runs in the vector ids




.. py:method:: QcMLFile.getRunNames


Cython signature: void getRunNames(libcpp_vector[String] & ids)
Gives the names of the registered runs in the vector ids




.. py:method:: QcMLFile.getVersion


Cython signature: String getVersion()
Return the version of the schema




.. py:method:: QcMLFile.load


Cython signature: void load(const String & filename)
Load a QCFile




.. py:method:: QcMLFile.map2csv




.. py:method:: QcMLFile.merge


Cython signature: void merge(QcMLFile & addendum, String setname)
Merges the given QCFile into this one




.. py:method:: QcMLFile.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: QcMLFile.registerRun


Cython signature: void registerRun(String id_, String name)
Registers a run in the qcml file with the respective mappings




.. py:method:: QcMLFile.registerSet


Cython signature: void registerSet(String id_, String name, libcpp_set[String] & names)
Registers a set in the qcml file with the respective mappings




.. py:method:: QcMLFile.removeAllAttachments


Cython signature: void removeAllAttachments(String at)
Removes attachment with cv accession at from all runs/sets




.. py:method:: QcMLFile.removeAttachment


- Cython signature: void removeAttachment(String r, libcpp_vector[String] & ids, String at)
  Removes attachments referencing an id given in ids, from run/set r. All attachments if no attachment name is given with at


- Cython signature: void removeAttachment(String r, String at)
  Removes attachment with cv accession at from run/set r




.. py:method:: QcMLFile.removeQualityParameter


Cython signature: void removeQualityParameter(String r, libcpp_vector[String] & ids)
Removes QualityParameter going by one of the ID attributes given in ids




.. py:method:: QcMLFile.reset


Cython signature: void reset()




.. py:method:: QcMLFile.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: QcMLFile.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: QcMLFile.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: QcMLFile.store


Cython signature: void store(const String & filename)
Store the qcML file




.. py:method:: QcMLFile.warning


Cython signature: void warning(ActionMode mode, const String & msg, unsigned int line, unsigned int column)




