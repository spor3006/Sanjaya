# Sanjaya - The Tactical Braille Interface

Sanjaya is a device which will be helpful for conversion of any printed , E-Document to Braille script alphabet by alphabet.

We can breakdown the process of conversion of text into braille in the following steps: 
  1) Procuring the text article either by capturing the text and saving it or in case of an E-document converting it into any image format(JPEG, PNG etc.)
  2) Optical Charcater Recognition using Deep Learning Nueral Networks and converting the text in the image into string of apha-numeric characters.
  3) Passing the text into the Braille Interface charcter by character.
  4) Using the Braille Interface to display the character one by one in required time interval.
  
  
Let us discuss one by one what was used in our model.

  1)For caprturing the image we used Raspberry Pi Camera V2 8 MP High resolution camera attached to a temporary base. The captured image shall be stored in the same directory as of the where the OCRFinal code shall run. In case of an E-document directly store the image in the Directory where the code will run.
  
  2) Optical Character Recognition was done through a famous Open Source Model named as Tesseract OCR. This shall directly give us the text in the image and will be stored in a string.
  
  3) Now the we shall pass the alphabets in the string letter by letter using into the Braille Interface
  
  4) The Braille Interface is made of two ocatgonal wheels. Each wheel which contain all the combinations of the 3 dots on a surface.
  Now to obtain the required alphabet/character we need to find the correct permuation of both the wheels and then we can set the angles on both of them to obtain the required result. After a specific delay period it is reset to initial condition and then again we can obtain the required combinatation of the next character.
  
  Thus we can use this interface to obtain 64 unique characters.
  
  
  
