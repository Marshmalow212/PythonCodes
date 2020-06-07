#6.5 Write code using find() and string slicing (see section 6.10) to 
#extract the number at the end of the line below. Convert the extracted 
#value to a floating point number and print it out.

t = "X-DSPAM-Confidence:    0.8475"

pos = t.find('0')
s = t[pos:]
s = float(s)
print(s)