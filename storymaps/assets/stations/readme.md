# Station photo naming convention and processing

Photos originate from G:\My Drive\GPS Utah\GPS Station Photos.

Organize them into a folder and rename them with 4-digit code_name-Antenna and Receiver like below and don't add `-#`.jpg files to storymap.

- `UTAI_Antelope-Island-Antenna.jpg`
- `UTAI_Antelope-Island-Antenna-2.jpg`
- `UTAI_Antelope-Island-Receiver.jpg`
- `UTAI_Antelope-Island-Receiver-2.jpg`
  - most likely don't use these image in storymap
- `UTAI_Antelope-Island-Desk.jpg`
- `UTAI_Antelope-Island-Rack.jpg`
- `UTAI_Antelope-Island-etcetcetc.jpg`

Use CMD with wildcards to fix the case of the file extensions

ex. G:\My Drive\GPS Utah\GPS Station Photos\Richfield>`rename *.JPG *.jpg`

Copy them to `C:\_Git\turn-gps\storymaps\assets\stations`

Open new images with _Windows Photos_

Rotate and Resize to Small -> Save and overwrite existing

Run `image-fixer.py` on new images

- C:\_Git\turn-gps\src> `.env\Scripts\activate.bat`

- `(.env) C:\_Git\turn-gps\src> 'python image-fixer.py -d ..\storymaps -r'`
- `(.env) C:\_Git\turn-gps\src> 'python image-fixer.py -d ..\storymaps\assets\stations -w UTWE_*'`
or
- `(.env) C:\_Git\turn-gps> 'python src\image-fixer.py -d storymaps/test -w IDHD_*'`

### Commit changes to a `New Branch` and `Bring my changes over` then `Publish Branch` or `Push origin` (in desktop)
### Open Pull Request in GitHub then `Rebase or Squash and merge`  
_Compress Images_ will happen after the pull request....maybe  
### After changes are merged `Pull origin` to sync Desktop with GitHub
---
Insert Images and Tabs HowTo:
- click overview tab
- zoom to location
- click station to bring up pop up
- ADD new tab
- ![Edit Tab -> Pop-up -> Custom Configuration -> MAP POP-UP -> Saved the pop-up configuration](https://raw.githubusercontent.com/agrc/turn-gps/master/storymaps/assets/stations/_Tab_Configuration.png)
- add images (Receiver top & Antenna bottom)
- No Caption Just add text (ex. Wendover Antenna) Bold, 20, left aligned
---
Examples URLs for linking to images:
- https://raw.githubusercontent.com/agrc/turn-gps/master/storymaps/assets/stations/IDHD_Homedale-Antenna.jpg
- https://raw.githubusercontent.com/agrc/turn-gps/master/storymaps/TURNGPS-Logo.jpg
---
The _STATUS_ field in CADASTRE.TURN_GPS_STATIONS controls the visibility of stations in the storymap. _STATUS_ = O will make them visible. The acceptable _STATUS_ values are:  

O = On  
P = Proposed  
R = Removed  
