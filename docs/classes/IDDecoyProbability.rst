IDDecoyProbability
==================

.. py:class:: IDDecoyProbability


   Bases: :py:class:`object`


Cython implementation of _IDDecoyProbability


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IDDecoyProbability.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: IDDecoyProbability.apply


         - Cython signature: void apply(libcpp_vector[PeptideIdentification] & prob_ids, libcpp_vector[PeptideIdentification] & fwd_ids, libcpp_vector[PeptideIdentification] & rev_ids)


Converts the forward and reverse identification into probabilities
-----
:param prob_ids: Output of the algorithm which includes identifications with probability based scores
:param fwd_ids: Input parameter which represents the identifications of the forward search
:param rev_ids: Input parameter which represents the identifications of the reversed search
         - Cython signature: void apply(libcpp_vector[PeptideIdentification] & ids)




.. py:method:: IDDecoyProbability.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: IDDecoyProbability.getName


Cython signature: String getName()
Returns the name




.. py:method:: IDDecoyProbability.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: IDDecoyProbability.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: IDDecoyProbability.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: IDDecoyProbability.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




