InclusionExclusionList
======================

.. py:class:: InclusionExclusionList


   Bases: :py:class:`object`


Cython implementation of _InclusionExclusionList


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1InclusionExclusionList.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: InclusionExclusionList.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: InclusionExclusionList.getName


Cython signature: String getName()
Returns the name




.. py:method:: InclusionExclusionList.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: InclusionExclusionList.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: InclusionExclusionList.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: InclusionExclusionList.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: InclusionExclusionList.writeTargets


- Cython signature: void writeTargets(libcpp_vector[FASTAEntry] & fasta_entries, const String & out_path, IntList & charges, const String rt_model_path)
  Writes inclusion or exclusion list of tryptic peptides of the given proteins (tab-delimited)


- Cython signature: void writeTargets(FeatureMap & map_, const String & out_path)
  Writes inclusion or exclusion list of given feature map


- Cython signature: void writeTargets(libcpp_vector[PeptideIdentification] & pep_ids, const String & out_path, IntList & charges)
  Writes inclusion or exclusion list of given peptide ids (tab-delimited)




