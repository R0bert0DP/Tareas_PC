#uis Roberto Diaz PIneda
#E11

import os
import argparse
import requests
from lxml import html
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
	
def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

 
def get_exif_metad(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
    
def GMeta():
    ruta = "Descargas"
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            #print(os.path.join(root, name))
            print ("Metadata for file: %s " %(name))
            try:
                exifData = {}
                exif = get_exif_metad(name)
                for metadata in exif:
                    file = open(str(name)+"Metadata.txt","a")
                    file.write(str(metadata) + ":" + str(exif[metadata]))
                    file.close()
                    #print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                #print ("\n")
            except:
                import sys, traceback
                traceback.print_exc(file = sys.stdout)
#printMeta()
def scrapingImages():
        url = a
        print("\nObteniendo imagenes de la url:"+ url)
    
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener imagenes
            images = parsed_body.xpath('//img/@src')

            print ('Imagenes %s encontradas' % len(images))
    
            #create directory for save images
            os.system("mkdir Descargas")
    
            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                print(download)
                # download images in images directory
                r = requests.get(download)
                f = open('Descargas/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
                
        except Exception as e:
                print(e)
                print ("Error conexion con " + url)
                print ("busque otra url")
                pass


description = "Descarga y extraccion de metadata de imagenes de internet, en la terminal escribir: python (nombrescript.py) -link (url)"

parser = argparse.ArgumentParser(description='Scrap y Metadata',

                                 epilog=description,

                                 formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-link", metavar='link', dest='link', help="link de ayuda",

                    required=True)

params = parser.parse_args()

a = (params.link)

scrapingImages()
GMeta()


