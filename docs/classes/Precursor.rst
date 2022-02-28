Precursor
=========

.. py:class:: Precursor


   Bases: :py:class:`object`


Cython implementation of _Precursor


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Precursor.html
 -- Inherits from ['Peak1D', 'CVTermList']




.. py:method:: Precursor.addCVTerm


Cython signature: void addCVTerm(CVTerm & term)
Adds a CV term




.. py:method:: Precursor.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: Precursor.consumeCVTerms


Cython signature: void consumeCVTerms(Map[String,libcpp_vector[CVTerm]] cv_term_map)
Merges the given map into the member map, no duplicate checking




.. py:method:: Precursor.empty


Cython signature: bool empty()




.. py:method:: Precursor.getActivationEnergy


Cython signature: double getActivationEnergy()
Returns the activation energy (in electronvolt)




.. py:method:: Precursor.getActivationMethods


Cython signature: libcpp_set[ActivationMethod] getActivationMethods()
Returns the activation methods




.. py:method:: Precursor.getCVTerms


Cython signature: Map[String,libcpp_vector[CVTerm]] getCVTerms()
Returns the accession string of the term




.. py:method:: Precursor.getCharge


Cython signature: int getCharge()
Returns the charge




.. py:method:: Precursor.getDriftTime


Cython signature: double getDriftTime()
Returns the ion mobility drift time in milliseconds (-1 means it is not set)




.. py:method:: Precursor.getDriftTimeWindowLowerOffset


Cython signature: double getDriftTimeWindowLowerOffset()
Returns the lower offset from the target ion mobility in milliseconds




.. py:method:: Precursor.getDriftTimeWindowUpperOffset


Cython signature: double getDriftTimeWindowUpperOffset()
Returns the upper offset from the target ion mobility in milliseconds




.. py:method:: Precursor.getIntensity


Cython signature: float getIntensity()




.. py:method:: Precursor.getIsolationWindowLowerOffset


Cython signature: double getIsolationWindowLowerOffset()
Returns the lower offset from the target m/z




.. py:method:: Precursor.getIsolationWindowUpperOffset


Cython signature: double getIsolationWindowUpperOffset()
Returns the upper offset from the target m/z




.. py:method:: Precursor.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: Precursor.getMZ


Cython signature: double getMZ()




.. py:method:: Precursor.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: Precursor.getPos


Cython signature: double getPos()




.. py:method:: Precursor.getPossibleChargeStates


Cython signature: libcpp_vector[int] getPossibleChargeStates()
Returns the possible charge states




.. py:method:: Precursor.getUnchargedMass


Cython signature: double getUnchargedMass()
Returns the uncharged mass of the precursor, if charge is unknown, i.e. 0 best guess is its doubly charged




.. py:method:: Precursor.hasCVTerm


Cython signature: bool hasCVTerm(String accession)




.. py:method:: Precursor.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: Precursor.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: Precursor.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: Precursor.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: Precursor.replaceCVTerm


Cython signature: void replaceCVTerm(CVTerm & term)
Replaces the specified CV term




.. py:method:: Precursor.replaceCVTerms


Cython signature: void replaceCVTerms(libcpp_vector[CVTerm] cv_terms, String accession)




.. py:method:: Precursor.setActivationEnergy


Cython signature: void setActivationEnergy(double activation_energy)
Sets the activation energy (in electronvolt)




.. py:method:: Precursor.setActivationMethods


Cython signature: void setActivationMethods(libcpp_set[ActivationMethod] activation_methods)
Sets the activation methods




.. py:method:: Precursor.setCVTerms


Cython signature: void setCVTerms(libcpp_vector[CVTerm] & terms)
Sets the CV terms




.. py:method:: Precursor.setCharge


Cython signature: void setCharge(int charge)
Sets the charge




.. py:method:: Precursor.setDriftTime


Cython signature: void setDriftTime(double drift_time)
Sets the ion mobility drift time in milliseconds




.. py:method:: Precursor.setDriftTimeWindowLowerOffset


Cython signature: void setDriftTimeWindowLowerOffset(double drift_time)
Sets the lower offset from the target ion mobility




.. py:method:: Precursor.setDriftTimeWindowUpperOffset


Cython signature: void setDriftTimeWindowUpperOffset(double drift_time)
Sets the upper offset from the target ion mobility




.. py:method:: Precursor.setIntensity


Cython signature: void setIntensity(float)




.. py:method:: Precursor.setIsolationWindowLowerOffset


Cython signature: void setIsolationWindowLowerOffset(double bound)
Sets the lower offset from the target m/z




.. py:method:: Precursor.setIsolationWindowUpperOffset


Cython signature: void setIsolationWindowUpperOffset(double bound)
Sets the upper offset from the target m/z




.. py:method:: Precursor.setMZ


Cython signature: void setMZ(double)




.. py:method:: Precursor.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: Precursor.setPos


Cython signature: void setPos(double pos)




.. py:method:: Precursor.setPossibleChargeStates


Cython signature: void setPossibleChargeStates(libcpp_vector[int] possible_charge_states)
Sets the possible charge states




