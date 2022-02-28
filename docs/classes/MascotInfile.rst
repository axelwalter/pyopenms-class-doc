MascotInfile
============

.. py:class:: MascotInfile


   Bases: :py:class:`object`


Cython implementation of _MascotInfile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MascotInfile.html
 -- Inherits from ['ProgressLogger']




.. py:method:: MascotInfile.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MascotInfile.getBoundary


Cython signature: String getBoundary()
Returns the boundary used for the MIME format




.. py:method:: MascotInfile.getCharges


Cython signature: String getCharges()
Returns the charges




.. py:method:: MascotInfile.getCleavage


Cython signature: String getCleavage()
Returns the enzyme used for cleavage




.. py:method:: MascotInfile.getDB


Cython signature: String getDB()
Returns the DB to use




.. py:method:: MascotInfile.getFormVersion


Cython signature: String getFormVersion()
Returns the Mascot form version




.. py:method:: MascotInfile.getHits


Cython signature: String getHits()
Returns the number of hits to report back




.. py:method:: MascotInfile.getInstrument


Cython signature: String getInstrument()
Returns the instrument type




.. py:method:: MascotInfile.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MascotInfile.getMassType


Cython signature: String getMassType()
Returns the used mass type ("Monoisotopic" or "Average")




.. py:method:: MascotInfile.getMissedCleavages


Cython signature: unsigned int getMissedCleavages()
Returns the number of allowed missed cleavages




.. py:method:: MascotInfile.getModifications


Cython signature: libcpp_vector[String] getModifications()
Returns a vector containing the fixed modifications (default none)




.. py:method:: MascotInfile.getPeakMassTolerance


Cython signature: float getPeakMassTolerance()
Returns the peak mass tolerance in Da




.. py:method:: MascotInfile.getPrecursorMassTolerance


Cython signature: float getPrecursorMassTolerance()
Returns the precursor mass tolerance




.. py:method:: MascotInfile.getSearchType


Cython signature: String getSearchType()
Returns the search type




.. py:method:: MascotInfile.getTaxonomy


Cython signature: String getTaxonomy()
Returns the taxonomy




.. py:method:: MascotInfile.getVariableModifications


Cython signature: libcpp_vector[String] getVariableModifications()
Returns a vector containing the variable modifications (default none)




.. py:method:: MascotInfile.load


Cython signature: void load(const String & filename, MSExperiment & exp)


Loads a Mascot Generic File into a PeakMap
-----
:param filename: File name which the map should be read from
:param exp: The map which is filled with the data from the given file
:raises:
  Exception: FileNotFound is thrown if the given file could not be found




.. py:method:: MascotInfile.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MascotInfile.setBoundary


Cython signature: void setBoundary(const String & boundary)
Sets the boundary used for the MIME format.By default a 22 character random string is used




.. py:method:: MascotInfile.setCharges


Cython signature: void setCharges(libcpp_vector[int] & charges)
Sets the charges (default 1+, 2+ and 3+)




.. py:method:: MascotInfile.setCleavage


Cython signature: void setCleavage(const String & cleavage)
Sets the enzyme used for cleavage (default Trypsin). See mascot path /config/enzymes for possible settings




.. py:method:: MascotInfile.setDB


Cython signature: void setDB(const String & db)
Sets the DB (default MSDB). See mascot path /config/mascot.dat in "Databases" section for possible settings




.. py:method:: MascotInfile.setFormVersion


Cython signature: void setFormVersion(const String & form_version)
Sets the Mascot form version (default 1.01)




.. py:method:: MascotInfile.setHits


Cython signature: void setHits(const String & hits)
Sets the number of hits to report back (default 20)




.. py:method:: MascotInfile.setInstrument


Cython signature: void setInstrument(const String & instrument)
Sets the instrument type (Default Default). Possible instruments are ESI-QUAD-TOF, MALDI-TOF-PSD, ESI-TRAP, ESI-QUAD, ESI-FTICR, MALDI-TOF-TOF, ESI-4SECTOR, FTMS-ECD, MALDI-QUAD-TOF, MALDI-QIT-TOF




.. py:method:: MascotInfile.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MascotInfile.setMassType


Cython signature: void setMassType(const String & mass_type)
Sets the used mass type "Monoisotopic" or "Average" (default Monoisotopic)




.. py:method:: MascotInfile.setMissedCleavages


Cython signature: void setMissedCleavages(unsigned int missed_cleavages)
Sets the number of allowed missed cleavages (default 1)




.. py:method:: MascotInfile.setModifications


Cython signature: void setModifications(libcpp_vector[String] & mods)
Sets the fixed modifications (default none). See mascot path /config/mod_file for possible settings




.. py:method:: MascotInfile.setPeakMassTolerance


Cython signature: void setPeakMassTolerance(float ion_mass_tolerance)
Sets the peak mass tolerance in Da (default 1.0)




.. py:method:: MascotInfile.setPrecursorMassTolerance


Cython signature: void setPrecursorMassTolerance(float precursor_mass_tolerance)
Sets the precursor mass tolerance in Da (default 2.0)




.. py:method:: MascotInfile.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MascotInfile.setSearchType


Cython signature: void setSearchType(const String & search_type)
Sets the search type (default MIS). So far only MIS is supported!Valid types are "MIS" (MS/MS Ion Search), "PMF" (Peptide Mass Fingerprint) , "SQ" (Sequence Query)




.. py:method:: MascotInfile.setTaxonomy


Cython signature: void setTaxonomy(const String & taxonomy)
Sets the taxonomy (default All entries). See mascot path /config/taxonomy for possible settings




.. py:method:: MascotInfile.setVariableModifications


Cython signature: void setVariableModifications(libcpp_vector[String] & mods)
Sets the fixed modifications (default none). See mascot path /config/mod_file for possible settings




.. py:method:: MascotInfile.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: MascotInfile.store


- Cython signature: void store(const String & filename, MSSpectrum & spec, double mz, double retention_time, String search_title)
  Stores the peak list in a MascotInfile that can be used as input for MASCOT shell execution


- Cython signature: void store(const String & filename, MSExperiment & experiment, String search_title)
  Stores the experiment data in a MascotInfile that can be used as input for MASCOT shell execution




