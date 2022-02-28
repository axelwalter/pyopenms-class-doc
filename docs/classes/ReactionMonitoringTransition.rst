ReactionMonitoringTransition
============================

.. py:class:: ReactionMonitoringTransition


   Bases: :py:class:`object`


Cython implementation of _ReactionMonitoringTransition


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ReactionMonitoringTransition.html
 -- Inherits from ['CVTermList']




.. py:method:: ReactionMonitoringTransition.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)
Adds a CV term




.. py:method:: ReactionMonitoringTransition.addIntermediateProduct


Cython signature: void addIntermediateProduct(TraMLProduct product)




.. py:method:: ReactionMonitoringTransition.addPrecursorCVTerm


Cython signature: void addPrecursorCVTerm(CVTerm & cv_term)
Adds precursor CV Term




.. py:method:: ReactionMonitoringTransition.addPredictionTerm


Cython signature: void addPredictionTerm(CVTerm & prediction)
Adds prediction term




.. py:method:: ReactionMonitoringTransition.addProductCVTerm


Cython signature: void addProductCVTerm(CVTerm & cv_term)




.. py:method:: ReactionMonitoringTransition.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: ReactionMonitoringTransition.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)
Merges the given map into the member map, no duplicate checking




.. py:method:: ReactionMonitoringTransition.empty


Cython signature: bool empty()




.. py:method:: ReactionMonitoringTransition.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()
Returns the accession string of the term




.. py:method:: ReactionMonitoringTransition.getCompoundRef


Cython signature: String getCompoundRef()




.. py:method:: ReactionMonitoringTransition.getDecoyTransitionType


Cython signature: DecoyTransitionType getDecoyTransitionType()
Returns the type of transition (target or decoy)




.. py:method:: ReactionMonitoringTransition.getIntermediateProducts


Cython signature: libcpp_vector[TraMLProduct] getIntermediateProducts()




.. py:method:: ReactionMonitoringTransition.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: ReactionMonitoringTransition.getLibraryIntensity


Cython signature: double getLibraryIntensity()
Returns the library intensity (ion count or normalized ion count from a spectral library)




.. py:method:: ReactionMonitoringTransition.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: ReactionMonitoringTransition.getName


Cython signature: String getName()




.. py:method:: ReactionMonitoringTransition.getNativeID


Cython signature: String getNativeID()




.. py:method:: ReactionMonitoringTransition.getPeptideRef


Cython signature: String getPeptideRef()




.. py:method:: ReactionMonitoringTransition.getPrecursorCVTermList


Cython signature: CVTermList getPrecursorCVTermList()
Obtains the list of CV Terms for the precursor




.. py:method:: ReactionMonitoringTransition.getPrecursorMZ


Cython signature: double getPrecursorMZ()
Returns the precursor mz (Q1 value)




.. py:method:: ReactionMonitoringTransition.getPrediction


Cython signature: Prediction getPrediction()
Obtains the Prediction object




.. py:method:: ReactionMonitoringTransition.getProduct


Cython signature: TraMLProduct getProduct()




.. py:method:: ReactionMonitoringTransition.getProductChargeState


Cython signature: int getProductChargeState()
Returns the charge state of the product




.. py:method:: ReactionMonitoringTransition.getProductMZ


Cython signature: double getProductMZ()




.. py:method:: ReactionMonitoringTransition.getRetentionTime


Cython signature: RetentionTime getRetentionTime()




.. py:method:: ReactionMonitoringTransition.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:method:: ReactionMonitoringTransition.hasPrecursorCVTerms


Cython signature: bool hasPrecursorCVTerms()
Returns true if precursor CV Terms exist (means it is safe to call getPrecursorCVTermList)




.. py:method:: ReactionMonitoringTransition.hasPrediction


Cython signature: bool hasPrediction()
Returns true if a Prediction object exists (means it is safe to call getPrediction)




.. py:method:: ReactionMonitoringTransition.isDetectingTransition


Cython signature: bool isDetectingTransition()




.. py:method:: ReactionMonitoringTransition.isIdentifyingTransition


Cython signature: bool isIdentifyingTransition()




.. py:method:: ReactionMonitoringTransition.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: ReactionMonitoringTransition.isProductChargeStateSet


Cython signature: bool isProductChargeStateSet()
Returns true if charge state of product is already set




.. py:method:: ReactionMonitoringTransition.isQuantifyingTransition


Cython signature: bool isQuantifyingTransition()




.. py:method:: ReactionMonitoringTransition.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: ReactionMonitoringTransition.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: ReactionMonitoringTransition.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: ReactionMonitoringTransition.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)
Replaces the specified CV term




.. py:method:: ReactionMonitoringTransition.replaceCVTerms


Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)




.. py:method:: ReactionMonitoringTransition.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)
Sets the CV terms




.. py:method:: ReactionMonitoringTransition.setCompoundRef


Cython signature: void setCompoundRef(const String & compound_ref)




.. py:method:: ReactionMonitoringTransition.setDecoyTransitionType


Cython signature: void setDecoyTransitionType(DecoyTransitionType & d)
Sets the type of transition (target or decoy)




.. py:method:: ReactionMonitoringTransition.setDetectingTransition


Cython signature: void setDetectingTransition(bool val)




.. py:method:: ReactionMonitoringTransition.setIdentifyingTransition


Cython signature: void setIdentifyingTransition(bool val)




.. py:method:: ReactionMonitoringTransition.setIntermediateProducts


Cython signature: void setIntermediateProducts(libcpp_vector[TraMLProduct] & products)




.. py:method:: ReactionMonitoringTransition.setLibraryIntensity


Cython signature: void setLibraryIntensity(double intensity)
Sets the library intensity (ion count or normalized ion count from a spectral library)




.. py:method:: ReactionMonitoringTransition.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: ReactionMonitoringTransition.setName


Cython signature: void setName(String name)




.. py:method:: ReactionMonitoringTransition.setNativeID


Cython signature: void setNativeID(String name)




.. py:method:: ReactionMonitoringTransition.setPeptideRef


Cython signature: void setPeptideRef(String peptide_ref)




.. py:method:: ReactionMonitoringTransition.setPrecursorCVTermList


Cython signature: void setPrecursorCVTermList(CVTermList & list_)
Sets a list of precursor CV Terms




.. py:method:: ReactionMonitoringTransition.setPrecursorMZ


Cython signature: void setPrecursorMZ(double)
Sets the precursor mz (Q1 value)




.. py:method:: ReactionMonitoringTransition.setPrediction


Cython signature: void setPrediction(Prediction & prediction)
Sets prediction




.. py:method:: ReactionMonitoringTransition.setProduct


Cython signature: void setProduct(TraMLProduct product)




.. py:method:: ReactionMonitoringTransition.setProductMZ


Cython signature: void setProductMZ(double)




.. py:method:: ReactionMonitoringTransition.setQuantifyingTransition


Cython signature: void setQuantifyingTransition(bool val)




.. py:method:: ReactionMonitoringTransition.setRetentionTime


Cython signature: void setRetentionTime(RetentionTime rt)




