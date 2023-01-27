# Ascii-To-C
Python program to turn Ascii Art text into C/C++ print statements

HOW TO USE:

1) Generate text in https://patorjk.com/software/taag/ (may work with other websites)
2) Copy and paste in asciiInput.txt (it already contains an example)
3) Execute main.py
4) Select C (printf) or C++ (cout)
5) Result will be stored in asciiOutput.txt, ready to be printed in C/C++

Features:
  * C++: Adds cout<< at the beginning, \n; at the end, and puts the text between quotation marks.
  * C: Adds printf(" at the beginning, puts the text between quotation marks, and finally \n and ; are added.
  * C and C++: Changes all the backslashes (\) to double backslashes (\\) for escaping the character so it can be printed OK.
