# TMT
Microsoft Threat Modeling Tool python scripts to increase TMT’s utility for both template developers and model makers.

scripts for .tb7 template files:
-	template2csv.py - enumerate a template's elements, threat categories, and threats, and threat logic. Save elements and threats as csv file.

- csv2template.py - script to convert the template.csv back to a .tb7 file. Ideally for merging, you'd import new threats then modify the threat logic to fit your template with a find & replace in excel


scripts for .tm7 model files:
-	model2csv.py - enumerate extra information from a model which we cannot get from TMT's built-in csv threat file. ex: notes, custom properties. Keep as separate csv file in conjunction with the TMT produced csv file.

View threat_modeling_notes.txt for more
