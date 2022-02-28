ProteinResolver
===============

.. py:class:: ProteinResolver


   Bases: :py:class:`object`


Cython implementation of _ProteinResolver


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProteinResolver.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: ProteinResolver.clearResult


Cython signature: void clearResult()




.. py:method:: ProteinResolver.countTargetDecoy


- Cython signature: void countTargetDecoy(libcpp_vector[MSDGroup] & msd_groups, ConsensusMap & consensus)
- Cython signature: void countTargetDecoy(libcpp_vector[MSDGroup] & msd_groups, libcpp_vector[PeptideIdentification] & peptide_nodes)




.. py:method:: ProteinResolver.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: ProteinResolver.getName


Cython signature: String getName()
Returns the name




.. py:method:: ProteinResolver.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: ProteinResolver.getPeptideHit


- Cython signature: PeptideHit getPeptideHit(ConsensusMap & consensus, PeptideEntry * peptide)
- Cython signature: PeptideHit getPeptideHit(libcpp_vector[PeptideIdentification] & peptide_nodes, PeptideEntry * peptide)




.. py:method:: ProteinResolver.getPeptideIdentification


- Cython signature: PeptideIdentification getPeptideIdentification(ConsensusMap & consensus, PeptideEntry * peptide)
- Cython signature: PeptideIdentification getPeptideIdentification(libcpp_vector[PeptideIdentification] & peptide_nodes, PeptideEntry * peptide)




.. py:method:: ProteinResolver.getResults


Cython signature: libcpp_vector[ResolverResult] getResults()




.. py:method:: ProteinResolver.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: ProteinResolver.resolveConsensus


Cython signature: void resolveConsensus(ConsensusMap & consensus)




.. py:method:: ProteinResolver.resolveID


Cython signature: void resolveID(libcpp_vector[PeptideIdentification] & peptide_identifications)




.. py:method:: ProteinResolver.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: ProteinResolver.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: ProteinResolver.setProteinData


Cython signature: void setProteinData(libcpp_vector[FASTAEntry] & protein_data)




