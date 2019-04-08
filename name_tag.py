#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader, select_autoescape
from bs4 import BeautifulSoup
import argparse
import json
import hashlib

'''
dealing with command line arguments, you don't really have to worry about this part!
'''

def check_hexadecimal(value):
    try:
        numeric = int(value,16)
    except ValueError:
        raise argparse.ArgumentTypeError("%s is not a valid hexadecimal value" % value)
    return numeric

parser = argparse.ArgumentParser(description='Make your own name tag for the Feminist Python meetup!')
parser.add_argument('--template', type=str, help='name of the svg file containing your template (in the templates/ directory)', required=True)
parser.add_argument('--colors', help='file that defines the mapping between the colors and pronouns. Should be a json file with the following form {"pronoun":"hex-code"}',
        nargs="?", default="color_mapping.json", type=argparse.FileType("r"))
parser.add_argument('--defaultcolor', type=str, help='the hex-code of the color that is used if no mapping for pronoun is defined in the mapping file', nargs="?", default="009e73")
parser.add_argument('--name', type=str, help='your name', nargs="?", default="Barbara") # like Barbara Liskov as in the Liskov substitution principle
parser.add_argument('--pronouns', type=str, help='your pronouns', nargs="?", default="they, them, theirs")
parser.add_argument('--output', type=str, help='path to the output file for your rendered name tag', nargs="?", default="rendered/output.svg")
parser.add_argument('--fingerprint', help='Encryption Key Fingerprint', nargs="?", type=check_hexadecimal)
parser.add_argument('--gradient', help='flag for dynamically created gradient background',action="store_true")

args = parser.parse_args()
color_map = json.load(args.colors)
default_color = args.defaultcolor
name = args.name 
pronouns = args.pronouns 
template_file = args.template 
output_file = args.output 
fingerprint = args.fingerprint
gradient = args.gradient

'''
load the specified template for the name tag from templates/ folder
'''
env = Environment(
    loader=FileSystemLoader("templates/"),
    autoescape=select_autoescape(['html', 'xml', 'svg'])
)

template = env.get_template(template_file)

'''
set the jinja2 variables in the template to the values we got from the command line
'''
name_tag = template.render(name=name, pronouns=pronouns)

'''
unfortunately we can't use jinja2 to set all variable things (such as background color) in the template :( so we'll use beautifulsoup to manipulate the xml
'''

soup = BeautifulSoup(name_tag, 'xml')

'''
find the backgound and change the color of the "fill" element to the color according to the mapping file
'''

background_tag = soup.find(id="background-rectangle")
background = background_tag["style"].replace("fill:#ffdd55", "fill:#{}".format(color_map.get(pronouns, default_color)))
background_tag["style"] = background

'''
generate the fun squiggly in the top left corner, one way to get numeric data is by getting the unicode code point of each letter in the user's name
'''
# 3,3 14.5,10.5 20,3 26,18
squiggly_tag = soup.find(id="squiggly")

points = []
start_x = 3
start_y = 3
max_length = 23
max_height = 15
x_position = max_length / len(name)
for i, char in enumerate(name):
    x = i * x_position + start_x
    y = ord(char) % max_height + start_y
    point = "{},{}".format(x, y)
    points.append(point)
generated_squiggly = "M " + " ".join(points)

squiggly_tag["d"] = generated_squiggly

'''
add barcode under name block if user gave a public key
'''

breakUpBy = 6
if fingerprint is not None:
    hexstring = hex(fingerprint)[2:]
    colorArray = [hexstring[i:i+breakUpBy] for i in range(0, len(hexstring), breakUpBy)]
    lastColor = colorArray[-1]
    colorArray.remove(colorArray[-1])
    lastColor = lastColor + (breakUpBy-len(lastColor)) * '8'
    colorArray.append(lastColor)
    hashboxes = len(colorArray)
    hash_height = 2.5
    hash_width = 79/hashboxes
    hash_origin = [2.75,38.12] # originX, originY 
    for idx, color in enumerate(colorArray):
        hash_tag = soup.new_tag("rect")
        hash_tag["id"] = "hash-" + str(idx)
        hash_tag["height"] = hash_height
        hash_tag["width"] = hash_width
        hash_tag["x"] = idx * hash_width + hash_origin[0]
        hash_tag["y"] = hash_origin[1]
        color = "#" + color
        hash_tag["style"] = "fill:" + color +";stroke:none;"
        squiggly_tag.insert_after(hash_tag)

'''
make pretty gradient in background by hashing the name and using the hash for 3 hex codes!
'''

if gradient:
   pretty_gradient_tag = soup.find(id="prettyGradient")
   if pretty_gradient_tag is not None:
        hashed_name = hashlib.sha1(name.encode('utf-8')).hexdigest()
        color_one, color_two, color_three = color_map.get(pronouns, default_color), hashed_name[:3], hashed_name[3:6]
    
        top_left = soup.find(id="topLeft")
        top_left["style"] = top_left["style"].replace("stop-color:#ff0000", "stop-color:#{}".format(color_one))
    
        middle = soup.find(id="middle")
        middle["style"] = middle["style"].replace("stop-color:#00cc99", "stop-color:#{}".format(color_two))
    
        bottom_right = soup.find(id="bottomRight")
        bottom_right["style"] = bottom_right["style"].replace("stop-color:#ff99ff", "stop-color:#{}".format(color_three))

'''
write the created/rendered svg to the output file so that you can admire your name tag in inkscape!
'''

output_svg = open(output_file, "w+")
output_svg.write(str(soup))
print("Wrote svg to {}".format(output_file))
