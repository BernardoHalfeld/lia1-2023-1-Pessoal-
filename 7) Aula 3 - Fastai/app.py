# AUTOGENERATED! DO NOT EDIT! File to edit: . (unless otherwise specified).

import pathlib
pathlib.WindowsPath = pathlib.PosixPath

__all__ = ['learn', 'classify_image', 'categories', 'image', 'label', 'examples', 'intf']

# Cell
from fastai.vision.all import *
import gradio as gr
import timm

# Cell
learn = load_learner('model.pkl')

# Cell
categories = learn.dls.vocab

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

# Cell
image = gr.inputs.Image(shape=(192, 192))
label = gr.outputs.Label()
examples = ['pug.jpg']

# Cell
intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch()