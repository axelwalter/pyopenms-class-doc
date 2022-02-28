FASTAFile
=========

.. py:class:: FASTAFile


   Bases: :py:class:`object`


Cython implementation of _FASTAFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FASTAFile.html




.. py:method:: FASTAFile.atEnd


Cython signature: bool atEnd()
Boolean function to check if streams is at end of file




.. py:method:: FASTAFile.load


Cython signature: void load(const String & filename, libcpp_vector[FASTAEntry] & data)
Loads a FASTA file given by 'filename' and stores the information in 'data'




.. py:method:: FASTAFile.readNext


Cython signature: bool readNext(FASTAEntry & protein)


Reads the next FASTA entry from file
-----
If you want to read all entries in one go, use load()
-----
:returns: true if entry was read; false if eof was reached
:raises:
    Exception:FileNotFound is thrown if the file does not exists
:raises:
    Exception:ParseError is thrown if the file does not suit to the standard




.. py:method:: FASTAFile.readStart


Cython signature: void readStart(const String & filename)


Prepares a FASTA file given by 'filename' for streamed reading using readNext()
-----
:raises:
    Exception:FileNotFound is thrown if the file does not exists
:raises:
    Exception:ParseError is thrown if the file does not suit to the standard
Reads the next FASTA entry from file
-----
If you want to read all entries in one go, use load()
-----
:returns: true if entry was read; false if eof was reached
:raises:
    Exception:FileNotFound is thrown if the file does not exists
:raises:
    Exception:ParseError is thrown if the file does not suit to the standard




.. py:method:: FASTAFile.store


Cython signature: void store(const String & filename, libcpp_vector[FASTAEntry] & data)
Stores the data given by 'data' at the file 'filename'




.. py:method:: FASTAFile.writeEnd


Cython signature: void writeEnd()
Closes the file (flush). Called implicitly when FASTAFile object does out of scope




.. py:method:: FASTAFile.writeNext


Cython signature: void writeNext(const FASTAEntry & protein)


Stores the data given by `protein`. Call writeStart() once before calling writeNext()
-----
Call writeEnd() when done to close the file!
-----
:raises:
    Exception:UnableToCreateFile is thrown if the process is not able to write to the file (disk full?)




.. py:method:: FASTAFile.writeStart


Cython signature: void writeStart(const String & filename)


Prepares a FASTA file given by 'filename' for streamed writing using writeNext()
-----
:raises:
    Exception:UnableToCreateFile is thrown if the process is not able to write to the file (disk full?)
Stores the data given by `protein`. Call writeStart() once before calling writeNext()
-----
Call writeEnd() when done to close the file!
-----
:raises:
    Exception:UnableToCreateFile is thrown if the process is not able to write to the file (disk full?)




