InspectOutfile
==============

.. py:class:: InspectOutfile


   Bases: :py:class:`object`


Cython implementation of _InspectOutfile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1InspectOutfile.html




.. py:method:: InspectOutfile.compressTrieDB


Cython signature: void compressTrieDB(const String & database_filename, const String & index_filename, libcpp_vector[size_t] & wanted_records, const String & snd_database_filename, const String & snd_index_filename, bool append)
Generates a trie database from another one, using the wanted records only




.. py:method:: InspectOutfile.generateTrieDB


Cython signature: void generateTrieDB(const String & source_database_filename, const String & database_filename, const String & index_filename, bool append, const String species)
Generates a trie database from a given one (the type of database is determined by getLabels)




.. py:method:: InspectOutfile.getACAndACType


Cython signature: void getACAndACType(String line, String & accession, String & accession_type)
Retrieve the accession type and accession number from a protein description line




.. py:method:: InspectOutfile.getExperiment


Cython signature: void getExperiment(MSExperiment & exp, String & type_, const String & in_filename)
Get the experiment from a file




.. py:method:: InspectOutfile.getLabels


Cython signature: void getLabels(const String & source_database_filename, String & ac_label, String & sequence_start_label, String & sequence_end_label, String & comment_label, String & species_label)
Retrieve the labels of a given database (at the moment FASTA and Swissprot)




.. py:method:: InspectOutfile.getSearchEngineAndVersion


Cython signature: bool getSearchEngineAndVersion(const String & cmd_output, ProteinIdentification & protein_identification)
Get the search engine and its version from the output of the InsPecT executable without parameters. Returns true on success, false otherwise




.. py:method:: InspectOutfile.getSequences


Cython signature: libcpp_vector[size_t] getSequences(const String & database_filename, libcpp_map[size_t,size_t] & wanted_records, libcpp_vector[String] & sequences)
Retrieve sequences from a trie database




.. py:method:: InspectOutfile.getWantedRecords


Cython signature: libcpp_vector[size_t] getWantedRecords(const String & result_filename, double p_value_threshold)


Loads only results which exceeds a given p-value threshold
-----
:param result_filename: The filename of the results file
:param p_value_threshold: Only identifications exceeding this threshold are read
:raises:
  Exception: FileNotFound is thrown if the given file could not be found
:raises:
  Exception: FileEmpty is thrown if the given file is empty




.. py:method:: InspectOutfile.load


Cython signature: libcpp_vector[size_t] load(const String & result_filename, libcpp_vector[PeptideIdentification] & peptide_identifications, ProteinIdentification & protein_identification, double p_value_threshold, const String & database_filename)


Load the results of an Inspect search
-----
:param result_filename: Input parameter which is the file name of the input file
:param peptide_identifications: Output parameter which holds the peptide identifications from the given file
:param protein_identification: Output parameter which holds the protein identifications from the given file
:param p_value_threshold
:param database_filename
:raises:
  Exception: FileNotFound is thrown if the given file could not be found
:raises:
  Exception: ParseError is thrown if the given file could not be parsed
:raises:
  Exception: FileEmpty is thrown if the given file is empty




.. py:method:: InspectOutfile.readOutHeader


Cython signature: void readOutHeader(const String & filename, const String & header_line, int & spectrum_file_column, int & scan_column, int & peptide_column, int & protein_column, int & charge_column, int & MQ_score_column, int & p_value_column, int & record_number_column, int & DB_file_pos_column, int & spec_file_pos_column, size_t & number_of_columns)
Read the header of an inspect output file and retrieve various information




