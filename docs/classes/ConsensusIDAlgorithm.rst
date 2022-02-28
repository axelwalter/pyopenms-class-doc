ConsensusIDAlgorithm
====================

.. py:class:: ConsensusIDAlgorithm


   Bases: :py:class:`object`


Cython implementation of _ConsensusIDAlgorithm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusIDAlgorithm.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: ConsensusIDAlgorithm.apply


Cython signature: void apply(libcpp_vector[PeptideIdentification] & ids, size_t number_of_runs)
Calculates the consensus ID for a set of peptide identifications of one spectrum or (consensus) feature




.. py:method:: ConsensusIDAlgorithm.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: ConsensusIDAlgorithm.getName


Cython signature: String getName()
Returns the name




.. py:method:: ConsensusIDAlgorithm.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: ConsensusIDAlgorithm.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: ConsensusIDAlgorithm.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: ConsensusIDAlgorithm.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




