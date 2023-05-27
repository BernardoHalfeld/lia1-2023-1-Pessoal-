# AUTOGENERATED! DO NOT EDIT! File to edit: ../Example_catsVSdogs.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'examples', 'intf', 'classify_image']

## %% ../Example_catsVSdogs.ipynb 13
from fastai.vision.all import *
import gradio as gr

## %% ../Example_catsVSdogs.ipynb 15
learn = load_learner('model_catsVSdogs.pkl')

# %% ../Example_catsVSdogs.ipynb 17
categories = ('Dog', 'Cat')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

# %% ../Example_catsVSdogs.ipynb 20
image = gr.inputs.Image(shape=(192, 192))
label = gr.outputs.Label()
examples = ['dog.jpg', 'cat.jpg', 'dunno.jpg']

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)
