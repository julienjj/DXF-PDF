import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend

import os, re, time
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory(initialdir='c://',title="Selecione os .dxf  -   Duvidas: Julien(GEP)")
directory = os.listdir(folder_selected)
os.chdir(folder_selected)

for file in directory:
    try:
        plt.rcParams["savefig.facecolor"] = 'black'
        plt.rcParams['axes.facecolor'] = 'black'



        doc = ezdxf.readfile(file)
        msp = doc.modelspace()
        mylayer=doc.layers.new(name='MyLines', dxfattribs={'linetype': 'Continuous', 'color': 0})
        mystyle=doc.styles.new('myStandard', dxfattribs={'font' : 'Arial.ttf'})
        doc.styles.replace('Standard',mystyle)

        auditor = doc.audit()


        if len(auditor.errors) == 0:
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 1, 1])
            ctx = RenderContext(doc)

            ctx.set_current_layout(msp)
            ctx.current_layout.set_colors(bg='#FFFFFF')

            pdf=file.replace('.dxf','.pdf')
            out = MatplotlibBackend(ax)
            Frontend(ctx, out).draw_layout(msp, finalize=True)
            fig.savefig(pdf, dpi=600, facecolor = 'black', edgecolor = 'black')

    except:
        pass
