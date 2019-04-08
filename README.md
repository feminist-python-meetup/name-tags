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
