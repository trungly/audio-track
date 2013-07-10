import sys, os
import xml.etree.ElementTree as ET


###############################################################################
### Set up the first set of questions and choices
###############################################################################
answers = []
questions = [
    {
        "title": "What is the Audio Configuration?",
        "print_choices_horizontally": False,
        "choices": [
            "BOTH Discrete Multi Track 5.1 MOV & Discreet Multi Track Stereo MOV",
            "ONLY Discreet Multi Track Stereo MOV"
        ]
    },
    {
        # This question is only asked if the first selection was Multi Track Stereo
        "title": "What is the Audio Channel Assignment",
        "print_choices_horizontally": False,
        "choices": [
            "Left (or) Right",
            "Left Total (or) Right Total",
            "Mono (or) Mono"
            # "Front Center",
            # "Left",
            # "Left Total",
            # "LFE",
            # "Mono",
            # "Rear Center",
            # "Rear Left",
            # "Rear Right",
            # "Right",
            # "Right Total",
            # "Side Left",
            # "Side Right",
            # "Surround",
            # "Dolby E 1",
            # "Dolby E 2",
            # "MOS",
        ]
    },
    {
        "title": "What is the Audio Content?",
        "print_choices_horizontally": False,
        "choices": [
            "Composite",
            "Dialogue",
            "M&E",
            "Music",
            "FX",
            "Narration",
            "Laughter",
            "Sync",
            "MOS",
        ]
    },
    {
        "title": "What is the Language",
        "print_choices_horizontally": True,
        "choices": [
            "Afghan/Pushto",
            "Afrikaans",
            "Albanian",
            "Arabic",
            "Bangla / Bengali",
            "Bhojpuri",
            "Bulgarian",
            "Burmese",
            "Cantonese",
            "Catalan",
            "Chinese (Cantonese)",
            "Chinese (Mandarin Simplified) [Text]",
            "Chinese (Mandarin Traditional) [Text]",
            "Chinese (Mandarin, PRC)",
            "Chinese (Mandarin, Taiwanese)",
            "Chinese (Taiwanese)",
            "Corsican",
            "Croatian",
            "Czech",
            "Danish",
            "Dutch (Flemish)",
            "Dutch (Netherlands)",
            "English",
            "Estonian",
            "Finnish",
            "French - Continental",
            "French (Canadian)",
            "French (Parisian)",
            "Gaelic (Irish)",
            "Gaelic (Scots)",
            "Georgian",
            "German",
            "German (Austrian)",
            "German (Germany)",
            "German (Swiss)",
            "German [Text]",
            "Greek",
            "Hebrew",
            "Hindi",
            "Hungarian",
            "Icelandic",
            "Indonesian / Bahasa",
            "Inuktitut",
            "Italian",
            "Japanese",
            "Kannada",
            "Khmer",
            "Korean",
            "Kurdish",
            "Lao",
            "Latvian",
            "Lithuanian",
            "Macedonian",
            "Malay",
            "Malayalam",
            "Maori",
            "Marathi",
            "Nepali",
            "None",
            "Norwegian",
            "Persian / Farsi",
            "Polish",
            "Portuguese (Brazil)",
            "Portuguese (Portugal)",
            "Punjabi",
            "Romanian",
            "Russian (Russia)",
            "Russian (Ukraine)",
            "Serbian",
            "Serbo-Croatian",
            "Sindi",
            "Sinhalese",
            "Slovak",
            "Slovene",
            "Spanish (Argentinean)",
            "Spanish (Castilian)",
            "Spanish (Chilean)",
            "Spanish (Colombian)",
            "Spanish (Cuban)",
            "Spanish (Latin Am)",
            "Spanish (Mexican)",
            "Spanish (Puerto Rican)",
            "Swahili",
            "Swedish",
            "Tagalog",
            "Tamil",
            "Telugu",
            "Thai",
            "Tibetian",
            "Turkish",
            "Ukranian",
            "Urdu",
            "Vietnamese",
            "Welsh",
            "Yiddish",
            "Zulu",
        ]
    }
]


###############################################################################
### Convenience functions
###############################################################################
def error(msg, *args, **kwargs):
    print ("\033[91m" + msg + "\033[0m").format(*args, **kwargs)

def info(msg, *args, **kwargs):
    print ("\033[92m" + msg + "\033[0m").format(*args, **kwargs)

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def get_selection(question):
    if not answers:
        raise Exception("The questions haven't been answered yet")
    if question >= len(questions):
        return answers[question]
    if not isinstance(answers[question], (int, long)):
        return 'N/A'
    return questions[question].get('choices')[answers[question]-1]

def slugify(string):
    return None if not string else string.replace('/','_').replace(' ','_')


###############################################################################
### Get the input file, check it, and load it
###############################################################################
if len(sys.argv) != 2:
    error("\nUsage: ./{} <input_file_name>\n", sys.argv[0])
    exit(1)

try:
    input_file = open(sys.argv[1])
    tree = ET.parse(input_file)
except IOError as ioe:
    error("\nCould not load input file: {}\n", sys.argv[1])
    exit(1)
except ET.ParseError as pe:
    error("\nCould not parse input file. Are you sure it is an XML file?\n")
    exit(1)


