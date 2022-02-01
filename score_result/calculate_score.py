BLENDERSCORE=15
GIMPSCORE=15
ZIPSCORE=10
KERNELSCORE=25
MPLAYERSCORE=10
LIBREOFFICESCORE=10
FREECAD=15

print("--------------------------")
blender_score = open("/home/benchmark/Desktop/bash/results/blender.txt","r",encoding="utf-8")
blender_score = float(blender_score.read())
print("BLENDER =  " +str(blender_score))
print("--------------------------")
gimp_score = open("/home/benchmark/Desktop/bash/results/gimp.txt","r",encoding="utf-8")
gimp_score = float(gimp_score.read())
print("GIMP = " +str(gimp_score))
print("--------------------------")
zip_score = open("/home/benchmark/Desktop/bash/results/zip.txt","r",encoding="utf-8")
zip_score = float(zip_score.read())
print("ZIPFOLDER = " +str(zip_score))
print("--------------------------")
kernel_score = open("/home/benchmark/Desktop/bash/results/kernel.txt","r",encoding="utf-8")
kernel_score = float(kernel_score.read())
print("KERNELCOMPILE = " +str(kernel_score))
print("--------------------------")
mplayer_score = open("/home/benchmark/Desktop/bash/results/mplayer.txt","r",encoding="utf-8")
mplayer_score = mplayer_score.readlines()
mplayer_score = mplayer_score[-4:]
mplayer_score = float(mplayer_score[0].split()[10][0:-1])
print("MPLAYER = " +str(mplayer_score))
print("--------------------------")
freecad_score = open("/home/benchmark/Desktop/bash/results/freecad.txt","r",encoding="utf-8")
freecad_score = float(freecad_score.read())
print("FREECAD = " +str(freecad_score))
print("--------------------------")
libreoffice_score = open("/home/benchmark/Desktop/bash/results/libreoffice.txt","r",encoding="utf-8")
libreoffice_score = float(libreoffice_score.read())
print("LIBREOFFICE = " +str(libreoffice_score))
print("--------------------------")
resultBlender = 15*blender_score%100
resultGimp = 15*gimp_score%100
resultZip = 10*zip_score%100
resultKernel = 25*kernel_score%100
resultMplayer = 10*mplayer_score%100
resultLibreoffice = 10*libreoffice_score%100
resultFreecad = 15*freecad_score%100

result = resultBlender + resultGimp + resultZip + resultKernel + resultMplayer + resultLibreoffice + resultFreecad
print("RESULT : " + str(result))

print("--------------------------")