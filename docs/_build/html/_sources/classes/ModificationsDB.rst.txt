ModificationsDB
===============

.. py:class:: ModificationsDB


   Bases: :py:class:`object`


Cython implementation of _ModificationsDB


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ModificationsDB.html




.. py:method:: ModificationsDB.addModification


Cython signature: const ResidueModification * addModification(const ResidueModification & new_mod)
Add a new modification to ModificationsDB. If the modification already exists (based on its fullID) it is not added. Returns the modification in the ModificationDB (which can differ from input if mod was already present).




.. py:method:: ModificationsDB.findModificationIndex


Cython signature: size_t findModificationIndex(const String & mod_name)
Returns the index of the modification in the mods_ vector; a unique name must be given




.. py:method:: ModificationsDB.getAllSearchModifications


Cython signature: void getAllSearchModifications(libcpp_vector[String] & modifications)
Collects all modifications that can be used for identification searches




.. py:method:: ModificationsDB.getBestModificationByDiffMonoMass


Cython signature: const ResidueModification * getBestModificationByDiffMonoMass(double mass, double max_error, const String & residue, TermSpecificity term_spec)


Returns the best matching modification for the given delta mass and residue
-----
Query the modifications DB to get the best matching modification with
the given delta mass at the given residue (NULL pointer means no result,
maybe the maximal error tolerance needs to be increased). Possible
input for CAM modification would be a delta mass of 57 and a residue
of "C".
-----
Note: If there are multiple possible matches with equal masses, it
will choose the _first_ match which defaults to the first matching
UniMod entry.
-----
:param residue: The residue at which the modifications occurs
:param mass: The monoisotopic mass of the residue including the mass of the modification
:param max_error: The maximal mass error in the modification search
:returns: A pointer to the best matching modification (or NULL if none was found)




.. py:method:: ModificationsDB.getModification


- Cython signature: const ResidueModification * getModification(size_t index)
  Returns the modification with the given index


- Cython signature: const ResidueModification * getModification(const String & mod_name)
  Returns the modification with the given name


- Cython signature: const ResidueModification * getModification(const String & mod_name, const String & residue, TermSpecificity term_spec)
  Returns the modification with the given arguments




.. py:method:: ModificationsDB.getNumberOfModifications


Cython signature: size_t getNumberOfModifications()
Returns the number of modifications read from the unimod.xml file




.. py:method:: ModificationsDB.has


Cython signature: bool has(String modification)
Returns true if the modification exists




.. py:method:: ModificationsDB.isInstantiated


Cython signature: bool isInstantiated()
Check whether ModificationsDB was instantiated before




.. py:method:: ModificationsDB.searchModifications


Cython signature: void searchModifications(libcpp_set[const ResidueModification *] & mods, const String & mod_name, const String & residue, TermSpecificity term_spec)


Collects all modifications which have the given name as synonym
-----
If `residue` is set, only modifications with matching residue of origin are considered
If `term_spec` is set, only modifications with matching term specificity are considered
The resulting set of modifications will be empty if no modification exists that fulfills the criteria




.. py:method:: ModificationsDB.searchModificationsByDiffMonoMass


Cython signature: void searchModificationsByDiffMonoMass(libcpp_vector[String] & mods, double mass, double max_error, const String & residue, TermSpecificity term_spec)
Collects all modifications with delta mass inside a tolerance window




