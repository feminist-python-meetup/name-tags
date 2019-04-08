# BeautifulSoup
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

