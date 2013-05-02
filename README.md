# Audio Track XML generation script

This is a simple command line tool that generates an XML file based on an input XML file and some user input.

#####Example execution:
>./add-audio-track input.xml

  AUDIO CONFIGURATION:
	
	1) Discrete Multi Track 5.1 MOV
	2) Discreet Multi Track Stereo MOV
	3) Both
	
	(The following question is asked ONLY if 2 or 3 is selected above)
	AUDIO CHANNEL ASSIGNMENT:
	1) Front Center
	2) Left
	3) Left Total
	4) LFE
	5) Mono
	6) Rear Center
	7) Rear Left
	8) Rear Right
	9) Right
	10) Right Total
	11) Side Left
	12) Side Right
	13) Surround
	14) Dolby E 1
	15) Dolby E 2
	16) MOS
	
	AUDIO CONTENT:
	1) Composite
	2) Dialogue
	3) M&E
	4) Music
	5) FX
	6) Narration
	7) Laughter
	8) Sync
	9) MOS
	
	LANGUAGE: (Press Enter to select English)
	1) Afghan/Pushto
	2) Afrikaans
	3) Albanian
	4) Arabic
	5) Bangla / Bengali
	6) Bhojpuri
	7) Bulgarian
	8) Burmese
	9) Cantonese
	10) Catalan
	11) Chinese (Cantonese)
	12) Chinese (Mandarin Simplified) [Text]
	13) Chinese (Mandarin Traditional) [Text]
	14) Chinese (Mandarin, PRC)
	15) Chinese (Mandarin, Taiwanese)
	16) Chinese (Taiwanese)
	17) Corsican
	18) Croatian
	19) Czech
	20) Danish
	21) Dutch (Flemish)
	22) Dutch (Netherlands)
	23) English
	24) Estonian
	...
	<snipped for brevity>
	...
	
	FILE NAME:
	<free-form text input>

##### Example Output:
>An XML file in the current directory named "223243_ANTHROPOLOGY 101 - DiscreteMultipleTracks-PHSTEST_FROMVENDOR.xml" with the <a:component type="Audio Track Component"> section populated
