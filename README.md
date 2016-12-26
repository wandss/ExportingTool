# ExportingTool
WebApp for Exporting Documents from CMIS compliant repositories.
This app, made in Python / Django is destinated to ECM administrators.
It is not intended for a final user.

With this app is possible to download many files from a CMIS compliant repository and choosing these file's names to be created from it's metada.

Within the "ECM world", once a document is in the software, we don't guide ourselves by that file's name, instead we use metada or the content from the file itself.
When its needed to download a bunch of files at once, normally you don't know what these files are realated to after downloading them, since the metada its not exported with them.

With this tool you can choose which metadata will be used to compose the downloaded file's name.