###############################################################################
### Loop over the questions and grab the answers, doing some rudimentary
### checking on whether the user's numerical answer is in range
###############################################################################
for i, question in enumerate(questions):

    if i == 1 and answers[0] == 1: # Hack to skip question #2 in a certain case
        answers.append(None)
        continue

    answer_is_valid = False
    while not answer_is_valid:
        print "\nEnter the {}:".format(question.get('title'))
        choices = question.get('choices')
        if question.get('print_choices_horizontally'):
            for i, choice in enumerate(choices):
                print "{}) {}".format(i+1, choice), # comma here to print choices on same line
            print ""
        else:
            for i, choice in enumerate(choices):
                print "{}) {}".format(i+1, choice)
        answer = raw_input("> ")
        try:
            answer = int(answer)
            if answer < len(choices)+1:
                answers.append(answer)
                answer_is_valid = True
                continue
        except:
            pass
        error("Invalid answer!")
    info("You answered: {}", choices[answer-1])

# Ask the last question and grab the answer
print "\nWhat is the File Name?"
file_name = raw_input("> ")
info("You answered: {}", file_name)
answers.append(file_name)

print "\nYour answers: ", [get_selection(i) for i in range(0,4)] + [answers[4]]


###############################################################################
### Create the XML output file
###############################################################################

def create_audiochannelcomponent(filename, num, assignment):
    """
    EXAMPLE:
    <a:audiochannelcomponent>
        <a:filedescriptors>
            <a:filedescriptor>
                <a:filename>ANTHROPOLOGY_DiscreteMultipleTracks.mov</a:filename>
                <a:encodingequipment></a:encodingequipment>
                <a:encodingprofile></a:encodingprofile>
                <a:checksumvalue></a:checksumvalue>
                <a:checksumtype></a:checksumtype>
                <a:encodedate></a:encodedate>
                <a:encodevendororganizationname></a:encodevendororganizationname>
            </a:filedescriptor>
        </a:filedescriptors>
        <a:audiochannelinfile>3</a:audiochannelinfile>
        <a:audiochannelontape>3</a:audiochannelontape>
        <a:audiochannelassignment>Front Center</a:audiochannelassignment>
        <a:audiostreaminfile>1</a:audiostreaminfile>
    </a:audiochannelcomponent>
    """
    acc = ET.Element('a:audiochannelcomponent')
    fds = ET.Element('a:filedescriptors')
    fd = ET.Element('a:filedescriptor')
    fn = ET.Element('a:filename')
    fn.text = filename
    acif = ET.Element('a:audiochannelinfile')
    acif.text = num
    acot = ET.Element('a:audiochannelontape')
    acot.text = num
    aca = ET.Element('a:audiochannelassignment')
    aca.text = assignment
    asif = ET.Element('a:audiostreaminfile')
    asif.text = "1"

    fd.extend([
        fn,
        ET.Element('a:encodingequipment'),
        ET.Element('a:encodingprofile'),
        ET.Element('a:checksumvalue'),
        ET.Element('a:checksumtype'),
        ET.Element('a:encodedate'),
        ET.Element('a:encodevendororganizationname'),
    ])
    fds.append(fd)
    acc.extend([fds, acif, acot, aca, asif])

    return acc


ET.register_namespace('e', 'http://schema.dadcdigital.com/dbb/data/2010/externaltask/logging')
ET.register_namespace('t', 'http://schema.dadcdigital.com/dbb/data/2010/externaltask/')
ET.register_namespace('i', 'http://www.w3.org/2001/XMLSchema-instance')
ET.register_namespace('z', 'http://schemas.microsoft.com/2003/10/Serialization/')
ET.register_namespace('a', 'http://schema.dadcdigital.com/dbb/data/2010/inventory/')


root = tree.getroot()

components = root[1][6][0][3]

if answers[0] == 1: # both 5.1 and stereo
    # create 5.1 component
    audio_component = ET.Element('a:component', {'type': 'Audio Track Component'})
    a_config = ET.Element('a:audioconfiguration')
    a_config.text = 'Discrete Multi Track 5.1 MOV'
    a_content = ET.Element('a:audiocontent')
    a_content.text = get_selection(2)
    language = ET.Element('a:language')
    language.text = get_selection(3)
    a_components = ET.Element('a:audiochannelcomponents')
    for i, assignment in enumerate(['Left', 'Right', 'Front Center', 'LFE', 'Rear Left', 'Rear Right']):
        acc = create_audiochannelcomponent(get_selection(4), str(i+1), assignment)
        a_components.append(acc)
    audio_component.extend([a_config, a_content, language, a_components])
    components.append(audio_component)

#create stereo component
audio_component = ET.Element('a:component', {'type': 'Audio Track Component'})
a_config = ET.Element('a:audioconfiguration')
a_config.text = 'Discrete Multi Track Stereo MOV'
a_content = ET.Element('a:audiocontent')
a_content.text = get_selection(2)
language = ET.Element('a:language')
language.text = get_selection(3)
a_components = ET.Element('a:audiochannelcomponents')
if answers[0] == 1:
    assignments = ['Left Total', 'Right Total']
    offset = 6 # so that audiochannelinfile & audiochannelontape are 7 and 8
else:
    splitted = get_selection(1).split(' (or) ')
    assignments = [splitted[0], splitted[1]]
    offset = 0
for i, assignment in enumerate(assignments):
    acc = create_audiochannelcomponent(answers[4], str(offset + i + 1), assignment)
    a_components.append(acc)
audio_component.extend([a_config, a_content, language, a_components])

components.append(audio_component)

indent(root)

display_code = slugify(components[0][3][0][0][0].text)
title_name = slugify(root[1][2].text)
episode_number = slugify(root[1][5].text)
language = slugify(get_selection(3))
output_filename = "{}{}{}{}_DiscreteMultipleTracks.xml".format(
    (display_code + "_") if display_code else "",
    (title_name + "_") if title_name else "",
    (episode_number + "_") if episode_number else "",
    language
)
info("\nWriting file {} ...", format(output_filename))

tree.write(output_filename, encoding='UTF-8', xml_declaration=False)
