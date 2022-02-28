TextFile
========

.. py:class:: TextFile


   Bases: :py:class:`object`


Cython implementation of _TextFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TextFile.html




.. py:method:: TextFile.addLine


Cython signature: void addLine(const String line)




.. py:method:: TextFile.load


Cython signature: void load(const String & filename, bool trim_linesalse, int first_n1)


Loads data from a text file
-----
:param filename: The input file name
:param trim_lines: Whether or not the lines are trimmed when reading them from file
:param first_n: If set, only `first_n` lines the lines from the beginning of the file are read
:param skip_empty_lines: Should empty lines be skipped? If used in conjunction with `trim_lines`, also lines with only whitespace will be skipped. Skipped lines do not count towards the total number of read lines




.. py:method:: TextFile.store


Cython signature: void store(const String & filename)
Writes the data to a file




