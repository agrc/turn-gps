# Station photo naming convention and processing

Photos originate from G:\My Drive\GPS Utah\GPS Station Photos.

Organize them into a folder and rename them with 4-digit code_name-Antenna and Receiver like below. We most likely will not use the `-#`.jpg images.

- `UTAI_Antelope-Island-Antenna.jpg`
- `UTAI_Antelope-Island-Antenna-2.jpg`
- `UTAI_Antelope-Island-Receiver.jpg`
- `UTAI_Antelope-Island-Receiver-2.jpg`
  - most likely don't need these
- `UTAI_Antelope-Island-Desk.jpg`
- `UTAI_Antelope-Island-Rack.jpg`
- `UTAI_Antelope-Island-etcetcetc.jpg`

Use CMD with wildcards to fix the case of the file extensions

ex. G:\My Drive\GPS Utah\GPS Station Photos\Richfield>`rename *.JPG *.jpg`

Copy them to `C:\_Git\turn-gps\storymaps\assets\stations`

Open new images with _Windows Photos_

Rotate and Resize to Small -> Save and overwrite existing

Run `image-fixer.py` on new images

- `DON'T DO THIS` C:\_Git\turn-gps\src> `.env\Scripts\activate.bat` `DO THIS Instead:`

- activate arcgispro-py3-clone

- `(arcgispro-py3-clone) C:\_Git\turn-gps\src> 'python image-fixer.py -d ..\storymaps -r'`
- `(arcgispro-py3-clone) C:\_Git\turn-gps\src> 'python image-fixer.py -d ..\storymaps\assets\stations -w UTWE_*'`
or
- `(arcgispro-py3-clone) C:\_Git\turn-gps> 'python src\image-fixer.py -d storymaps/test -w IDHD_*'`

### Commit changes to a `New Branch` and `Bring my changes over`, `commit changes` then `Publish Branch` or `Push origin` (in desktop)
### Open Pull Request in GitHub then `Rebase and merge`  
_Compress Images_ will happen after the pull request....maybe  
### After changes are merged `Pull origin` TO MASTER to sync Desktop with GitHub
Edit the layer SGID.CADASTRE.TURN_GPS_Stations and calculate 'Photos = Y' for thestations with new photos
---
Examples URLs for linking to images:
- https://raw.githubusercontent.com/agrc/turn-gps/master/storymaps/assets/stations/IDHD_Homedale-Antenna.jpg
- https://raw.githubusercontent.com/agrc/turn-gps/master/storymaps/TURNGPS-Logo.jpg
---
The _STATUS_ field in CADASTRE.TURN_GPS_STATIONS controls the visibility of stations in the storymap. _STATUS_ = O will make them visible. The acceptable _STATUS_ values are:  

O = On  
P = Proposed  
R = Removed  
