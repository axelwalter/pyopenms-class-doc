FalseDiscoveryRate
==================

.. py:class:: FalseDiscoveryRate


   Bases: :py:class:`object`


Cython implementation of _FalseDiscoveryRate


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FalseDiscoveryRate.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: FalseDiscoveryRate.apply


- Cython signature: void apply(libcpp_vector[PeptideIdentification] & forward_ids, libcpp_vector[PeptideIdentification] & reverse_ids)
- Cython signature: void apply(libcpp_vector[PeptideIdentification] & id)
- Cython signature: void apply(libcpp_vector[ProteinIdentification] & forward_ids, libcpp_vector[ProteinIdentification] & reverse_ids)
- Cython signature: void apply(libcpp_vector[ProteinIdentification] & id)




.. py:method:: FalseDiscoveryRate.applyBasic


- Cython signature: void applyBasic(libcpp_vector[PeptideIdentification] & ids)
- Cython signature: void applyBasic(ConsensusMap & cmap, bool use_unassigned_peptides)
- Cython signature: void applyBasic(ProteinIdentification & id, bool groups_too)




.. py:method:: FalseDiscoveryRate.applyEstimated


Cython signature: void applyEstimated(libcpp_vector[ProteinIdentification] & ids)




.. py:method:: FalseDiscoveryRate.applyEvaluateProteinIDs


- Cython signature: double applyEvaluateProteinIDs(libcpp_vector[ProteinIdentification] & ids, double pepCutoff, unsigned int fpCutoff, double diffWeight)
- Cython signature: double applyEvaluateProteinIDs(ProteinIdentification & ids, double pepCutoff, unsigned int fpCutoff, double diffWeight)




.. py:method:: FalseDiscoveryRate.applyPickedProteinFDR


Cython signature: void applyPickedProteinFDR(ProteinIdentification & id, String & decoy_string, bool decoy_prefix, bool groups_too)




.. py:method:: FalseDiscoveryRate.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: FalseDiscoveryRate.getName


Cython signature: String getName()
Returns the name




.. py:method:: FalseDiscoveryRate.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: FalseDiscoveryRate.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: FalseDiscoveryRate.rocN


- Cython signature: double rocN(libcpp_vector[PeptideIdentification] & ids, size_t fp_cutoff)
- Cython signature: double rocN(ConsensusMap & ids, size_t fp_cutoff)




.. py:method:: FalseDiscoveryRate.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: FalseDiscoveryRate.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




