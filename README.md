# Name tag workshop (09-04-2019)
# Quick start
1. Clone this repository or download and unzip the zip file from Github
2. Create and start a virtual environment
3. Install the dependencies: pip install -r requirements.txt

You should end up with the following files in your installation directory.
```
├── color_mapping.json
├── name_tag.py
├── README.md
├── rendered
│   └── output.svg
├── requirements.txt
└── templates
    ├── gradient.svg
    └── template.svg
```

You can check out the program parameters by using the `-h` or `--help` parameter:
``` python3 name_tag.py -h ``` or `python3 name_tag.py --help`
``` 
Make your own name tag for the Feminist Python meetup!

optional arguments:
  -h, --help            show this help message and exit
  --template TEMPLATE   name of the svg file containing your template (in the
                        templates/ directory)
  --colors [COLORS]     file that defines the mapping between the colors and
                        pronouns. Should be a json file with the following
                        form {"pronoun":"hex-code"}
  --defaultcolor [DEFAULTCOLOR]
                        the hex-code of the color that is used if no mapping
                        for pronoun is defined in the mapping file
  --name [NAME]         your name
  --pronouns [PRONOUNS]
                        your pronouns
  --output [OUTPUT]     path to the output file for your rendered name tag
  --fingerprint [FINGERPRINT]
                        Encryption Key Fingerprint
  --gradient [GRADIENT]
                        flag for dynamically created gradient background
```

# Running the program
Running the program with the "basic" template and using the default arguments
` python3 name_tag.py --template template.svg `

Running the program with your name and pronouns
` python3 name_tag.py --template template.svg --name Saara --pronouns "she, her, her's" `

Running the program with your name and pronouns and using a dynamically created gradient background
` python3 name_tag.py --template gradient.svg --name Saara --pronouns "she, her, her's" `

# Color mapping
The color mapping and name tags were inspired by these [name tags](https://now.uiowa.edu/sites/now.uiowa.edu/files/wysiwyg_uploads/LGBTQ%20Pronoun%20nametags.jpg).
`color_mapping.json`
```
{
  "she, her, hers": "ffd200",
  "he, him, his": "e69f00" ,
  "they, them, theirs": "d55e00",
  "xe, xem, xyrs": "cc79a7",
  "ze, hir, hirs": "56b4e9" 
}
```
- ![#ffd200](https://placehold.it/15/ffd200/000000?text=+) `#ffd200`
- ![#e69f00](https://placehold.it/15/e69f00/000000?text=+) `#e69f00`
- ![#d55e00](https://placehold.it/15/d55e00/000000?text=+) `#d55e00`
- ![#cc79a7](https://placehold.it/15/cc79a7/000000?text=+) `#cc79a7`
- ![#56b4e9](https://placehold.it/15/56b4e9/000000?text=+) `#56b4e9`

# BeautifulSoup intro
[bs4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
## useful commands
* creating the soup
`soup = BeautifulSoup(mySvg, "xml")`
* find by id
`soup.find(id="smallCircle")`
* get attribute in tag
`soup.find(id="smallCircle")["fill"]`
* modify attribute in tag
`soup.find(id="smallCircle")["fill"] = "black"`
* create new tag
`soup.new_tag("circle")`
## short example
[Online SVG editor](https://www.w3schools.com/graphics/tryit.asp?filename=trysvg_myfirst)
``` python
>>> from bs4 import BeautifulSoup
>>> mySvg = '''<svg width="300" height="300">
   <circle cx="50" cy="50" r="20" stroke="green" stroke-width="4" fill="yellow" id="smallCircle"/>

   <circle cx="150" cy="150" r="40" stroke="red" stroke-width="4" fill="blue" id="bigCircle"/>
  
</svg> '''

>>> soup = BeautifulSoup(mySvg, "xml")
# finding XML elements

# you can find elements based on their tag
>>> soup.find_all("circle")
[<circle cx="50" cy="50" fill="yellow" id="smallCircle" r="20" stroke="green" stroke-width="4"/>, <circle cx="150" cy="150" fill="blue" id="bigCircle" r="40" stroke="red" stroke-width="4"/>]
# you can find elements based on their id
>>> soup.find(id="smallCircle")
<circle cx="50" cy="50" fill="yellow" id="smallCircle" r="20" stroke="green" stroke-width="4"/>
# you can access a tags attributes using the dictionary syntax
>>> soup.find(id="smallCircle")["fill"]
'yellow'

# manipulating the XML file
# you can use the dictionary assignment syntax to change the value of a tag's attribute
>>> soup.find(id="smallCircle")["stroke"] = "black"
>>> soup
<circle cx="50" cy="50" fill="yellow" id="smallCircle" r="20" stroke="black" stroke-width="4"/>
<circle cx="150" cy="150" fill="blue" id="bigCircle" r="40" stroke="red" stroke-width="4"/></svg>
# you can create a new tag using new_tag()
>>> medium = soup.new_tag("circle")
>>> medium
<circle/>
# and let's create some attributes for the tag
>>> medium["cx"] = 150
>>> medium["cy"] = 150
>>> medium["r"] = 30
>>> medium["fill"] = "purple"
>>> medium["id"] = "mediumCircle"
>>> medium
<circle r="30" cx="100" cy="100" fill="purple"/>
# but our new medium-sized circle isn't part of the soup yet :(
>>> soup
<?xml version="1.0" encoding="utf-8"?>
<svg height="300" width="300">
<circle cx="50" cy="50" fill="yellow" id="smallCircle" r="20" stroke="black" stroke-width="4"/>
<circle cx="150" cy="150" fill="blue" id="bigCircle" r="40" stroke="red" stroke-width="4"/></svg>
# we can insert our tag to the soup using several different methods, e.g. insert_after(), which inserts our tag after some other element in the tree
>>>soup.find(id="bigCircle").insert_after(medium)
>>> soup
<?xml version="1.0" encoding="utf-8"?>
<svg height="300" width="300">
<circle cx="50" cy="50" fill="yellow" id="smallCircle" r="20" stroke="black" stroke-width="4"/>
<circle cx="150" cy="150" fill="blue" id="bigCircle" r="40" stroke="red" stroke-width="4"/><circle cr="30" cx="150" cy="150" fill="purple"/></svg>
# if you want to copy the svg into the svg editor you only need the svg tag
>>> soup.svg
<svg height="300" width="300">
<circle cx="50" cy="50" fill="yellow" id="smallCircle" r="20" stroke="black" stroke-width="4"/>
<circle cx="150" cy="150" fill="blue" id="bigCircle" r="40" stroke="red" stroke-width="4"/><circle cr="30" cx="150" cy="150" fill="purple"/></svg>
```
# Adding generative art to the name tags
## Ideas
* different kinds of squiggles (change stroke, color etc.)
* flags, e.g. are you allowed to be photographed
* gradient
* embedding images
* patterns/shapes e.g. "barcode"
* maybe the color palettes in the gradient could be prettier ([color palettes for python](https://jiffyclub.github.io/palettable/#finding-palettes))

## Ways to get "data" for generative art
* use unicode code points of name/pronouns
* use hash of name/pronouns ([how inputs affect the hash](https://tantemalkah.at/2019/fempy_hashing/#/2/3))
* pgp public key 

## Inspiration
* [bleeptrack](https://www.bleeptrack.de/) created [badges](https://chaos.social/@bleeptrack/101637293852959794) for a wikidata workshop
* [badges](https://35c3.bleeptrack.de/) for 35c3
* [sha2017 design generator](https://sha2017.org/design/)


