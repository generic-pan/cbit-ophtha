## INSERTNAMEHERE Plugins

A INSTERNAMEHERE plugin is a Python setuptools package which satisfies the following conditions:

 1. There is a non-standard tag, **plugin_key**, which contains a UUID that identifies the plugin.
 2. There is a non-standard tag, **plugin_name**, which is the *display name* of the plugin 
 2. There is a **signature** key that cryptographically signs the plugin.  (This is for HIPAA compliance)
 3. Some optional setuptools tags are required:

       **license**
       **version**
       **author**
       **author_email**
       **url**
 4. The **url** tag is a link to the plugin on our app store (see exampe below)
 5.  There is an entry-point, called plugin.py, which runs the code that processes an input image.

 In production, there would be an online plugin store, which would sign plugins and assign a plugin key  For the MVP, this is done manually.

Example:
 
 ```
from setuptools import setup


setup(
    name = "glaucoma_ai",
    version = "1.0",
    plugin_key="69283bb3-20e7-4c0f-9b57-fd7b9f5b84c8", 
    plugin_signature = 'f3626e8a-8159-45c5-81a5-1cea097df304',
    plugin_name="Glaucoma AI",
    author = "Andrew Carter",
    author_email = "andrewjcarter@gmail.com",
    license = "MIT",
    url = "http://ourappstore.INSERTNAMEHERE.com/glaucoma_ai",
    packages=['an_example_pypi_project', 'tests']
)
 ```