ContactPerson
=============

.. py:class:: ContactPerson


   Bases: :py:class:`object`


Cython implementation of _ContactPerson


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ContactPerson.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: ContactPerson.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: ContactPerson.getAddress


Cython signature: String getAddress()
Returns the address




.. py:method:: ContactPerson.getContactInfo


Cython signature: String getContactInfo()
Returns miscellaneous info about the contact person




.. py:method:: ContactPerson.getEmail


Cython signature: String getEmail()
Returns the email address




.. py:method:: ContactPerson.getFirstName


Cython signature: String getFirstName()
Returns the first name of the person




.. py:method:: ContactPerson.getInstitution


Cython signature: String getInstitution()
Returns the affiliation




.. py:method:: ContactPerson.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: ContactPerson.getLastName


Cython signature: String getLastName()
Returns the last name of the person




.. py:method:: ContactPerson.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: ContactPerson.getURL


Cython signature: String getURL()
Returns the URL associated with the contact person (e.g., the institute webpage




.. py:method:: ContactPerson.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: ContactPerson.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: ContactPerson.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: ContactPerson.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: ContactPerson.setAddress


Cython signature: void setAddress(String email)
Sets the address




.. py:method:: ContactPerson.setContactInfo


Cython signature: void setContactInfo(String contact_info)
Sets miscellaneous info about the contact person




.. py:method:: ContactPerson.setEmail


Cython signature: void setEmail(String email)
Sets the email address




.. py:method:: ContactPerson.setFirstName


Cython signature: void setFirstName(String name)
Sets the first name of the person




.. py:method:: ContactPerson.setInstitution


Cython signature: void setInstitution(String institution)
Sets the affiliation




.. py:method:: ContactPerson.setLastName


Cython signature: void setLastName(String name)
Sets the last name of the person




.. py:method:: ContactPerson.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: ContactPerson.setName


Cython signature: void setName(String name)
Sets the full name of the person (gets split into first and last name internally)




.. py:method:: ContactPerson.setURL


Cython signature: void setURL(String email)
Sets the URL associated with the contact person (e.g., the institute webpage




