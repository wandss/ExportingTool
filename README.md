# ExportingTool
### What it is:
This is a web aplication for Exporting Documents from CMIS compliant repositories.
It was created specifically to attend some particularities from IBM's FileNet, but it will connect to any CMIS compliant repository and can be modified to be compatible with any repository's particularities.
This app, made in Python / Django is destinated to ECM administrators and users the amazing Apache cmislib package: https://chemistry.apache.org/python/cmislib.html

It is not intended for a final user.

With this app is possible to download many files from a CMIS compliant repository and choosing these file's names to be created from it's metadata.

Within the "ECM world", once a document is in the "software", we don't guide ourselves by that file's name, instead we use metadata or the content from the file itself.
When its needed to download a bunch of files at once, normally we don't know what these files are realated to after downloading them, since the metadata its not exported along.

With this tool its possible to choose which metadata will be used to compose the downloaded file's name.

Let's take a sample file called "My_File.pdf". We have no ideia about it's contents. Inside an ECM domain or system we have some metadata related to this file like: "Create date, Year, Contract Number" and so on. So, within the system it's possible to know "what" is that file without checking it's name or even opening it. If we download it thought we are going to have a "My_File.pdf". With this tool we say that we want "My_File.pdf" to be named as: "0012345-2016.pdf" after the download; been theese values extracted from the contract number and year metadata for this specific file.

Whenever I was requested to export (download) many files, I was forced to edit this basic script I've created in the past. So why not automate this task to allows me identifying which metadata I want to use, and just run whihtout having to edit scripts all over again?

So this tool was born.......

This program was made to help me on a particular issue but been the world as big as it is, who knows if it can't help anybody else.
So... let me know if it can be usefull in some way.

###Installing:
After installing: Python 2.7 and Django, install cmislib. I suggest installing with pip.

Clone the repository:



###How to use:
