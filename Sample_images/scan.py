#Library Used to scan the files
import os
import os.path
#Library Used to change the ImageDescription
import pyexiv2 #Need to be download and install on website, runs on python2.7

for dirpath, dirnames, filenames in os.walk("."):
    #Scan through the files in all subdirectories
    
    for filename in [f for f in filenames if f.endswith(".jpg")]:#Only pick .jpg files
        folder = os.path.basename(dirpath);
        Time = filename.strip(folder);
        Date = Time[0:4]+':'+Time[4:6]+':'+Time[6:8]+' '+Time[8:10]+':'+Time[10:12]+':00';
        text = os.path.join(dirpath, filename); # Create a string combining the path and filename
        metadata = pyexiv2.ImageMetadata('%s'%text);# Load the metadata of the jpg files
        metadata.read();# Read the metadata
        key = 'Exif.Image.ImageDescription'; # Select the tag to change
        metadata[key] = pyexiv2.ExifTag(key, text); # Change the metadata
        metadata.write(); # Write in the changes
        key = 'Exif.Photo.DateTimeOriginal';
        metadata[key] = pyexiv2.ExifTag(key,Date);
        metadata.write();
    # The code needs to be put in the main directory. It will scan all photos in the same folder and
    # all files in the subdirectories .
