import os
from odf.opendocument import OpenDocumentText
from odf.text import P, Span

class inout:
    def __init__(self) -> None:
        """
        Constructor for this class... doesn't do anything too exciting. This is a class of methods. OOP does not dwell here...
        """

    def __repr__(self) -> str:
        return 'This is a class of useful methods because I like my stuff tidy. Stop inspecting things and do something productive!'
    def __str__(self) -> str:
        return 'This is a class of useful methods because I like my stuff tidy. Stop inspecting things and do something productive!'

    @classmethod
    def read_txt(cls, filepath) -> None:
        """
        Class method that takes in a text file ready for further processing. This should not be a surprise if your IQ is above 20.
        Args:
            filepath (str): Take a wild guess Sherlock.
        """
        try:
            cls.filepath = filepath
            with open(cls.filepath, 'r', encoding='utf-8') as file:
                cls.content = file.read()
            return cls.content
        except Exception as e:
            print(f"You've got an error pal. Maybe your file doesn't exist, or you don't have permission to read it. Or you fat-fingered the filepath.\n{e}")
    
    @classmethod
    def save_txt(cls, filepath, content) -> None:
        """
        Saves the transliterated text into a txt file, and appends '-futhorc' to the end.

        Args:
            filepath (str): Just give this the filepath var you used for the read_txt path. 
            content (str): The content you want to write to the txt file. Wow. Such original. Mucho amaze.
        """
        cls.content = content
        cls.filepath = filepath
        cls.base, cls.ext = os.path.splitext(cls.filepath)
        cls.new_filename = f"{cls.base}-futhorc{cls.ext}"
        try:
            with open(cls.new_filename, 'w', encoding='utf-8') as file:
                file.write(cls.content)
        except Exception as e:
            print(f"It's error time again! Maybe you don't have permission to write to the location... Whatever.\n{e}")
    @classmethod
    def save_as_odt(cls, filepath, content) -> None:
        """
        Saves the transliterated text into a. odt file, and appends '-futhorc' to the end.

        Args:
            filepath (str): Just give this the filepath var you used for the read_txt path. 
            content (str): The content you want to write to the odt file. Wow. Such original. Mucho amaze.
        """
        cls.content = content
        cls.filepath = filepath
        cls.base, cls.ext = os.path.splitext(cls.filepath)
        cls.new_filename = f"{cls.base}-futhorc.odt"
        try:
            cls.lines = content.split('\n')
            cls.doc = OpenDocumentText()
            for line in cls.lines:
                cls.p = P()
                cls.p.addElement(Span(text=line))
                cls.doc.text.addElement(cls.p)
            cls.doc.save(cls.new_filename)
        except Exception as e:
            print(f"Uh oh. Something went wrong saving it as a libreoffice doc. Sorry pal:\n{e}")