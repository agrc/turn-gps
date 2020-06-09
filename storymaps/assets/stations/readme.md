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

G:\My Drive\GPS Utah\GPS Station Photos\Richfield>`rename *.JPG *.jpg`

Copy them to `C:\_Git\turn-gps\storymaps\assets\stations`

Open new renamed images with _Windows Photos_

Rotate and Resize to Small

Run `image-fixer.py` as below

- `(.env) C:\_Git\turn-gps\src>'python image-fixer.py -d ..\storymaps -r'`
- `(.env) C:\_Git\turn-gps\src>'python image-fixer.py -d ..\storymaps\assets\stations -w UTWE_*'`
or
- `(.env) C:\_Git\turn-gps>'python src\image-fixer.py -d storymaps/test -w IDHD_*'`
