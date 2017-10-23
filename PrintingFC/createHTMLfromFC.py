from dominate import document
from dominate.tags import *
import arcpy
import pdfkit
import os

##fc = arcpy.GetParameterAsText(0)
fc=r"C:\Users\matt9014\Documents\ArcGIS\Projects\MyProject11\MyProject11.gdb/test_fc"
field_names = [f.name for f in arcpy.ListFields(fc)]
print(len(field_names))

with document(title='Features') as doc:
    with arcpy.da.SearchCursor(fc,'*') as cursor:
        for row in cursor:
            h1("Feature: " + str(row[0]))
            count=0
            while count < len(field_names):
                p(str(field_names[count]) + ": " + str(row[count]))
                count = count+1
with open('gallery.html', 'w') as f:
    f.write(doc.render())

path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
pdfkit.from_file('gallery.html', 'out.pdf', configuration=config)
os.remove('gallery.html')
