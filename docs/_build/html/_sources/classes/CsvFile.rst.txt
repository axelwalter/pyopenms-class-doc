CsvFile
=======

.. py:class:: CsvFile


   Bases: :py:class:`object`


Cython implementation of _CsvFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1CsvFile.html




.. py:method:: CsvFile.addRow


Cython signature: void addRow(const StringList & list)
Add a row to the buffer




.. py:method:: CsvFile.clear


Cython signature: void clear()
Clears the buffer




.. py:method:: CsvFile.getRow


Cython signature: bool getRow(int row, StringList & list)
Writes all items from a row to list




.. py:method:: CsvFile.load


Cython signature: void load(const String & filename, char is_, bool ie_, int first_n)
Loads data from a text file




.. py:method:: CsvFile.store


Cython signature: void store(const String & filename)
Stores the buffer's content into a file




