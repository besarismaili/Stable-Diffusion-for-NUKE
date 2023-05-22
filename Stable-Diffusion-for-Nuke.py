import nuke
import os

Stability_group = nuke.createNode("Group", inpanel=False)
Stability_group.setName("Stability")
Stability_group.knob("tile_color").setValue(0xf794ff00)

def ui():
    n = Stability_group 

    # Get the directory of the current Nuke script
    script_dir = str(os.path.dirname(nuke.root().name()))
    sub_dir = "Stability"
    # Set the directories where the image files and temp files will be stored
    image_dir = os.path.join(os.sep, script_dir, sub_dir, "Images")
    temp_dir = os.path.join(os.sep, script_dir, sub_dir, "temp")
    # Create the directories if they don't exist
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)
    # Get the list of existing image files in the directory
    os.listdir(image_dir)

    with Stability_group:

        Img_input = nuke.nodes.Input(name="Image")
        reformat_img = nuke.nodes.Reformat(format='square_512',resize='fill')
        reformat_img.setInput(0, Img_input)
        write_init_image = nuke.nodes.Write(name="write_init_image")
        img_filename = "int2img_.png"
        write_init_image_path = f"{temp_dir}/{img_filename}"
        write_init_image['file'].fromUserText(write_init_image_path)
        write_init_image.setInput(0, reformat_img)

        mask_input = nuke.nodes.Input(name="Mask")
        shuffle = nuke.nodes.Shuffle2(name="mask_input_shuffle")
        shuffle.setInput(0, mask_input)
        shuffle["mappings"].setValue([('rgba.alpha', 'rgba.red'), ('rgba.alpha', 'rgba.green'), ('rgba.alpha', 'rgba.blue'), ('rgba.alpha', 'rgba.alpha')])

        reformat_mask = nuke.nodes.Reformat(format='square_512',resize='fill')
        reformat_mask.setInput(0, shuffle)
        write_mask_image = nuke.nodes.Write(name="write_mask_image")
        mask_filename = "mask_img_.png"
        write_mask_image_path = f"{temp_dir}/{mask_filename}"
        write_mask_image['file'].fromUserText(write_mask_image_path)
        write_mask_image.setInput(0, reformat_mask)

        write_upscale_image = nuke.nodes.Write(name="write_upscale_image")
        upscale_filename = "upscale_img_.png"
        write_upscale_image_path = f"{temp_dir}/{upscale_filename}"
        write_upscale_image['file'].fromUserText(write_upscale_image_path)
        write_upscale_image.setInput(0, reformat_img)

        init_write_mask_image = nuke.nodes.Write(name="write_init_mask_image")
        init_mask_filename = "init_mask_img_.png"
        init_write_mask_image_path = f"{temp_dir}/{init_mask_filename}"
        init_write_mask_image['file'].fromUserText(init_write_mask_image_path)
        init_write_mask_image.setInput(0, reformat_img)

        output = nuke.nodes.Output()
        merge = nuke.nodes.Merge(mix='0.5')
        merge.setInput(0, reformat_img)
        merge.setInput(1, reformat_mask)
        output.setInput(0, merge)

    SD = '<p  style="color:#f794ff;font-weight:bold;font-size:24px;">Stable<span style="color:#504eaa;"> Diffusion</span> <span style="color:#cccccc;font-size:12px;;font-weight:regular"> for Nuke</span></p>'
    n.addKnob(nuke.Tab_Knob("img", "Still Image"))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Text_Knob("sda", " ",SD))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.BeginTabGroup_Knob())
    n.addKnob(nuke.Tab_Knob("text-to-image","Text to image"))
    n.addKnob(nuke.Text_Knob(""))
    ti_eng_knob = nuke.Enumeration_Knob("ti_engine_name", "Engine", ['stable-diffusion-v1', 'stable-diffusion-v1-5','stable-diffusion-512-v2-0','stable-diffusion-768-v2-0', 'stable-diffusion-512-v2-1','stable-diffusion-768-v2-1','stable-diffusion-xl-beta-v2-2-2'])
    ti_eng_knob.setValue('stable-diffusion-xl-beta-v2-2-2')
    n.addKnob(ti_eng_knob) 
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("ti_prompt", "Prompt", "a unicorn in socotra island, pink and white elegant"))
    n.addKnob(nuke.Double_Knob("ti_weight","Prompt Weight"))
    n["ti_weight"].setValue(0.5)
    n["ti_weight"].setRange(0,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Double_Knob("ti_cfg_scale","Cfg Scale"))
    n["ti_cfg_scale"].setValue(7)
    n["ti_cfg_scale"].setRange(1,10)
    n.addKnob(nuke.Enumeration_Knob("ti_style_preset","Style Preset", [(""),("3d-model"), ("analog-film"),("anime"),("cinematic"),("comic-book"),("digital-art"),("enhance"),("fantasy-art"),("isometric"),("line-art"),("low-poly"),("modeling-compound"),("neon-punk"),("origami"),("photographic"),("pixel-art"),("tile-texture")]))
    n.addKnob(nuke.Enumeration_Knob("ti_clip_guidance_preset","Clip Guidance Preset", [("NONE"), ("FAST_BLUE"), ("FAST_GREEN"), ("SIMPLE"),("SLOW"),("SLOWER"),("SLOWEST")]))
    n.addKnob(nuke.Enumeration_Knob("ti_sampler","Sampler", [("DDIM"), ("DDPM"),("K_DPMPP_2M"), ("K_DPMPP_2S_ANCESTRAL"), ("K_EULER"),("K_EULER_ANCESTRAL"),("K_HEUN"), ("K_LMS")]))
    n.addKnob(nuke.Int_Knob("ti_samples","Samples"))
    n["ti_samples"].setValue(1)
    n["ti_samples"].setRange(1,10)
    n.addKnob(nuke.Int_Knob("ti_seed","Seed"))
    n["ti_seed"].setValue(0)
    n["ti_seed"].setRange(1,4294967295)
    n.addKnob(nuke.Int_Knob("ti_steps","Steps"))
    n["ti_steps"].setValue(30)
    n["ti_steps"].setRange(10,150)
    
    get_text_to_image_response = """
import base64
import os
import requests

engine_id = "stable-diffusion-v1-5"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = os.getenv("STABILITY_API_KEY")

# Get the directory of the current Nuke script
script_dir = os.path.dirname(nuke.root().name())

# Set the subdirectory where the image files will be stored
sub_dir = "Stability"

# Set the directories where the image files and temp files will be stored
image_dir = os.path.join(script_dir, sub_dir, "Images")
temp_dir = os.path.join(script_dir, sub_dir, "temp")

# Create the directories if they don't exist
os.makedirs(image_dir, exist_ok=True)
os.makedirs(temp_dir, exist_ok=True)

# Get the list of existing image files in the directory
existing_files = os.listdir(image_dir)

engine_txt_img=nuke.thisNode().knob('ti_engine_name').value()
prompt_txt_img=nuke.thisNode().knob('ti_prompt').value()
cfg_scale_txt_img=int(nuke.thisNode().knob('ti_cfg_scale').getValue())
clip_guidance_preset_txt_img=nuke.thisNode().knob('ti_clip_guidance_preset').value()
style_preset_txt_img=nuke.thisNode().knob('ti_style_preset').value()
samples_txt_img=int(nuke.thisNode().knob('ti_samples').getValue())
steps_txt_img=int(nuke.thisNode().knob('ti_steps').getValue())
weight_txt_img=nuke.thisNode().knob('ti_weight').getValue()
api_key = nuke.thisNode().knob('api-key').value()

json_data = {
    "text_prompts": [
        {
            "text": prompt_txt_img,
        }
    ],
    "weight": weight_txt_img,
    "cfg_scale": cfg_scale_txt_img,
    "clip_guidance_preset": clip_guidance_preset_txt_img,
    "height": 512,
    "width": 512,
    "samples": samples_txt_img,
    "steps": steps_txt_img,
}

if style_preset_txt_img:
    json_data["style_preset"] = style_preset_txt_img

response = requests.post(
    f"{api_host}/v1/generation/{engine_txt_img}/text-to-image",
    headers={
        "Content-Type": 'application/json',
        "Accept": 'application/json',
        "Authorization": f'Bearer {api_key}'
    },
    json = json_data
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

for i, image in enumerate(data["artifacts"]):
    # Construct the initial filename
    file_name = f"Text_To_Image_{i}.png"
    input_path = os.path.join(image_dir, file_name)
    
    # Check if the filename already exists
    version = 1
    while os.path.exists(input_path):
        # If the file already exists, version up the filename
        version += 1
        file_name = f"Text_To_Image_{i}_v{version}.png"
        input_path = os.path.join(image_dir, file_name)
    
    # Write the image data to the new file
    with open(input_path, "wb") as f:
        f.write(base64.b64decode(image["base64"]))
    
    # Create a Read node for the new file
    with nuke.root():
        read_node = nuke.createNode("Read", inpanel=False)
        read_node['file'].fromUserText(input_path)"""

    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.PyScript_Knob("t2i_dream", "Dream", get_text_to_image_response))
    n["t2i_dream"].setFlag(0x0000000000001000)
        
    #IMAGE TO IMAGE TAB
    
    n.addKnob(nuke.Tab_Knob("image-to-image","Image to image"))
    n.addKnob(nuke.Text_Knob(""))
    ii_eng_knob = nuke.Enumeration_Knob("ii_engine_name", "Model", ['stable-diffusion-v1', 'stable-diffusion-v1-5','stable-diffusion-512-v2-0','stable-diffusion-768-v2-0', 'stable-diffusion-512-v2-1','stable-diffusion-768-v2-1','stable-diffusion-xl-beta-v2-2-2'])
    ii_eng_knob.setValue('stable-diffusion-xl-beta-v2-2-2')
    ii_eng_knob.clearFlag(nuke.STARTLINE) 
    n.addKnob(ii_eng_knob)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("ii_prompt1", "Prompt", "Dark nightmare unicorn, dreamy and ethereal, expressive pose, big pink eyes, exciting expression, fantasy, intricate, elegant"))
    promp2w = n.addKnob(nuke.Double_Knob("ii_weight1","Prompt Weight"))
    n["ii_weight1"].setValue(0.5)
    n["ii_weight1"].setRange(-1,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("ii_prompt2", "Second Prompt", "pink, unicorn, rainbow"))
    n.addKnob(nuke.Double_Knob("ii_weight2","Second Prompt Weight"))
    n["ii_weight2"].setValue(-0.9)
    n["ii_weight2"].setRange(-1,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Double_Knob("image_strength","Image Strength"))
    n["image_strength"].setValue(0.35)
    n["image_strength"].setRange(0.0,1.0)
    n.addKnob(nuke.Enumeration_Knob("ii_init_image_mode","Init Image Mode", [("IMAGE_STRENGTH"), ("STEP_SCHEDULE.")]))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Double_Knob("ii_cfg_scale","Cfg Scale"))
    n["ii_cfg_scale"].setValue(7)
    n["ii_cfg_scale"].setRange(1,10)
    n.addKnob(nuke.Enumeration_Knob("ii_style_preset","Style Preset", [(""),("3d-model"), ("analog-film"),("anime"),("cinematic"),("comic-book"),("digital-art"),("enhance"),("fantasy-art"),("isometric"),("line-art"),("low-poly"),("modeling-compound"),("neon-punk"),("origami"),("photographic"),("pixel-art"),("tile-texture")]))
    n.addKnob(nuke.Enumeration_Knob("ii_clip_guidance_preset","Clip Guidance Preset", [("NONE"), ("FAST_BLUE"), ("FAST_GREEN"), ("SIMPLE"),("SLOW"),("SLOWER"),("SLOWEST")]))
    n.addKnob(nuke.Enumeration_Knob("ii_sampler","Sampler", [("DDIM"), ("DDPM"),("K_DPMPP_2M"), ("K_DPMPP_2S_ANCESTRAL"), ("K_EULER"),("K_EULER_ANCESTRAL"),("K_HEUN"), ("K_LMS")]))
    n.addKnob(nuke.Int_Knob("ii_samples","Samples"))
    n["ii_samples"].setTooltip("Number of images to generate")
    n["ii_samples"].setValue(1)
    n["ii_samples"].setRange(1,10)
    n.addKnob(nuke.Int_Knob("ii_seed","Seed"))
    n["ii_samples"].setTooltip("Random noise seed (omit this option or use 0 for a random seed)")
    n["ii_seed"].setValue(0)
    n["ii_seed"].setRange(1,4294967295)
    n.addKnob(nuke.Int_Knob("ii_steps","Steps"))
    n["ii_samples"].setTooltip("Number of diffusion steps to run")
    n["ii_steps"].setValue(30)
    n["ii_steps"].setRange(10,150)

    get_image_to_image_response = """
import base64
import os
import requests

engine_id = "stable-diffusion-v1-5"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = os.getenv("STABILITY_API_KEY")

# Get the directory of the current Nuke script
script_dir = os.path.dirname(nuke.root().name())
# Set the subdirectory where the image files will be stored
sub_dir = "Stability"
# Set the directories where the image files and temp files will be stored
image_dir = os.path.join(script_dir, sub_dir, "Images")
temp_dir = os.path.join(script_dir, sub_dir, "temp")
# Create the directories if they don't exist
os.makedirs(image_dir, exist_ok=True)
os.makedirs(temp_dir, exist_ok=True)
# Get the list of existing image files in the directory
existing_files = os.listdir(image_dir)

nuke.execute(nuke.toNode('write_init_image'), start=1, end=1)

img_engine = nuke.thisNode().knob('ii_engine_name').value()
prompt1_img_img=str(nuke.thisNode().knob('ii_prompt1').value())
weight1_img_img=nuke.thisNode().knob('ii_weight1').value()
prompt2_img_img=str(nuke.thisNode().knob('ii_prompt2').value())
weight2_img_img=nuke.thisNode().knob('ii_weight2').value()
cfg_scale_img_img=int(nuke.thisNode().knob('ii_cfg_scale').value())
clip_guidance_preset_img_img=nuke.thisNode().knob('ii_clip_guidance_preset').value()
style_preset_img_img=nuke.thisNode().knob('ii_style_preset').value()
samples_img_img=int(nuke.thisNode().knob('ii_samples').value())
steps_img_img=int(nuke.thisNode().knob('ii_steps').value())
weight_img_img=nuke.thisNode().knob('image_strength').getValue()
api_key = nuke.thisNode().knob('api-key').value()

with nuke.thisNode():
    write_init_image_path = nuke.toNode('write_init_image')['file'].value()

json_data = {
    "text_prompts[0][text]": prompt1_img_img,
    "text_prompts[0][weight]": weight1_img_img,
    "text_prompts[1][text]": prompt2_img_img,
    "text_prompts[1][weight]": weight2_img_img,
    "image_strength": weight_img_img,
    "init_image_mode": "IMAGE_STRENGTH",
    "cfg_scale": cfg_scale_img_img,
    "clip_guidance_preset": clip_guidance_preset_img_img,
    "samples": samples_img_img,
    "steps": steps_img_img,
}

if style_preset_img_img:
    json_data["style_preset"] = style_preset_img_img

response = requests.post(
    f"{api_host}/v1/generation/{img_engine}/image-to-image",
    headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    files={
        "init_image": open(write_init_image_path, "rb")
    },
    data = json_data
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

for i, image in enumerate(data["artifacts"]):
    # Construct the initial filename
    file_name = f"Image_To_Image_{i}.png"
    input_path = os.path.join(image_dir, file_name)
    
    # Check if the filename already exists
    version = 1
    while os.path.exists(input_path):
        # If the file already exists, version up the filename
        version += 1
        file_name = f"Image_To_Image_{i}_v{version}.png"
        input_path = os.path.join(image_dir, file_name)
    
    # Write the image data to the new file
    with open(input_path, "wb") as f:
        f.write(base64.b64decode(image["base64"]))
    
    # Create a Read node for the new file
    with nuke.root():
        read_node = nuke.createNode("Read", inpanel=False)
        read_node['file'].fromUserText(input_path)"""
    
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.PyScript_Knob("i2i_dream", "Dream", get_image_to_image_response))
    n["i2i_dream"].setFlag(0x0000000000001000)
        
    #IMAGE TO IMAGE/UPSCALE TAB

    n.addKnob(nuke.Tab_Knob("upscale-tab","Upscale"))
    n.addKnob(nuke.Text_Knob(""))
    iiu_eng_knob = nuke.Enumeration_Knob("ui_engine_name", "Model", ['esrgan-v1-x2plus','stable-diffusion-x4-latent-upscaler'])
    n.addKnob(iiu_eng_knob)
    n.addKnob(nuke.Enumeration_Knob("upscale","Upscale size", [("1024x1024"), ("2048x2048")]))
    n["upscale"].setValue("1024x1024")
    iiu_eng_knob.clearFlag(nuke.STARTLINE) 

    get_image_to_image_upscale_response = """
import os
import requests

engine_id = "esrgan-v1-x2plus"
api_host = os.getenv("API_HOST", "https://api.stability.ai")
api_key = os.getenv("STABILITY_API_KEY")

# Get the directory of the current Nuke script
script_dir = os.path.dirname(nuke.root().name())

# Set the subdirectory where the image files will be stored
sub_dir = "Stability"

# Set the directories where the image files and temp files will be stored
image_dir = os.path.join(script_dir, sub_dir, "Images")
temp_dir = os.path.join(script_dir, sub_dir, "temp")

# Create the directories if they don't exist
os.makedirs(image_dir, exist_ok=True)
os.makedirs(temp_dir, exist_ok=True)

# Get the list of existing image files in the directory
existing_files = os.listdir(image_dir)

nuke.execute(nuke.toNode('write_upscale_image'), start=1, end=1)

upscale_engine = nuke.thisNode().knob('ui_engine_name').value()
api_key = nuke.thisNode().knob('api-key').value()
# Get the selected option from the Enumeration_Knob
selected_option = nuke.thisNode().knob('upscale').value()
# Set the integer variable based on the selected option
if selected_option == "1024x1024":
    upscale_value = 1024
elif selected_option == "2048x2048":
    upscale_value = 2048

with nuke.thisNode():
    write_upscale_image_path = nuke.toNode('write_upscale_image')['file'].value()

response = requests.post(
    f"{api_host}/v1/generation/{upscale_engine}/image-to-image/upscale",
    headers={
        "Accept": "image/png",
        "Authorization": f"Bearer {api_key}"
    },
    files={
        "image": open(write_upscale_image_path, "rb")
    },
    data={
        "width": upscale_value,
    }
)

data = response.content

# Construct the initial filename
input_path = os.path.join(image_dir, f"Image_upscaled_.png")

# Check if the filename already exists
version = 1
while os.path.exists(input_path):
    # If the file already exists, version up the filename
    version += 1
    file_name = f"Image_upscaled_{upscale_value}_v{version}.png"
    input_path = os.path.join(image_dir, file_name)

# Write the image data to the new file
with open(input_path, "wb") as f:
    f.write(response.content)

# Create a Read node for the new file
with nuke.root():
    read_node = nuke.createNode("Read", inpanel=False)
read_node['file'].fromUserText(input_path)"""

    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.PyScript_Knob("i2i_u_dream", "Dream", get_image_to_image_upscale_response))
    n["i2i_u_dream"].setFlag(0x0000000000001000)
    
    #IMAGE TO IMAGE/MASKING TAB

    n.addKnob(nuke.Tab_Knob("inpainting","Inpainting"))
    n.addKnob(nuke.Text_Knob(""))
    iim_eng_knob = nuke.Enumeration_Knob("iim_engine_name", "Model", ['stable-inpainting-v1-0','stable-inpainting-512-v2-0'])
    iim_eng_knob.setValue("stable-inpainting-512-v2-0")
    n.addKnob(iim_eng_knob) 
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("iim_prompt1", "Prompt", "a pink unicorn with a cat riding it with a lot of rainbow"))
    n.addKnob(nuke.Double_Knob("iim_weight1","Prompt Weight"))
    n["iim_weight1"].setValue(0.5)
    n["iim_weight1"].setRange(-1,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("iim_prompt2", "Second Prompt", "a pink unicorn with a cat riding it with a lot of rainbow"))
    n.addKnob(nuke.Double_Knob("iim_weight2","Second Prompt Weight"))
    n["iim_weight2"].setValue(-0.9)
    n["iim_weight2"].setRange(-1,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Double_Knob("iim_cfg_scale","Cfg Scale"))
    n["iim_cfg_scale"].setValue(7)
    n["iim_cfg_scale"].setRange(1,10)
    n.addKnob(nuke.Enumeration_Knob("iim_style_preset","Style Preset", [(""),("3d-model"), ("analog-film"),("anime"),("cinematic"),("comic-book"),("digital-art"),("enhance"),("fantasy-art"),("isometric"),("line-art"),("low-poly"),("modeling-compound"),("neon-punk"),("origami"),("photographic"),("pixel-art"),("tile-texture")]))
    n.addKnob(nuke.Enumeration_Knob("iim_clip_guidance_preset","Clip Guidance Preset", [("NONE"), ("FAST_BLUE"), ("FAST_GREEN"), ("SIMPLE"),("SLOW"),("SLOWER"),("SLOWEST")]))
    n.addKnob(nuke.Enumeration_Knob("iim_sampler","Sampler", [("DDIM"), ("DDPM"),("K_DPMPP_2M"), ("K_DPMPP_2S_ANCESTRAL"), ("K_EULER"),("K_EULER_ANCESTRAL"),("K_HEUN"), ("K_LMS")]))
    n.addKnob(nuke.Int_Knob("iim_samples","Samples"))
    n["iim_samples"].setValue(1)
    n["iim_samples"].setRange(1,10)
    n.addKnob(nuke.Int_Knob("iim_seed","Seed"))
    n["iim_seed"].setValue(0)
    n["iim_seed"].setRange(1,4294967295)
    n.addKnob(nuke.Int_Knob("iim_steps","Steps"))
    n["iim_steps"].setValue(30)
    n["iim_steps"].setRange(10,150)
    n["iim_steps"].setFlag(0x0000000000002000) 

    get_image_to_image_masking_response = """
import base64
import os
import requests

engine_id = "stable-inpainting-512-v2-0"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = os.getenv("STABILITY_API_KEY")

# Get the directory of the current Nuke script
script_dir = os.path.dirname(nuke.root().name())

# Set the subdirectory where the image files will be stored
sub_dir = "Stability"

# Set the directories where the image files and temp files will be stored
image_dir = os.path.join(script_dir, sub_dir, "Images")
temp_dir = os.path.join(script_dir, sub_dir, "temp")

# Create the directories if they don't exist
os.makedirs(image_dir, exist_ok=True)
os.makedirs(temp_dir, exist_ok=True)

# Get the list of existing image files in the directory
existing_files = os.listdir(image_dir)

api_key = nuke.thisNode().knob('api-key').value()

nuke.execute(nuke.toNode('write_init_mask_image'), start=1, end=1)
nuke.execute(nuke.toNode('write_mask_image'), start=1, end=1)

inpaint_engine = nuke.thisNode().knob('iim_engine_name').value()
prompt1_img_msk=nuke.thisNode().knob('iim_prompt1').getValue()
prompt2_img_msk=nuke.thisNode().knob('iim_prompt1').getValue()
cfg_scale_img_msk=int(nuke.thisNode().knob('iim_cfg_scale').getValue())
clip_guidance_preset_img_msk=nuke.thisNode().knob('iim_clip_guidance_preset').value()
style_preset_img_msk=nuke.thisNode().knob('iim_style_preset').value()
samples_img_msk=int(nuke.thisNode().knob('iim_samples').getValue())
steps_img_msk=int(nuke.thisNode().knob('iim_steps').getValue())
weight1_img_msk=nuke.thisNode().knob('iim_weight1').getValue()
weight2_img_msk=nuke.thisNode().knob('iim_weight2').getValue()

with nuke.thisNode():
    init_write_mask_image_path = nuke.toNode('write_init_mask_image')['file'].value()
    write_mask_image_path = nuke.toNode('write_mask_image')['file'].value()

json_data = {
    "mask_source": "MASK_IMAGE_WHITE",
    "text_prompts[0][text]": prompt1_img_msk,
    "text_prompts[0][weight]": weight1_img_msk,
    "text_prompts[1][text]": prompt2_img_msk,
    "text_prompts[1][weight]": weight2_img_msk,
    "cfg_scale": cfg_scale_img_msk,
    "clip_guidance_preset": clip_guidance_preset_img_msk,
    "samples": samples_img_msk,
    "steps": steps_img_msk,
}
    
if style_preset_img_msk:
    json_data["style_preset"] = style_preset_img_msk

response = requests.post(
    f"{api_host}/v1/generation/{inpaint_engine}/image-to-image/masking",
    headers={
        "Accept": 'application/json',
        "Authorization": f"Bearer {api_key}"
    },
    files={
        'init_image': open(init_write_mask_image_path, 'rb'),
        'mask_image': open(write_mask_image_path, 'rb'),
    },
    data = json_data
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

for i, image in enumerate(data["artifacts"]):
    # Construct the initial filename
    file_name = f"Inpaint_Image_{i}.png"
    input_path = os.path.join(image_dir, file_name)
        
    # Check if the filename already exists
    version = 1
    while os.path.exists(input_path):
        # If the file already exists, version up the filename
        version += 1
        file_name = f"Inpaint_Image_{i}_v{version}.png"
        input_path = os.path.join(image_dir, file_name)
    
    # Write the image data to the new file
    with open(input_path, "wb") as f:
        f.write(base64.b64decode(image["base64"]))
    
    # Create a Read node for the new file
    with nuke.root():
        read_node = nuke.createNode("Read", inpanel=False)
        read_node['file'].fromUserText(input_path)"""

    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.PyScript_Knob("i2i_m_dream", "Dream", get_image_to_image_masking_response))
    n["i2i_m_dream"].setFlag(0x0000000000001000)
    n.addKnob(nuke.EndTabGroup_Knob())

    #ANIMATION TAB
    """
    n.addKnob(nuke.Tab_Knob("anim_tab", "Animation"))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Text_Knob("sda", " ",SD))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.BeginTabGroup_Knob())
    n.addKnob(nuke.Tab_Knob('promts', 'Prompts'))
    n.addKnob(nuke.Enumeration_Knob("anim_engine_name", "Model", ['stable-diffusion-v1', 'stable-diffusion-v1-5','stable-diffusion-512-v2-0','stable-diffusion-768-v2-0', 'stable-diffusion-512-v2-1','stable-diffusion-768-v2-1','stable-diffusion-xl-beta-v2-2-2']))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob('animation_prompts', 'Animation Prompts'))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob('negative_prompt', 'Negative Prompts', 'blurry, low resolution'))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.PyScript_Knob("i2i_m_dream", "Dream", get_image_to_image_masking_response))
    n.addKnob(nuke.Tab_Knob('config', 'Config'))
    n.addKnob(nuke.Int_Knob('max_frames', 'Max Frames'))
    n['max_frames'].setValue(72)
    n.addKnob(nuke.WH_Knob('hw', 'Height and Width'))
    n['hw'].setValue(512)
    n.addKnob(nuke.Int_Knob('steps_curve', 'Steps Curve'))
    n['steps_curve'].setValue(30)

    n.addKnob(nuke.Enumeration_Knob("anim_style_preset","Style Preset", [(""),("3d-model"), ("analog-film"),("anime"),("cinematic"),("comic-book"),("digital-art"),("enhance"),("fantasy-art"),("isometric"),("line-art"),("low-poly"),("modeling-compound"),("neon-punk"),("origami"),("photographic"),("pixel-art"),("tile-texture")]))
    n.addKnob(nuke.String_Knob('sampler', 'Sampler', 'k_dpmpp_2m'))
    n.addKnob(nuke.Int_Knob('seed', 'Seed', -1))
    n.addKnob(nuke.Int_Knob('cfg_scale', 'Guidance Scale', 7))
    n.addKnob(nuke.String_Knob('clip_guidance', 'CLIP Guidance'))
    n.addKnob(nuke.Boolean_Knob('steps_strength_adj', 'Steps Strength Adj', True))
    n.addKnob(nuke.Boolean_Knob('interpolate_prompts', 'Interpolate Prompts', False))
    n.addKnob(nuke.Boolean_Knob('locked_seed', 'Locked Seed', False))
    n.addKnob(nuke.Tab_Knob('noise_curve', 'Noise and Curve', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Double_Knob('noise_add_curve', 'Noise Add Curve'))
    n['noise_add_curve'].setValue([0.02])
    n.addKnob(nuke.Double_Knob('noise_scale_curve', 'Noise Scale Curve'))
    n['noise_scale_curve'].setValue([0.99])
    n.addKnob(nuke.Double_Knob('strength_curve', 'Previous Frame Strength Curve'))
    n['strength_curve'].setValue([0.65])
    n.addKnob(nuke.Int_Knob('diffusion_cadence_curve', 'Cadence', 1))
    n.addKnob(nuke.String_Knob('cadence_interp', 'Cadence Interp', 'mix'))
    n.addKnob(nuke.Boolean_Knob('cadence_spans', 'Cadence Spans', False))
    n.addKnob(nuke.Boolean_Knob('inpaint_border', 'Inpaint Border', False))
    n.addKnob(nuke.String_Knob('border', 'Border', 'Replicate'))
    
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))
    n.addKnob(nuke.Tab_Knob('Coherence', 'Coherence', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Int_Knob('fps', 'FPS', 12))

    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))
    n.addKnob(nuke.Tab_Knob('color', 'Color', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.String_Knob('color_coherence', 'Colour Coherence', 'LAB'))
    n.addKnob(nuke.Double_Knob('brightness_curve', 'Brightness Curve'))
    n['brightness_curve'].setValue([1.0])
    n.addKnob(nuke.Double_Knob('contrast_curve', 'Contrast Curve'))
    n['contrast_curve'].setValue([1.0])
    n.addKnob(nuke.Double_Knob('hue_curve', 'Hue Curve'))
    n['hue_curve'].setValue([0.0])
    n.addKnob(nuke.Double_Knob('saturation_curve', 'Saturation Curve'))
    n['saturation_curve'].setValue([1.0])
    n.addKnob(nuke.Double_Knob('lightness_curve', 'Lightness Curve'))
    n['lightness_curve'].setValue([0.0])
    n.addKnob(nuke.Boolean_Knob('color_match_animate', 'Animate Colour Match', True))
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))
    n.addKnob(nuke.Tab_Knob('depth', 'Depth', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Double_Knob('depth_model_weight', 'Depth Model Weight'))
    n['depth_model_weight'].setValue([0.3])
    n.addKnob(nuke.Double_Knob('fov_curve', 'Fov Curve'))
    n['fov_curve'].setValue([25.0])
    n.addKnob(nuke.Double_Knob('depth_blur_curve', 'Depth Blur Curve'))
    n['depth_blur_curve'].setValue([0.0])
    n.addKnob(nuke.Double_Knob('depth_warp_curve', 'Depth Warp Curve'))
    n['depth_warp_curve'].setValue([1.0])
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))
    n.addKnob(nuke.Tab_Knob('3drender', '3D Render', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.String_Knob('camera_type', 'Camera Type', 'Perspective'))
    n.addKnob(nuke.String_Knob('render_mode', 'Render Mode', 'Mesh'))
    n.addKnob(nuke.Double_Knob('mask_power', 'Mask Power'))
    n['mask_power'].setValue(0.3)
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))
    n.addKnob(nuke.Tab_Knob('inpainting', 'Inpainting', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Boolean_Knob('use_inpainting_model', 'Use Inpainting Model', False))
    n.addKnob(nuke.Double_Knob('mask_min_value', 'Mask Min Value'))
    n['mask_min_value'].setValue(0.25)
    n.addKnob(nuke.Double_Knob('mask_binarization_thr', 'Mask Binarization THR'))
    n['mask_binarization_thr'].setValue(0.5)
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))
    n.addKnob(nuke.Tab_Knob('input', 'Input'))
    n.addKnob(nuke.Tab_Knob('camera', 'Camera'))
    n.addKnob(nuke.Text_Knob('2d-camera', '2D Camera'))
    n.addKnob(nuke.Double_Knob('angle', 'Angle'))
    n['angle'].setValue(0)
    n.addKnob(nuke.Double_Knob('zoom', 'Zoom'))
    n['zoom'].setValue(1)
    n.addKnob(nuke.Text_Knob('2D-3D-camera-translation', '2D and 3D Camera translation'))
    n.addKnob(nuke.Int_Knob('translation_x', 'Translation X'))
    n.addKnob(nuke.Int_Knob('translation_y', 'Translation Y'))
    n.addKnob(nuke.Int_Knob('translation_z', 'Translation Z'))
    n.addKnob(nuke.Text_Knob('3D-camera-rotation', '3D Camera rotation'))
    n.addKnob(nuke.Double_Knob('rotation_x', 'Rotation X'))
    n.addKnob(nuke.Double_Knob('rotation_y', 'Rotation Y'))
    n.addKnob(nuke.Double_Knob('rotation_z', 'Rotation Z'))

    n.addKnob(nuke.Tab_Knob('post-process', 'Post-process'))
    n.addKnob(nuke.File_Knob('init_image', 'Init Image'))
    n.addKnob(nuke.String_Knob('init_sizing', 'Init Sizing', 'Stretch'))
    n.addKnob(nuke.File_Knob('mask_path', 'Mask Path'))
    n.addKnob(nuke.Boolean_Knob('mask_invert', 'Mask Invert', False))
    n.addKnob(nuke.File_Knob('video_init_path', 'Video Init Path'))
    n.addKnob(nuke.Double_Knob('video_mix_in_curve', 'Mix-in Curve'))
    n['video_mix_in_curve'].setValue([0.02])
    n.addKnob(nuke.Boolean_Knob('video_flow_warp', 'Flow Warp', True))
    n.addKnob(nuke.Int_Knob('extract_nth_frame', 'Extract Nth Frame', 1))
    n.addKnob(nuke.Int_Knob('fps', 'FPS', 24))
    n.addKnob(nuke.String_Knob('frame_interpolation_mode', 'Frame Interpolation Mode'))
    n.addKnob(nuke.Int_Knob('frame_interpolation_factor', 'Frame Interpolation Factor', 2))
    n.addKnob(nuke.EndTabGroup_Knob())
    """



    #ACCOUNT TAB

    n.addKnob(nuke.Tab_Knob("account", "Account"))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Text_Knob("sda", " ",SD))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Text_Knob("link"," ",'<a href="https://platform.stability.ai/docs/getting-started/authentication"><span  style="color:#f794ff;font-size:8pt;">Get your Stability API key<span style="color:#504eaa;"></a>'))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.String_Knob("api-key","API key", ''))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Text_Knob("sdinfo", " ",'<span  style="color:#f794ff;font-weight:bold;font-size:8pt;">STABLE<span style="color:#504eaa;">DIFFUSION</span></span><span style="color:#aaa;font-family:sans-serif;font-size:8pt"> - Version 1.0 - 2023 - <a href="https://github.com/besarismaili/Stable-Diffusion-for-NUKE" style="color:#aaa">Github Page</a></span><p><a href="https://www.linkedin.com/in/besarismaili/" style="color:#aaa">Besar Ismaili</a> </p>'))
    n.addKnob(nuke.Text_Knob(""))
    n['text-to-image'].setFlag(0)
    
ui()
