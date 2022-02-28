SimpleSearchEngineAlgorithm
===========================

.. py:class:: SimpleSearchEngineAlgorithm


   Bases: :py:class:`object`


Cython implementation of _SimpleSearchEngineAlgorithm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SimpleSearchEngineAlgorithm.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: SimpleSearchEngineAlgorithm.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: SimpleSearchEngineAlgorithm.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: SimpleSearchEngineAlgorithm.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: SimpleSearchEngineAlgorithm.getName


Cython signature: String getName()
Returns the name




.. py:method:: SimpleSearchEngineAlgorithm.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: SimpleSearchEngineAlgorithm.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: SimpleSearchEngineAlgorithm.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: SimpleSearchEngineAlgorithm.search


Cython signature: void search(const String & in_mzML, const String & in_db, libcpp_vector[ProteinIdentification] & prot_ids, libcpp_vector[PeptideIdentification] & pep_ids)




.. py:method:: SimpleSearchEngineAlgorithm.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: SimpleSearchEngineAlgorithm.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: SimpleSearchEngineAlgorithm.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: SimpleSearchEngineAlgorithm.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: SimpleSearchEngineAlgorithm.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




