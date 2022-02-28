IncludeExcludeTarget
====================

.. py:class:: IncludeExcludeTarget


   Bases: :py:class:`object`


Cython implementation of _IncludeExcludeTarget


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IncludeExcludeTarget.html




.. py:method:: IncludeExcludeTarget.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)




.. py:method:: IncludeExcludeTarget.addConfiguration


Cython signature: void addConfiguration(Configuration & configuration)




.. py:method:: IncludeExcludeTarget.addInterpretation


Cython signature: void addInterpretation(CVTermList & interpretation)




.. py:method:: IncludeExcludeTarget.addPrecursorCVTerm


Cython signature: void addPrecursorCVTerm(CVTerm & cv_term)




.. py:method:: IncludeExcludeTarget.addPredictionTerm


Cython signature: void addPredictionTerm(CVTerm & prediction)




.. py:method:: IncludeExcludeTarget.addProductCVTerm


Cython signature: void addProductCVTerm(CVTerm & cv_term)




.. py:method:: IncludeExcludeTarget.empty


Cython signature: bool empty()




.. py:method:: IncludeExcludeTarget.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()




.. py:method:: IncludeExcludeTarget.getCompoundRef


Cython signature: String getCompoundRef()




.. py:method:: IncludeExcludeTarget.getConfigurations


Cython signature: libcpp_vector[Configuration] getConfigurations()




.. py:method:: IncludeExcludeTarget.getInterpretations


Cython signature: libcpp_vector[CVTermList] getInterpretations()




.. py:method:: IncludeExcludeTarget.getName


Cython signature: String getName()




.. py:method:: IncludeExcludeTarget.getPeptideRef


Cython signature: String getPeptideRef()




.. py:method:: IncludeExcludeTarget.getPrecursorCVTermList


Cython signature: CVTermList getPrecursorCVTermList()




.. py:method:: IncludeExcludeTarget.getPrecursorMZ


Cython signature: double getPrecursorMZ()




.. py:method:: IncludeExcludeTarget.getPrediction


Cython signature: CVTermList getPrediction()




.. py:method:: IncludeExcludeTarget.getProductCVTermList


Cython signature: CVTermList getProductCVTermList()




.. py:method:: IncludeExcludeTarget.getProductMZ


Cython signature: double getProductMZ()




.. py:method:: IncludeExcludeTarget.getRetentionTime


Cython signature: RetentionTime getRetentionTime()




.. py:method:: IncludeExcludeTarget.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:method:: IncludeExcludeTarget.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)




.. py:method:: IncludeExcludeTarget.replaceCVTerms


- Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)
- Cython signature: void replaceCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)




.. py:method:: IncludeExcludeTarget.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)




.. py:method:: IncludeExcludeTarget.setCompoundRef


Cython signature: void setCompoundRef(const String & compound_ref)




.. py:method:: IncludeExcludeTarget.setConfigurations


Cython signature: void setConfigurations(libcpp_vector[Configuration] & configuration)




.. py:method:: IncludeExcludeTarget.setInterpretations


Cython signature: void setInterpretations(libcpp_vector[CVTermList] & interpretations)




.. py:method:: IncludeExcludeTarget.setName


Cython signature: void setName(const String & name)




.. py:method:: IncludeExcludeTarget.setPeptideRef


Cython signature: void setPeptideRef(const String & peptide_ref)




.. py:method:: IncludeExcludeTarget.setPrecursorCVTermList


Cython signature: void setPrecursorCVTermList(CVTermList & list_)




.. py:method:: IncludeExcludeTarget.setPrecursorMZ


Cython signature: void setPrecursorMZ(double mz)




.. py:method:: IncludeExcludeTarget.setPrediction


Cython signature: void setPrediction(CVTermList & prediction)




.. py:method:: IncludeExcludeTarget.setProductCVTermList


Cython signature: void setProductCVTermList(CVTermList & list_)




.. py:method:: IncludeExcludeTarget.setProductMZ


Cython signature: void setProductMZ(double mz)




.. py:method:: IncludeExcludeTarget.setRetentionTime


Cython signature: void setRetentionTime(RetentionTime rt)




