# Virtual Maths Camp Content Toolchain

This is a tool chain for converting content (puzzles, fun facts, games) from
Google Docs into various serving formats. It consists of a Google Apps script
and various python3 scripts.

## Setup

1. Ensure you have python >= 3.6 installed.

2. Install the CommonMark python library: https://pypi.org/project/commonmark/

3. Open the Google Docs "Content/Export test" in the Virtual maths camp Google
Drive folder. In the menu, select Tools -> Script Editor. The code editor
should already contain the content of `gdocs2md.gs` from this repository.
If it doesn't, paste it into the code editor and save it (File -> Save).
Then follow the installation instructions from the **Note** in
https://github.com/lmmx/gdocs2md-html

## Running the pipeline

The pipeline consists of various stages. 

### Google Docs to Markdown

Open the Google Docs "Content/Export test" in the Virtual maths camp Google
Drive folder. In the menu, select Tools -> Script Editor. 
Select `onInstall` from the functions dropdown menu and run it.
In the main document's menu, a *Markdown* should have appeared.
(Also see https://github.com/lmmx/gdocs2md-html for more details.)
Select Markdown -> Export to Markdown -> Export entire folder to local file.

This will create a Markdown subfolder within the Content folder, and
populate it with the content converted to Markdown format.

Note: If the script runs for longer than 6 minutes, you will get an error
saying that the script has timed out. You can simply rerun the script
multiple times until it has processed all content (indicated by a lack
of such error). This works as the script does not process already processed
content unless the corresponding GDoc file has been modified in the meantime.

### Markdown to json

Download the Markdown folder produced by the previous step, and place it in
your local copy of this repository. Run `md_to_json.py`.
This will create a `json/` folder containing each piece of content from
the Markdown folder converted to JSON.

### Various output formats.

TBD. Still have to clean up the code.
