import sys, os
from PIL import Image

def main():
    mode = ''
    infile = ''
    if(len(sys.argv) == 1 or len(sys.argv) == 2):
        print("Usage: convert (inputfile) (type)")
        print("Usage: resize (inputfile) (width) (height) (app/repl)")
        sys.exit()
    if(str(sys.argv[1]) == "convert"):
        mode = 'convert'
    if(str(sys.argv[1]) == "resize"):
        mode = 'resize'
    
    if(mode == ''):
        print("Unknown mode")
        sys.exit()

    infile = sys.argv[2]

    if(mode == 'convert'):
        if(len(sys.argv) != 4):
            print("Usage: convert (inputfile) (type)")
            sys.exit()
        f, e = os.path.splitext(infile)
        try:
            im = Image.open(infile).save(f+"."+sys.argv[3], sys.argv[3].upper())
        except IOError:
            print("invalid filename ", infile)
            sys.exit()
    if(mode == 'resize'):
        if(len(sys.argv) != 6):
            print("Usage: resize (inputfile) (width) (height) (app/repl)")
            sys.exit()
        f, e = os.path.splitext(infile)
        try:
            im = Image.open(infile)
            im = im.resize((int(sys.argv[3]),int(sys.argv[4])))
            if(sys.argv[5] == 'app'):
                im.save("tmpimg." + e)
                os.rename("tmpimg." + e, infile+".resized")
                sys.exit()
            if(sys.argv[5] == 'repl'):
                im.save(infile)
                sys.exit()
        except IOError:
            print("invalid filename ", infile)
            sys.exit()
main()
