import os
import shutil

# make dir for class rst files
if os.path.isdir("docs/classes"):
    shutil.rmtree("docs/classes")
os.mkdir("docs/classes")

# generate classes.rst for toc of all classes
if os.path.exists("docs/classes.rst"):
    os.remove("docs/classes.rst")
with open("docs/classes.rst", "w") as classes_toc:
    classes_toc.write("""Class Documentation
===================

.. toctree::
   :maxdepth: 2
   :caption: Content:

""")

current_class = ""
with open("doc.rst", "r") as file:
    for l in file:
        if ":module: pyopenms.pyopenms_" in l: # remove pyopenms_1 etc 
            continue
        if l.startswith(".. py:class::"):
            if "(" in l:
                current_class = l[14:].split("(")[0]
            else:
                current_class = l[14:-1]
            # write header for class rst file
            with open(os.path.join("docs/classes", current_class+".rst"), "w") as class_file:
                class_file.write(current_class + "\n")
                class_file.write("=" * len(current_class) + "\n\n")
            # add class to toc for class documentation (classes.rst) if not already in toc
            already_in_toc = False
            with open("docs/classes.rst", "r") as classes_toc:
                if current_class + "\n" in classes_toc.read():
                    already_in_toc = True
            if not already_in_toc:
                with open("docs/classes.rst", "a") as classes_toc:
                    classes_toc.write("   classes/" + current_class + "\n") 
        if current_class:
            with open(os.path.join("docs/classes", current_class+".rst"), "a") as class_file:
                class_file.write(l)