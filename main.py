import Neutron

win = Neutron.Window("Example", size=(600,600))

# The loader covers while all the other elements and css loads
win.loader(content="<h1>Loading App...</h1>", color="#fff", after=lambda: win.toggle_fullscreen())


def setName():
    name = win.getElementById("inputName").value
    win.getElementById("title").innerHTML = "Hello: " + name


win.display(f"""
<!DOCTYPE html>
<html>
   <head lang="en">
      <meta charset="UTF-8">
   </head>
   <body>
      <h1 id="title">Hello: </h1>
      <input id="inputName">
      <button id="submitName" onclick="{Neutron.event(setName)}">Submit</button>
   </body>
</html>
""")
win.show()