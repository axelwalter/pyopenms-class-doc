TraMLProduct
============

.. py:class:: TraMLProduct


   Bases: :py:class:`object`


Cython implementation of _TraMLProduct


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::TargetedExperimentHelper::RetentionTime::RTUnit_1_1TraMLProduct.html
 -- Inherits from ['CVTermList']




.. py:method:: TraMLProduct.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)
Adds a CV term




.. py:method:: TraMLProduct.addConfiguration


Cython signature: void addConfiguration(Configuration configuration)




.. py:method:: TraMLProduct.addInterpretation


Cython signature: void addInterpretation(TargetedExperiment_Interpretation interpretation)




.. py:method:: TraMLProduct.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: TraMLProduct.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)
Merges the given map into the member map, no duplicate checking




.. py:method:: TraMLProduct.empty


Cython signature: bool empty()




.. py:method:: TraMLProduct.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()
Returns the accession string of the term




.. py:method:: TraMLProduct.getChargeState


Cython signature: int getChargeState()




.. py:method:: TraMLProduct.getConfigurationList


Cython signature: libcpp_vector[Configuration] getConfigurationList()




.. py:method:: TraMLProduct.getInterpretationList


Cython signature: libcpp_vector[TargetedExperiment_Interpretation] getInterpretationList()




.. py:method:: TraMLProduct.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: TraMLProduct.getMZ


Cython signature: double getMZ()




.. py:method:: TraMLProduct.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: TraMLProduct.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:method:: TraMLProduct.hasCharge


Cython signature: bool hasCharge()




.. py:method:: TraMLProduct.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: TraMLProduct.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: TraMLProduct.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: TraMLProduct.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: TraMLProduct.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)
Replaces the specified CV term




.. py:method:: TraMLProduct.replaceCVTerms


Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)




.. py:method:: TraMLProduct.resetInterpretations


Cython signature: void resetInterpretations()




.. py:method:: TraMLProduct.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)
Sets the CV terms




.. py:method:: TraMLProduct.setChargeState


Cython signature: void setChargeState(int charge)




.. py:method:: TraMLProduct.setMZ


Cython signature: void setMZ(double mz)




.. py:method:: TraMLProduct.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




