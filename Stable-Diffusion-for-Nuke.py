import nuke
import os
import subprocess
import threading

n = nuke.createNode("Group", inpanel=False)
n.setName("Stability")
n.knob("tile_color").setValue(0xfc402600)
code_tab = nuke.Tab_Knob("code_tab", "Code Tab")
n.addKnob(code_tab)
        
SVG_LOGO = """<?xml version="1.0" encoding="utf-8"?><!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0) --><svg version="1.1" id="Layer_12" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 140 60" enable-background="new 0 0 140 60" xml:space="preserve"><g> <path fill="#1E1D1C" d="M139,59.5l-0.05-34.8l-3.14-3.14h-10.27v3.38l-3.3-3.38h-8.78v3.31c-0.02-0.02-0.37-0.38-0.44-0.44 c-0.68-0.67-1.45-1.25-2.3-1.73c-1.74-0.97-3.68-1.47-5.76-1.47c-2.08,0-4.02,0.49-5.77,1.47c-0.38,0.21-0.74,0.45-1.09,0.7h0V4.57 l-3.14-3.14H78.73v2.59h0l-2.4-2.59h-9.64v1.41c-1.38-0.94-3.17-1.41-5.32-1.41H49.94v4.42l-0.46-1.27l-3.14-3.14h-9.4L36.2,3.42 l-1.85-1.99H14.83v1.01c-1.53-0.87-3.41-1.32-5.61-1.32c-1.59,0-3.06,0.27-4.37,0.8C3.44,2.48,2.3,3.35,1.47,4.48 c-0.86,1.18-1.3,2.6-1.3,4.19c-0.02,1.63,0.37,3.01,1.18,4.12c0.23,0.32,1.18,1.31,1.2,1.34H0l0.12,2 c0.14,2.25,0.95,4.07,2.41,5.42H0.7v34.43l3.14,3.14L139,59.5z"/></g><g> <path fill="#FBEEE3" d="M4.37,20.63c-1.45-1.05-2.24-2.58-2.36-4.61h6.23c0.09,1.07,0.56,1.61,1.43,1.61 c0.32,0,0.59-0.07,0.81-0.22c0.22-0.15,0.33-0.38,0.33-0.7c0-0.44-0.24-0.8-0.71-1.07c-0.48-0.27-1.22-0.59-2.22-0.94 c-1.2-0.42-2.19-0.84-2.97-1.24c-0.78-0.4-1.46-0.99-2.02-1.77C2.31,10.91,2.04,9.92,2.06,8.7c0-1.22,0.31-2.25,0.94-3.1 c0.62-0.85,1.48-1.5,2.56-1.94C6.64,3.22,7.86,3,9.22,3c2.29,0,4.11,0.53,5.45,1.58c1.35,1.06,2.06,2.54,2.13,4.46h-6.31 c-0.02-0.53-0.15-0.91-0.4-1.14c-0.25-0.23-0.55-0.34-0.9-0.34c-0.25,0-0.45,0.08-0.61,0.25c-0.16,0.17-0.24,0.4-0.24,0.7 c0,0.42,0.23,0.77,0.7,1.04c0.47,0.27,1.21,0.6,2.23,0.99c1.18,0.44,2.15,0.86,2.92,1.27c0.77,0.41,1.43,0.97,1.99,1.69 c0.56,0.72,0.85,1.63,0.85,2.72c0,1.14-0.28,2.17-0.85,3.08c-0.56,0.91-1.38,1.62-2.46,2.13c-1.07,0.51-2.35,0.77-3.83,0.77 C7.67,22.2,5.82,21.68,4.37,20.63z"/> <path fill="#FBEEE3" d="M32.46,3.31v4.65H27.5v14.05h-5.86V7.96h-4.91V3.31H32.46z"/> <path fill="#FBEEE3" d="M44.72,19.19h-6.23l-0.92,2.83h-6.15l6.84-18.7h6.76l6.82,18.7h-6.18L44.72,19.19z M43.29,14.78l-1.69-5.2 l-1.69,5.2H43.29z"/> <path fill="#FBEEE3" d="M66.97,14.05c0.62,0.82,0.94,1.77,0.94,2.84c0,1.64-0.54,2.9-1.62,3.79c-1.08,0.89-2.64,1.33-4.66,1.33 h-9.8V3.31h9.54c1.9,0,3.4,0.41,4.49,1.24c1.09,0.83,1.64,2.03,1.64,3.62c0,1.09-0.29,2.01-0.86,2.76 c-0.57,0.75-1.33,1.25-2.28,1.49C65.47,12.69,66.35,13.23,66.97,14.05z M57.69,10.6h2.27c0.53,0,0.92-0.11,1.18-0.32 c0.26-0.21,0.38-0.54,0.38-0.98c0-0.46-0.13-0.8-0.38-1.02c-0.26-0.22-0.65-0.33-1.18-0.33h-2.27V10.6z M61.53,17.01 c0.26-0.2,0.38-0.53,0.38-0.99c0-0.9-0.52-1.35-1.56-1.35h-2.67v2.64h2.67C60.88,17.31,61.28,17.21,61.53,17.01z"/> <path fill="#FBEEE3" d="M74.44,17.58h5.65v4.44H68.57V3.31h5.86V17.58z"/> <path fill="#FBEEE3" d="M86.48,7.99v2.3h5.81v4.41h-5.81v2.64h6.6v4.68H80.62V3.31h12.47v4.68H86.48z"/> <path fill="#FC4026" d="M15.52,24.63c1.47,0.79,2.6,1.89,3.39,3.3c0.79,1.41,1.19,3.01,1.19,4.81c0,1.78-0.4,3.38-1.19,4.81 c-0.79,1.43-1.92,2.55-3.39,3.37c-1.47,0.82-3.18,1.23-5.14,1.23H2.59v-18.7h7.79C12.33,23.44,14.05,23.84,15.52,24.63z M12.99,35.83c0.77-0.72,1.16-1.75,1.16-3.09c0-1.34-0.39-2.37-1.16-3.09c-0.78-0.72-1.82-1.08-3.14-1.08h-1.4v8.35h1.4 C11.17,36.91,12.22,36.55,12.99,35.83z"/> <path fill="#FC4026" d="M26.76,23.44v18.7h-5.86v-18.7H26.76z"/> <path fill="#FC4026" d="M41.28,23.44v4.65h-7.34v2.59h5.28v4.41h-5.28v7.05h-5.86v-18.7H41.28z"/> <path fill="#FC4026" d="M55.15,23.44v4.65h-7.34v2.59h5.28v4.41h-5.28v7.05h-5.86v-18.7H55.15z"/> <path fill="#FC4026" d="M61.54,23.44v10.54c0,0.86,0.19,1.55,0.57,2.05c0.38,0.5,0.99,0.75,1.84,0.75s1.47-0.25,1.88-0.75 c0.4-0.5,0.61-1.18,0.61-2.05V23.44h5.84v10.54c0,1.78-0.37,3.3-1.11,4.56c-0.74,1.26-1.75,2.21-3.04,2.84 c-1.29,0.63-2.72,0.95-4.31,0.95c-1.58,0-2.99-0.32-4.21-0.95c-1.22-0.63-2.18-1.58-2.87-2.83c-0.69-1.25-1.03-2.77-1.03-4.57 V23.44H61.54z"/> <path fill="#FC4026" d="M75.27,40.75c-1.45-1.05-2.24-2.58-2.36-4.61h6.23c0.09,1.07,0.56,1.61,1.43,1.61 c0.32,0,0.59-0.07,0.81-0.22c0.22-0.15,0.33-0.38,0.33-0.7c0-0.44-0.24-0.8-0.71-1.07c-0.48-0.27-1.22-0.59-2.22-0.94 c-1.2-0.42-2.19-0.84-2.97-1.24c-0.78-0.4-1.46-0.99-2.02-1.77c-0.56-0.77-0.84-1.77-0.82-2.98c0-1.22,0.31-2.25,0.94-3.1 c0.62-0.85,1.48-1.5,2.56-1.94c1.08-0.44,2.3-0.66,3.66-0.66c2.29,0,4.11,0.53,5.45,1.58c1.35,1.06,2.06,2.54,2.13,4.46h-6.31 c-0.02-0.53-0.15-0.91-0.4-1.14c-0.25-0.23-0.55-0.34-0.9-0.34c-0.25,0-0.45,0.08-0.61,0.25c-0.16,0.17-0.24,0.4-0.24,0.7 c0,0.42,0.23,0.77,0.7,1.04c0.47,0.27,1.21,0.6,2.23,0.99c1.18,0.44,2.15,0.86,2.92,1.27c0.77,0.41,1.43,0.97,1.99,1.69 c0.56,0.72,0.85,1.63,0.85,2.72c0,1.14-0.28,2.17-0.85,3.08c-0.56,0.91-1.38,1.62-2.46,2.13c-1.07,0.51-2.35,0.77-3.83,0.77 C78.56,42.33,76.72,41.8,75.27,40.75z"/> <path fill="#FC4026" d="M94.54,23.44v18.7h-5.86v-18.7H94.54z"/> <path fill="#FC4026" d="M100.12,41.08c-1.47-0.83-2.64-1.97-3.5-3.43c-0.86-1.46-1.29-3.11-1.29-4.94c0-1.83,0.43-3.48,1.29-4.94 c0.86-1.46,2.03-2.6,3.5-3.42c1.47-0.82,3.09-1.23,4.85-1.23c1.76,0,3.37,0.41,4.83,1.23c1.46,0.82,2.62,1.96,3.47,3.42 c0.85,1.46,1.28,3.11,1.28,4.94c0,1.83-0.43,3.48-1.28,4.94c-0.85,1.46-2.02,2.61-3.49,3.43c-1.47,0.83-3.08,1.24-4.82,1.24 C103.21,42.33,101.59,41.91,100.12,41.08z M107.66,35.74c0.63-0.75,0.95-1.76,0.95-3.02c0-1.29-0.32-2.3-0.95-3.05 c-0.63-0.75-1.53-1.12-2.69-1.12c-1.18,0-2.09,0.37-2.72,1.12c-0.63,0.75-0.95,1.77-0.95,3.05c0,1.27,0.32,2.28,0.95,3.02 c0.63,0.75,1.54,1.12,2.72,1.12C106.13,36.86,107.03,36.48,107.66,35.74z"/> <path fill="#FC4026" d="M133.29,42.14h-5.86l-6.21-9.4v9.4h-5.86v-18.7h5.86l6.21,9.56v-9.56h5.86V42.14z"/></g><g id="Layer_16"> <rect x="2.76" y="44.4" fill="#FFB936" width="130.82" height="9.43"/> <rect x="124.14" y="44.4" fill="#E9E1BF" width="9.43" height="9.43"/> <rect x="48.67" y="44.4" fill="#FC4026" width="81.76" height="3.14"/> <rect x="48.67" y="50.69" fill="#1B63BA" width="75.47" height="3.14"/> <rect x="48.67" y="47.55" fill="#2BA076" width="78.62" height="3.14"/> <polygon fill="#1E1D1C" points="4.53,52.55 6.14,52.55 6.14,49.89 8.15,49.89 8.15,48.64 6.14,48.64 6.14,47.25 8.82,47.25 8.82,45.97 4.53,45.97 "/> <path fill="#1E1D1C" d="M14.02,46.31c-0.52-0.29-1.08-0.43-1.7-0.43c-0.62,0-1.19,0.14-1.7,0.43c-0.52,0.29-0.93,0.69-1.23,1.2 c-0.3,0.51-0.46,1.09-0.46,1.74c0,0.64,0.15,1.22,0.46,1.74c0.3,0.52,0.71,0.92,1.23,1.21c0.52,0.29,1.08,0.43,1.7,0.43 c0.62,0,1.19-0.14,1.7-0.43c0.51-0.29,0.92-0.69,1.22-1.21c0.3-0.52,0.45-1.1,0.45-1.74c0-0.64-0.15-1.22-0.45-1.74 C14.94,46.99,14.53,46.59,14.02,46.31z M13.57,50.63c-0.32,0.35-0.74,0.53-1.26,0.53c-0.53,0-0.96-0.17-1.27-0.52 c-0.32-0.35-0.47-0.81-0.47-1.39c0-0.59,0.16-1.05,0.47-1.4c0.32-0.34,0.74-0.52,1.27-0.52c0.53,0,0.95,0.17,1.26,0.52 c0.32,0.35,0.47,0.81,0.47,1.39C14.05,49.82,13.89,50.28,13.57,50.63z"/> <path fill="#1E1D1C" d="M20.85,49.21c0.25-0.34,0.37-0.73,0.37-1.17c0-0.39-0.09-0.74-0.27-1.06s-0.45-0.56-0.82-0.75 c-0.37-0.18-0.81-0.27-1.33-0.27H16.1v6.59h1.6v-2.49h0.38l1.37,2.49h1.81l-1.52-2.61C20.23,49.8,20.6,49.56,20.85,49.21z M19.36,48.72c-0.15,0.14-0.37,0.22-0.66,0.22h-0.99V47.3h0.99c0.29,0,0.51,0.07,0.66,0.22c0.15,0.14,0.22,0.34,0.22,0.59 C19.58,48.37,19.51,48.57,19.36,48.72z"/> <polygon fill="#1E1D1C" points="27.56,50.05 24.88,45.97 23.27,45.97 23.27,52.55 24.88,52.55 24.88,48.49 27.56,52.55 29.16,52.55 29.16,45.97 27.56,45.97 "/> <path fill="#1E1D1C" d="M33.74,49.91c0,0.39-0.1,0.7-0.3,0.91s-0.49,0.32-0.86,0.32c-0.38,0-0.66-0.11-0.85-0.32 c-0.19-0.21-0.29-0.52-0.29-0.91v-3.94h-1.6v3.93c0,0.59,0.12,1.09,0.36,1.5c0.24,0.41,0.56,0.72,0.97,0.92 c0.41,0.2,0.87,0.31,1.39,0.31c0.52,0,0.99-0.1,1.41-0.31c0.42-0.21,0.76-0.51,1.01-0.92c0.25-0.41,0.38-0.9,0.38-1.49v-3.93h-1.6 V49.91z"/> <polygon fill="#1E1D1C" points="41.69,45.97 39.8,45.97 37.61,48.86 37.61,45.97 36,45.97 36,52.55 37.61,52.55 37.61,49.65 39.82,52.55 41.78,52.55 39.14,49.2 "/> <polygon fill="#1E1D1C" points="46.11,47.25 46.11,45.97 42.08,45.97 42.08,52.55 46.11,52.55 46.11,51.27 43.68,51.27 43.68,49.82 45.83,49.82 45.83,48.59 43.68,48.59 43.68,47.25 "/></g></svg>
"""

n.addKnob(nuke.Multiline_Eval_String_Knob("svg_knob", "svg knob", SVG_LOGO))
n['svg_knob'].setVisible(False)

code_tab.setFlag(nuke.INVISIBLE)



def ui():

    # Get the directory of the current Nuke script
    script_dir = os.path.dirname(nuke.root().name())
    sub_dir = "Stability"
    # Set the directories where the image files and temp files will be stored
    image_dir = os.path.join(os.sep, script_dir, sub_dir, "images")
    temp_dir = os.path.join(os.sep, script_dir, sub_dir, "temp")
    anim_dir = os.path.join(os.sep, script_dir, sub_dir, "animations")
    video_dir = os.path.join(os.sep, script_dir, sub_dir, "stable_video")
    video_temp = os.path.join(os.sep, script_dir, video_dir, "stable_video_temp")
    # Create the directories if they don't exist
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(anim_dir, exist_ok=True)
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(video_temp, exist_ok=True)

    with n:

        Img_input = nuke.nodes.Input(name="Image")
        reformat_img = nuke.nodes.Reformat(format='square_1K',resize='fill')
        reformat_img.setInput(0, Img_input)
        reformat_img_1k = nuke.nodes.Reformat(format='square_1K',resize='fill')
        reformat_img_1k.setInput(0, Img_input)
        sv_format = nuke.Enumeration_Knob("sv_format_k", "Format", ["1024x576", "576x1024", "768x768"])
        nuke.addFormat('1024 576 SV_1024x576_format')
        nuke.addFormat('576 1024 SV_576x1024_format')
        nuke.addFormat('768 768 SV_768x768_format')
        reformat_stable_video_img_1024x576 = nuke.nodes.Reformat(name='reformat_stable_video', format='SV_1024x576_format',resize='fill')
        reformat_stable_video_img_576x1024 = nuke.nodes.Reformat(name='reformat_stable_video', format='SV_576x1024_format',resize='fill')
        reformat_stable_video_img_768x768 = nuke.nodes.Reformat(name='reformat_stable_video', format='SV_768x768_format',resize='fill')
        reformat_stable_video_img_1024x576.setInput(0, Img_input)
        reformat_stable_video_img_576x1024.setInput(0, Img_input)
        reformat_stable_video_img_768x768.setInput(0, Img_input)
        switch_sv_format = nuke.nodes.Switch()
        switch_sv_format.setInput(0, reformat_stable_video_img_1024x576)
        switch_sv_format.setInput(1, reformat_stable_video_img_576x1024)
        switch_sv_format.setInput(2, reformat_stable_video_img_768x768)
        switch_sv_format['which'].setExpression('[string equal [value sv_format_k] "1024x576"]?0:[string equal [value sv_format_k] "576x1024"]?1:2')
        switch_format = nuke.nodes.Switch()
        switch_format.setInput(0, reformat_img)
        switch_format.setInput(1, reformat_img_1k)
        switch_format['which'].setValue(1)
        write_init_image = nuke.nodes.Write(name="write_init_image")
        img_filename = "int2img_.png"
        write_init_image_path = f"{temp_dir}/{img_filename}"
        write_init_image['file'].fromUserText(write_init_image_path)
        write_init_image.setInput(0, switch_format)

        mask_input = nuke.nodes.Input(name="Mask")
        shuffle = nuke.nodes.Shuffle2(name="mask_input_shuffle")
        shuffle.setInput(0, mask_input)
        shuffle["mappings"].setValue([('rgba.alpha', 'rgba.red'), ('rgba.alpha', 'rgba.green'), ('rgba.alpha', 'rgba.blue'), ('rgba.alpha', 'rgba.alpha')])

        reformat_mask = nuke.nodes.Reformat(format='square_1K',resize='fill')
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

        sa_format = nuke.Enumeration_Knob("sa_format_k", "Format", [ "1024x1024", "512x512"])
        stable_animation_frames = nuke.nodes.Write(name="write_init_stable_animation_frames")
        sa_switch_format = nuke.nodes.Switch()
        sa_switch_format.setInput(0, reformat_img)
        sa_switch_format.setInput(1, reformat_img_1k)
        sa_switch_format['which'].setExpression('[string equal [value sa_format_k] "1024x1024"]?1:0')
        sa_shuffle = nuke.nodes.Shuffle2(name="alpha_input_shuffle")
        sa_shuffle.setInput(0, sa_switch_format)
        sa_shuffle["mappings"].setValue([(-1, 'white', 'rgba.alpha')])
        stable_animation_frames.setInput(0, sa_shuffle)


        reformat_sa_mask_1k = nuke.nodes.Reformat(format='square_1K',resize='fill')
        reformat_sa_mask_1k.setInput(0, shuffle)
        sa_mask_switch_format = nuke.nodes.Switch()
        sa_mask_switch_format.setInput(0, reformat_mask)
        sa_mask_switch_format.setInput(1, reformat_sa_mask_1k)
        sa_mask_switch_format['which'].setExpression('[string equal [value sa_format_k] "1024x1024"]?1:0')
        stable_animation_mask_frames = nuke.nodes.Write(name="write_init_stable_animation_mask_frames")
        stable_animation_mask_frames.setInput(0, sa_mask_switch_format)

        init_sa_init_image = nuke.nodes.Write(name="write_init_sa_init_image")
        init_sa_init_image['file'].fromUserText(f"{video_temp}/init_sa_init_image_.png")
        init_sa_init_image.setInput(0, sa_shuffle)

        init_stable_video_image = nuke.nodes.Write(name="write_init_stable_video_image")
        init_stable_video_image['file'].fromUserText(f"{video_temp}/init_stable_video_image_.png")
        init_stable_video_image.setInput(0, switch_sv_format)


        cam_input = nuke.nodes.Input(name="Camera")
        camera = nuke.nodes.Camera3(name="sa_cam")
        camera.setInput(0, cam_input)
        camera['translate'].setExpression("[value [topnode input2].translate.x]",0)
        camera['translate'].setExpression("[value [topnode input2].translate.y]",1)
        camera['translate'].setExpression("[value [topnode input2].translate.z]",2)
        camera['rotate'].setExpression("[value [topnode input2].rotate.x]",0)
        camera['rotate'].setExpression("[value [topnode input2].rotate.y]",1)
        camera['rotate'].setExpression("[value [topnode input2].rotate.z]",2)
        
        output = nuke.nodes.Output()
        merge = nuke.nodes.Merge(mix='0.5')
        merge.setInput(0, reformat_img)
        merge.setInput(1, reformat_mask)

        sv_switch = nuke.nodes.Switch(name="sv_switch_output")
        sv_switch.setInput(0, merge)
        sv_switch.setInput(1, switch_sv_format)
        sv_switch.setInput(2, sa_switch_format)

        output.setInput(0, sv_switch)

    set_img_init_image = """
s = nuke.thisNode()

with s:
    no=nuke.toNode('sv_switch_output')
    no['which'].setValue(0)
    """

    n.addKnob(nuke.Tab_Knob("img", "Still Image"))
    n.addKnob(nuke.PyCustom_Knob("img_logo", "", "logo(nuke.thisNode())"))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.PyScript_Knob("set_i2i_init_image_btn", "Preview Init Image", set_img_init_image)) 
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.BeginTabGroup_Knob())
    n.addKnob(nuke.Tab_Knob("text-to-image","Text to image"))
    n.addKnob(nuke.Text_Knob(""))
    ti_eng_knob = nuke.Enumeration_Knob("ti_engine_name", "Model", ['stable-diffusion-xl-1024-v0-9', 'stable-diffusion-xl-1024-v1-0'])
    ti_eng_knob.setValue('stable-diffusion-xl-1024-v1-0')
    n.addKnob(ti_eng_knob) 
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("ti_prompt", "Prompt", "cute cat wearing sunglasses, colorful, fantasy splash, light white and pink pastel tetradic colours, cute and quirky, bokeh, soft lighting, retro aesthetic, focused on the character, 4K resolution, photorealist, zoomed out, full body, cotton candy, day time, vibrant, bright, dream, particles of candy"))
    n.addKnob(nuke.Double_Knob("ti_weight","Prompt Weight"))
    n["ti_weight"].setValue(0.5)
    n["ti_weight"].setRange(-1,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("ti_prompt2", "Second Prompt", "blurry, low resolution"))
    n.addKnob(nuke.Double_Knob("ti_weight2","Second Prompt Weight"))
    n["ti_weight2"].setValue(-0.9)
    n["ti_weight2"].setRange(-1,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Tab_Knob('img_tab', 'Settings', nuke.TABBEGINGROUP))
    n.addKnob(nuke.Double_Knob("ti_cfg_scale","CFG Scale"))
    n["ti_cfg_scale"].setValue(7)
    n["ti_cfg_scale"].setRange(0,35)
    n["ti_cfg_scale"].setTooltip("This parameter controls how strictly the diffusion process adheres to the prompt text. Higher values keep your image closer to your prompt. The range is from 0 to 35")
    n.addKnob(nuke.Enumeration_Knob("ti_style_preset","Style Preset", [("None"),("3d-model"), ("analog-film"),("anime"),("cinematic"),("comic-book"),("digital-art"),("enhance"),("fantasy-art"),("isometric"),("line-art"),("low-poly"),("modeling-compound"),("neon-punk"),("origami"),("photographic"),("pixel-art"),("tile-texture")]))
    n.addKnob(nuke.Enumeration_Knob("ti_clip_guidance_preset","Clip Guidance Preset", [("NONE"), ("FAST_BLUE"), ("FAST_GREEN"), ("SIMPLE"),("SLOW"),("SLOWER"),("SLOWEST")]))
    n.addKnob(nuke.Enumeration_Knob("ti_sampler","Sampler", [("DDIM"), ("DDPM"),("K_DPMPP_2M"), ("K_DPMPP_2S_ANCESTRAL"), ("K_EULER"),("K_EULER_ANCESTRAL"),("K_HEUN"), ("K_LMS")]))
    n["ti_sampler"].setTooltip("This parameter determines the sampler to use for the diffusion process.")
    n.addKnob(nuke.Int_Knob("ti_samples","Batch Size"))
    n["ti_samples"].setValue(1)
    n["ti_samples"].setRange(1,10)
    n["ti_samples"].setTooltip("This parameter sets the number of images to generate. The range is from 1 to 10.")
    n.addKnob(nuke.Int_Knob("ti_seed","Seed"))
    n["ti_seed"].setValue(0)
    n["ti_seed"].setRange(1,4294967295)
    n["ti_seed"].setTooltip("This parameter sets the random noise seed. The range is from 0 to 4294967295. If this option is set to 0, a random seed will be used.")
    n.addKnob(nuke.Int_Knob("ti_steps","Steps"))
    n["ti_steps"].setValue(50)
    n["ti_steps"].setRange(10,150)
    n["ti_steps"].setTooltip("This parameter sets the number of diffusion steps to run. The range is from 10 to 150.")
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))
    
    get_text_to_image_response = """
import base64
import os
import requests

engine_id = "stable-diffusion-v1-5"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
sv_api_key = os.getenv("STABILITY_sv_API_KEY")

try:
    # Get the directory of the current Nuke script
    script_dir = os.path.dirname(nuke.root().name())

    # Set the subdirectory where the image files will be stored
    sub_dir = "Stability"

    # Set the directories where the image files and temp files will be stored
    image_dir = os.path.join(script_dir, sub_dir, "images")
    temp_dir = os.path.join(script_dir, sub_dir, "temp")

    # Create the directories if they don't exist
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    # Get the list of existing image files in the directory
    existing_files = os.listdir(image_dir)
except OSError as e:
    raise Exception("Please ensure that the Nuke script is saved and that you have write permissions in the directory where the script is saved.")

engine_txt_img=nuke.thisNode().knob('ti_engine_name').value()
prompt_txt_img=nuke.thisNode().knob('ti_prompt').value()
weight_txt_img=nuke.thisNode().knob('ti_weight').getValue()
prompt2_txt_img=nuke.thisNode().knob('ti_prompt2').value()
weight2_txt_img=nuke.thisNode().knob('ti_weight2').getValue()
cfg_scale_txt_img=int(nuke.thisNode().knob('ti_cfg_scale').getValue())
clip_guidance_preset_txt_img=nuke.thisNode().knob('ti_clip_guidance_preset').value()
style_preset_txt_img=nuke.thisNode().knob('ti_style_preset').value()
samples_txt_img=int(nuke.thisNode().knob('ti_samples').getValue())
steps_txt_img=int(nuke.thisNode().knob('ti_steps').getValue())

sv_api_key = nuke.thisNode().knob('api-key').value()

format = 512
if engine_txt_img in ['stable-diffusion-xl-1024-v0-9', 'stable-diffusion-xl-1024-v1-0']:
    format = 1024
else:
    format = 512

json_data = {
    "text_prompts": [
    {
        "text": prompt_txt_img,
        "weight": weight_txt_img
    },
    {
        "text": prompt2_txt_img,
        "weight": weight2_txt_img,
    }
    ],
    "cfg_scale": cfg_scale_txt_img,
    "clip_guidance_preset": clip_guidance_preset_txt_img,
    "height": format,
    "width": format,
    "samples": samples_txt_img,
    "steps": steps_txt_img,
}

if style_preset_txt_img != 'None':
    json_data["style_preset"] = style_preset_txt_img

response = requests.post(
    f"{api_host}/v1/generation/{engine_txt_img}/text-to-image",
    headers={
        "Content-Type": 'application/json',
        "Accept": 'application/json',
        "Authorization": f'Bearer {sv_api_key}'
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
        read_node['file'].fromUserText(input_path)
        

"""

    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.PyScript_Knob("t2i_dream", "Dream", get_text_to_image_response))
    n["t2i_dream"].setFlag(0x0000000000001000)
        
    #IMAGE TO IMAGE TAB

    n.addKnob(nuke.Tab_Knob("image-to-image","Image to image"))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Text_Knob(""))
    ii_eng_knob = nuke.Enumeration_Knob("ii_engine_name", "Model", ['stable-diffusion-xl-1024-v0-9', 'stable-diffusion-xl-1024-v1-0'])
    ii_eng_knob.setValue('stable-diffusion-xl-1024-v1-0')
    ii_eng_knob.clearFlag(nuke.STARTLINE) 
    n.addKnob(ii_eng_knob)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("ii_prompt1", "Prompt", "cute cat wearing sunglasses, colorful, fantasy splash, light white and pink pastel tetradic colours, cute and quirky, bokeh, soft lighting, retro aesthetic, focused on the character, 4K resolution, photorealist, zoomed out, full body, cotton candy, day time, vibrant, bright, dream, particles of candy"))
    n.addKnob(nuke.Double_Knob("ii_weight1","Prompt Weight"))
    n["ii_weight1"].setValue(0.5)
    n["ii_weight1"].setRange(-1,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("ii_prompt2", "Second Prompt", "blurry, low resolution"))
    n.addKnob(nuke.Double_Knob("ii_weight2","Second Prompt Weight"))
    n["ii_weight2"].setValue(-0.9)
    n["ii_weight2"].setRange(-1,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Double_Knob("image_strength","Image Strength"))
    n["image_strength"].setValue(0.35)
    n["image_strength"].setRange(0.0,1.0)
    n.addKnob(nuke.Enumeration_Knob("ii_init_image_mode","Init Image Mode", [("IMAGE_STRENGTH"), ("STEP_SCHEDULE.")]))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Tab_Knob('img2img_tab', 'Settings', nuke.TABBEGINGROUP))
    n.addKnob(nuke.Double_Knob("ii_cfg_scale","CFG Scale"))
    n["ii_cfg_scale"].setTooltip("This parameter controls how strictly the diffusion process adheres to the prompt text. Higher values keep your image closer to your prompt. The range is from 0 to 35")
    n["ii_cfg_scale"].setValue(7)
    n["ii_cfg_scale"].setRange(0,35)
    n.addKnob(nuke.Enumeration_Knob("ii_style_preset","Style Preset", [("None"),("3d-model"), ("analog-film"),("anime"),("cinematic"),("comic-book"),("digital-art"),("enhance"),("fantasy-art"),("isometric"),("line-art"),("low-poly"),("modeling-compound"),("neon-punk"),("origami"),("photographic"),("pixel-art"),("tile-texture")]))
    n.addKnob(nuke.Enumeration_Knob("ii_clip_guidance_preset","Clip Guidance Preset", [("NONE"), ("FAST_BLUE"), ("FAST_GREEN"), ("SIMPLE"),("SLOW"),("SLOWER"),("SLOWEST")]))
    n.addKnob(nuke.Enumeration_Knob("ii_sampler","Sampler", [("DDIM"), ("DDPM"),("K_DPMPP_2M"), ("K_DPMPP_2S_ANCESTRAL"), ("K_EULER"),("K_EULER_ANCESTRAL"),("K_HEUN"), ("K_LMS")]))
    n.addKnob(nuke.Int_Knob("ii_samples","Batch Size"))
    n["ii_samples"].setTooltip("This parameter sets the number of images to generate. The range is from 1 to 10.")
    n["ii_samples"].setValue(1)
    n["ii_samples"].setRange(1,10)
    n.addKnob(nuke.Int_Knob("ii_seed","Seed"))
    n["ii_samples"].setTooltip("This parameter sets the random noise seed. The range is from 0 to 4294967295. If this option is set to 0, a random seed will be used.")
    n["ii_seed"].setValue(0)
    n["ii_seed"].setRange(1,4294967295)
    n.addKnob(nuke.Int_Knob("ii_steps","Steps"))
    n["ii_steps"].setValue(30)
    n["ii_steps"].setRange(10,150)
    n["ii_steps"].setTooltip("This parameter sets the number of diffusion steps to run. The range is from 10 to 150.")
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))

    get_image_to_image_response = """
import base64
import os
import requests

engine_id = "stable-diffusion-v1-5"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
sv_api_key = os.getenv("STABILITY_sv_API_KEY")

try:
    # Get the directory of the current Nuke script
    script_dir = os.path.dirname(nuke.root().name())
    # Set the subdirectory where the image files will be stored
    sub_dir = "Stability"
    # Set the directories where the image files and temp files will be stored
    image_dir = os.path.join(script_dir, sub_dir, "images")
    temp_dir = os.path.join(script_dir, sub_dir, "temp")
    # Create the directories if they don't exist
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)
    # Get the list of existing image files in the directory
    existing_files = os.listdir(image_dir)
except OSError as e:
    raise Exception("Please ensure that the Nuke script is saved and that you have write permissions in the directory where the script is saved.")

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
sv_api_key = nuke.thisNode().knob('api-key').value()
switch_format_img = nuke.toNode('Switch1')

if img_engine in ['stable-diffusion-xl-1024-v0-9', 'stable-diffusion-xl-1024-v1-0']:
    switch_format_img["which"].setValue(1)
else:
    switch_format_img["which"].setValue(0)

nuke.execute(nuke.toNode('write_init_image'), start=1, end=1)

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

if style_preset_img_img != 'None':
    json_data["style_preset"] = style_preset_img_img

response = requests.post(
    f"{api_host}/v1/generation/{img_engine}/image-to-image",
    headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {sv_api_key}"
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
        read_node['file'].fromUserText(input_path)
        

"""
    
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.PyScript_Knob("i2i_dream", "Dream", get_image_to_image_response))
    n["i2i_dream"].setFlag(0x0000000000001000)

    #IMAGE TO IMAGE/MASKING TAB

    n.addKnob(nuke.Tab_Knob("inpainting","Inpainting"))
    n.addKnob(nuke.Text_Knob(""))
    iim_eng_knob = nuke.Enumeration_Knob("iim_engine_name", "Model", ['stable-diffusion-xl-1024-v0-9', 'stable-diffusion-xl-1024-v1-0'])
    iim_eng_knob.setValue("stable-diffusion-xl-1024-v0-9")
    n.addKnob(iim_eng_knob) 
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("iim_prompt1", "Prompt", "cute cat wearing sunglasses, colorful, fantasy splash, light white and pink pastel tetradic colours, cute and quirky, bokeh, soft lighting, retro aesthetic, focused on the character, 4K resolution, photorealist, zoomed out, full body, cotton candy, day time, vibrant, bright, dream, particles of candy"))
    n.addKnob(nuke.Double_Knob("iim_weight1","Prompt Weight"))
    n["iim_weight1"].setValue(0.5)
    n["iim_weight1"].setRange(-1,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Multiline_Eval_String_Knob("iim_prompt2", "Second Prompt", "blurry, low resolution"))
    n.addKnob(nuke.Double_Knob("iim_weight2","Second Prompt Weight"))
    n["iim_weight2"].setValue(-0.9)
    n["iim_weight2"].setRange(-1,1)
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Double_Knob("iim_cfg_scale","CFG Scale"))
    n["iim_cfg_scale"].setValue(7)
    n["iim_cfg_scale"].setRange(1,10)
    n.addKnob(nuke.Enumeration_Knob("iim_style_preset","Style Preset", [("None"),("3d-model"), ("analog-film"),("anime"),("cinematic"),("comic-book"),("digital-art"),("enhance"),("fantasy-art"),("isometric"),("line-art"),("low-poly"),("modeling-compound"),("neon-punk"),("origami"),("photographic"),("pixel-art"),("tile-texture")]))
    n.addKnob(nuke.Enumeration_Knob("iim_clip_guidance_preset","Clip Guidance Preset", [("NONE"), ("FAST_BLUE"), ("FAST_GREEN"), ("SIMPLE"),("SLOW"),("SLOWER"),("SLOWEST")]))
    n.addKnob(nuke.Enumeration_Knob("iim_sampler","Sampler", [("DDIM"), ("DDPM"),("K_DPMPP_2M"), ("K_DPMPP_2S_ANCESTRAL"), ("K_EULER"),("K_EULER_ANCESTRAL"),("K_HEUN"), ("K_LMS")]))
    n.addKnob(nuke.Int_Knob("iim_samples","Batch Size"))
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
sv_api_key = os.getenv("STABILITY_sv_API_KEY")

try:
    # Get the directory of the current Nuke script
    #script_dir = os.path.dirname(nuke.root().name())

    # Set the subdirectory where the image files will be stored
    sub_dir = "Stability"

    # Set the directories where the image files and temp files will be stored
    image_dir = os.path.join(script_dir, sub_dir, "images")
    temp_dir = os.path.join(script_dir, sub_dir, "temp")

    # Create the directories if they don't exist
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    # Get the list of existing image files in the directory
    existing_files = os.listdir(image_dir)
except OSError as e:
    raise Exception("Please ensure that the Nuke script is saved and that you have write permissions in the directory where the script is saved.")

sv_api_key = nuke.thisNode().knob('api-key').value()

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

if style_preset_img_msk != 'None':
    json_data["style_preset"] = style_preset_img_msk

response = requests.post(
    f"{api_host}/v1/generation/{inpaint_engine}/image-to-image/masking",
    headers={
        "Accept": 'application/json',
        "Authorization": f"Bearer {sv_api_key}"
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

    #IMAGE TO IMAGE/UPSCALE TAB

    n.addKnob(nuke.Tab_Knob("upscale-tab","Upscale"))
    n.addKnob(nuke.Text_Knob(""))
    iiu_eng_knob = nuke.Enumeration_Knob("ui_engine_name", "Model", ['esrgan-v1-x2plus'])
    n.addKnob(iiu_eng_knob)
    n.addKnob(nuke.Enumeration_Knob("upscale","Upscale size", [("1024x1024"), ("2048x2048")]))
    n["upscale"].setValue("1024x1024")
    iiu_eng_knob.clearFlag(nuke.STARTLINE) 

    get_image_to_image_upscale_response = """
import os
import requests

engine_id = "esrgan-v1-x2plus"
api_host = os.getenv("API_HOST", "https://api.stability.ai")
sv_api_key = os.getenv("STABILITY_sv_API_KEY")

try:
    # Get the directory of the current Nuke script
    script_dir = os.path.dirname(nuke.root().name())

    # Set the subdirectory where the image files will be stored
    sub_dir = "Stability"

    # Set the directories where the image files and temp files will be stored
    image_dir = os.path.join(script_dir, sub_dir, "images")
    temp_dir = os.path.join(script_dir, sub_dir, "temp")

    # Create the directories if they don't exist
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    # Get the list of existing image files in the directory
    existing_files = os.listdir(image_dir)
except OSError as e:
    raise Exception("Please ensure that the Nuke script is saved and that you have write permissions in the directory where the script is saved.")

nuke.execute(nuke.toNode('write_upscale_image'), start=1, end=1)

upscale_engine = nuke.thisNode().knob('ui_engine_name').value()
sv_api_key = nuke.thisNode().knob('api-key').value()
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
        "Authorization": f"Bearer {sv_api_key}"
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
    n.addKnob(nuke.EndTabGroup_Knob())

    #ANIMATION TAB
    set_anim_init_image = """
s = nuke.thisNode()

with s:
    no=nuke.toNode('sv_switch_output')
    no['which'].setValue(2)
    """
    # Prompts tab
    n.addKnob(nuke.Tab_Knob("anim_tab", "Animation"))
    n.addKnob(nuke.PyCustom_Knob("anim_logo", "", "logo(nuke.thisNode())"))
    n.addKnob(nuke.Text_Knob("")) 
    n.addKnob(nuke.PyScript_Knob("set_anim_init_image_btn", "Preview Init Image", set_anim_init_image)) 
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.BeginTabGroup_Knob())
    n.addKnob(nuke.Tab_Knob('promts', 'Prompts'))
    n.addKnob(nuke.Text_Knob("aptx","","Animation Prompts"))
    n.addKnob(nuke.Text_Knob(""))  
    n.addKnob(nuke.Text_Knob("mx","","Max Frames"))
    n.addKnob(nuke.Int_Knob('max_frames', ''))
    n['max_frames'].setValue(20)
    n['max_frames'].clearFlag(nuke.STARTLINE)
    n.addKnob(nuke.Int_Knob('fps', 'FPS'))
    n['fps'].setValue(12)
    n['fps'].clearFlag(nuke.STARTLINE)
    n.addKnob(nuke.Multiline_Eval_String_Knob('animation_prompts', 'Animation Prompts'))
    n['animation_prompts'].setVisible(False)
    n.addKnob(nuke.PyCustom_Knob("anim_prompts", "", 'anim_prompts(nuke.thisNode())'))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Text_Knob("nptx","","Negative Prompt"))
    n.addKnob(nuke.Multiline_Eval_String_Knob('negative_prompt', '', 'blurry, low resolution'))
    n.addKnob(nuke.Text_Knob("ngtp","","Negative Prompt Weight"))
    n.addKnob(nuke.Int_Knob("negative_prompt_weight", ""))
    n['negative_prompt_weight'].setValue(-1)
    n.addKnob(nuke.Boolean_Knob("interpolate_prompts", "Interpolate Prompts"))
    n['interpolate_prompts'].setValue(False)
    n.addKnob(nuke.Boolean_Knob('reverse', 'Reverse'))
    n['reverse'].setVisible(False)
    n.addKnob(nuke.String_Knob('frame_interpolation_mode', 'Frame Interpolation Mode'))
    n.addKnob(nuke.Int_Knob('frame_interpolation_factor', 'Frame Interpolation Factor'))
    n['frame_interpolation_mode'].setVisible(False)
    n['frame_interpolation_factor'].setVisible(False)    
    n.addKnob(nuke.Text_Knob(""))

    # Config tab

    n.addKnob(nuke.Tab_Knob('config', 'Config'))
    n.addKnob(nuke.Enumeration_Knob("anim_engine_name", "Model", ["stable-diffusion-xl-1024-v0-9"]))
    n['anim_engine_name'].setValue('stable-diffusion-xl-1024-v0-9')     
    n.addKnob(nuke.Enumeration_Knob("animation_mode", "Animation Mode", ['2D', '3D warp', '3D render', 'Video Input']))
    n['animation_mode'].setValue('Video Input')
    n.addKnob(nuke.Enumeration_Knob("border", "Border", ['reflect', 'replicate', 'wrap', 'zero', 'prefill']))
    n['border'].setValue('replicate')
    n['border'].clearFlag(nuke.STARTLINE)
    n.addKnob(sa_format)
    n['sa_format_k'].setVisible(False)
    n.addKnob(nuke.Int_Knob('hwh', 'Height'))
    n['hwh'].setExpression('[string equal [value sa_format_k] "1024x1024"]?1024:512')
    n.addKnob(nuke.Int_Knob('hww', 'Width'))
    n['hww'].setExpression('[string equal [value sa_format_k] "1024x1024"]?1024:512')
    n['hwh'].setVisible(False)
    n['hww'].setVisible(False)
    n['hww'].clearFlag(nuke.STARTLINE)
    n.addKnob(nuke.Enumeration_Knob("anim_style_preset","Style Preset", [("None"),("3d-model"), ("analog-film"),("anime"),("cinematic"),("comic-book"),("digital-art"),("enhance"),("fantasy-art"),("isometric"),("line-art"),("low-poly"),("modeling-compound"),("neon-punk"),("origami"),("photographic"),("pixel-art"),("tile-texture")]))
    n['anim_style_preset'].setValue('None')
    n.addKnob(nuke.Enumeration_Knob('sampler', 'Sampler', ["DDIM", "PLMS", "K_euler", "K_euler_ancestral", "K_heun", "K_dpm_2", "K_dpm_2_ancestral", "K_lms", "K_dpmpp_2m", "K_dpmpp_2s_ancestral"]))
    n['sampler'].setValue('K_dpmpp_2m')
    n['sampler'].clearFlag(nuke.STARTLINE)
    n.addKnob(nuke.Int_Knob('seed', 'Seed'))
    n['seed'].setValue(-1)
    n.addKnob(nuke.Int_Knob('cfg_scale', 'Guidance Scale'))
    n['cfg_scale'].setValue(7)
    n['cfg_scale'].clearFlag(nuke.STARTLINE)
    n.addKnob(nuke.Enumeration_Knob('clip_guidance', 'CLIP Guidance', ["None", "Simple", "FastBlue", "FastGreen"]))
    n['clip_guidance'].setValue('None')
    n.addKnob(nuke.Boolean_Knob('steps_strength_adj', 'Steps Strength Adj'))
    n['steps_strength_adj'].setValue(False)
    n.addKnob(nuke.Boolean_Knob('locked_seed', 'Locked Seed'))
    n['locked_seed'].setValue(True)

    #Noise and Curve
    n.addKnob(nuke.Tab_Knob('noise_curve', 'Noise and Curve', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Double_Knob('noise_add_curve', 'Noise Add Curve'))
    n['noise_add_curve'].setValue(0.02)
    n.addKnob(nuke.Double_Knob('noise_scale_curve', 'Noise Scale Curve'))
    n['noise_scale_curve'].setValue(0.99)
    n.addKnob(nuke.Double_Knob('strength_curve', 'Previous Frame Strength Curve'))
    n['strength_curve'].setValue(0.65)
    n.addKnob(nuke.Int_Knob('steps_curve', 'Steps curve'))
    n['steps_curve'].setValue(30)
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))

    #Coherence
    n.addKnob(nuke.Tab_Knob('Coherence', 'Coherence', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Int_Knob('diffusion_cadence_curve', 'Cadence'))
    n['diffusion_cadence_curve'].setValue(1)
    n.addKnob(nuke.Enumeration_Knob('cadence_interp', 'Cadence Interp', ['film', 'mix', 'rife', 'vae-lerp', 'vae-slerp']))
    n['cadence_interp'].setValue("mix")
    n.addKnob(nuke.Boolean_Knob('cadence_spans', 'Cadence Spans'))
    n['cadence_spans'].setValue(False)
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))

    #Color
    n.addKnob(nuke.Tab_Knob('color', 'Color', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Enumeration_Knob('color_coherence', 'Colour Coherence', ['None', 'HSV', 'LAB', 'RGB']))
    n['color_coherence'].setValue('LAB')
    n.addKnob(nuke.Double_Knob('brightness_curve', 'Brightness Curve'))
    n['brightness_curve'].setValue(1.0)
    n.addKnob(nuke.Double_Knob('contrast_curve', 'Contrast Curve'))
    n['contrast_curve'].setValue(1.0)
    n.addKnob(nuke.Double_Knob('hue_curve', 'Hue Curve'))
    n['hue_curve'].setValue(0.0)
    n.addKnob(nuke.Double_Knob('saturation_curve', 'Saturation Curve'))
    n['saturation_curve'].setValue(1.0)
    n.addKnob(nuke.Double_Knob('lightness_curve', 'Lightness Curve'))
    n['lightness_curve'].setValue(0.0)
    n.addKnob(nuke.Boolean_Knob('color_match_animate', 'Animate Colour Match'))
    n['color_match_animate'].setValue(True)
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))

    #Depth
    n.addKnob(nuke.Tab_Knob('depth', 'Depth', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Double_Knob('depth_model_weight', 'Depth Model Weight'))
    n['depth_model_weight'].setValue([0.3])
    n.addKnob(nuke.Int_Knob('near_plane', 'Near Plane'))
    n['near_plane'].setValue(200)
    n.addKnob(nuke.Int_Knob('far_plane', 'Far Plane'))
    n['far_plane'].setValue(10000)
    n.addKnob(nuke.Double_Knob('fov_curve', 'Fov Curve'))
    n['fov_curve'].setValue([25.0])
    n.addKnob(nuke.Double_Knob('depth_blur_curve', 'Depth Blur Curve'))
    n['depth_blur_curve'].setValue([0.0])
    n.addKnob(nuke.Double_Knob('depth_warp_curve', 'Depth Warp Curve'))
    n['depth_warp_curve'].setValue([1.0])
    n.addKnob(nuke.Boolean_Knob('save_depth_maps', 'save depth maps'))
    n['save_depth_maps'].setVisible(False)
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))

    #3D Render
    n.addKnob(nuke.Tab_Knob('3drender', '3D Render', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Enumeration_Knob('camera_type', 'Camera Type', ['perspective', 'orthographic']))
    n.addKnob(nuke.Enumeration_Knob('render_mode', 'Render Mode', ['mesh', 'pointcloud']))
    n.addKnob(nuke.Double_Knob('mask_power', 'Mask Power'))
    n['mask_power'].setValue(0.3)
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))

    #Inpainting 
    n.addKnob(nuke.Tab_Knob('inpainting', 'Inpainting', nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Boolean_Knob('use_inpainting_model', 'Use Inpainting Model'))
    n.addKnob(nuke.Boolean_Knob('inpaint_border', 'Inpaint Border'))
    n.addKnob(nuke.Double_Knob('mask_min_value', 'Mask Min Value'))
    n['mask_min_value'].setValue(0.25)
    n.addKnob(nuke.Double_Knob('mask_binarization_thr', 'Mask Binarization THR'))
    n['mask_binarization_thr'].setValue(0.5)
    n.addKnob(nuke.Boolean_Knob('save_inpaint_masks', 'save inpaint masks'))
    n['save_inpaint_masks'].setVisible(False)
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))

    # Input tab
    n.addKnob(nuke.Tab_Knob('input', 'Input'))
    n.addKnob(nuke.Tab_Knob("Init_Image_tx", "Init Image", nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.Boolean_Knob('use_init_img_input', 'Use Init Image Input'))
    n.addKnob(nuke.Int_Knob("init_image_frame", "Frame"))
    n['init_image_frame'].setValue(1)
    n.addKnob(nuke.PyScript_Knob("int_img_set_currecnt_frame", "Set Current Frame", "nuke.thisNode().knob('init_image_frame').setValue(nuke.frame())"))
    n.addKnob(nuke.File_Knob('init_image', 'Image Path'))
    n.addKnob(nuke.Enumeration_Knob('init_sizing', 'Init Sizing', ["cover", "stretch", "resize-canvas"]))
    n['init_sizing'].setValue("stretch")
    n['init_sizing'].setVisible(False)
    n.addKnob(nuke.Text_Knob("Init_Image_txe", ""))
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))

    n.addKnob(nuke.Tab_Knob("Mask_tx", "Mask", nuke.TABBEGINCLOSEDGROUP))
    n.addKnob(nuke.File_Knob('mask_path', 'Mask Path'))
    n.addKnob(nuke.Boolean_Knob('mask_invert', 'Mask Invert'))
    n['mask_invert'].setVisible(False)
    n.addKnob(nuke.Text_Knob("Mask_txe", ""))
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))

    n.addKnob(nuke.Tab_Knob("Video_Input_tx", "Video Input", nuke.TABBEGINGROUP))
    n.addKnob(nuke.Text_Knob("video_input_frame_range","", "Frame Range"))
    n['video_input_frame_range'].clearFlag(nuke.STARTLINE)
    n.addKnob(nuke.Int_Knob("video_input_first_frame", ""))
    n['video_input_first_frame'].setValue(0)
    n['video_input_first_frame'].clearFlag(nuke.STARTLINE)
    n.addKnob(nuke.Int_Knob("video_input_last_frame", ""))
    n['video_input_last_frame'].setValue(50)
    n['video_input_last_frame'].clearFlag(nuke.STARTLINE)
    n.addKnob(nuke.PyScript_Knob("video_input_set_max_frame", "Set to Max Frames", "nuke.thisNode().knob('video_input_last_frame').setValue(nuke.thisNode().knob('max_frames').value())"))
    n.addKnob(nuke.Boolean_Knob('use_video_input', 'Always render new input video'))
    n['use_video_input'].setFlag(nuke.STARTLINE)
    n.addKnob(nuke.File_Knob('video_init_path', 'Video Path'))
    n.addKnob(nuke.Double_Knob('video_mix_in_curve', 'Mix-in Curve'))
    n['video_mix_in_curve'].setValue([1])
    n.addKnob(nuke.Boolean_Knob('video_flow_warp', 'Flow Warp'))
    n['video_flow_warp'].setValue(True)
    n.addKnob(nuke.Int_Knob('extract_nth_frame', 'Extract Nth Frame'))
    n['extract_nth_frame'].setValue(1)
    n.addKnob(nuke.Tab_Knob('', None, nuke.TABENDGROUP))

    # Camera tab 
    n.addKnob(nuke.Tab_Knob('camera', 'Camera'))
    n.addKnob(nuke.Text_Knob('2d-camera', '2D Camera'))
    n.addKnob(nuke.Double_Knob('angle', 'Angle'))
    n['angle'].setValue(0)
    n.addKnob(nuke.Double_Knob('zoom', 'Zoom'))
    n['zoom'].setValue(1)
    n.addKnob(nuke.Text_Knob('2D-3D-camera-translation', '2D and 3D Camera translation'))
    n.addKnob(n.node('sa_cam').knob('translate'))
    n.addKnob(n.node('sa_cam').knob('rotate'))
    n.addKnob(nuke.EndTabGroup_Knob())    


    get_anim ="""
from stability_sdk import api
import os
import json
from stability_sdk.animation import (
    AnimationArgs,
    Animator,
    AnimationSettings,
    BasicSettings,
    CoherenceSettings,
    ColorSettings,
    DepthSettings,
    InpaintingSettings,
    Rendering3dSettings,
    CameraSettings,
    VideoInputSettings,
    VideoOutputSettings,
)
from stability_sdk.api import (
    ClassifierException, 
    Context,
    OutOfCreditsException,
)

from stability_sdk.utils import (
    create_video_from_frames,
    extract_frames_from_video,
    interpolate_mode_from_string
)

try:
    # Get the directory of the current Nuke script
    script_dir = os.path.dirname(nuke.root().name())

    # Set the directories where the image files and temp files will be stored
    anim_dir = os.path.join(os.sep, script_dir, "Stability", "animations")
    
    # Create the directories if they don't exist
    os.makedirs(anim_dir, exist_ok=True)

    # Initialize version
    version = 1

    # Create a versioned directory
    version_dir = os.path.join(os.sep, anim_dir, f"v{version:03d}")

    # Check if the directory already exists
    while os.path.exists(version_dir):
        # If the directory already exists, increment the version and create a new directory
        version += 1
        version_dir = os.path.join(os.sep, anim_dir, f"v{version:03d}")

    frames_dir = os.path.join(os.sep, version_dir, "frames")
    temp_frames_dir = os.path.join(os.sep, version_dir, "temp_frames")
    temp_mask_dir = os.path.join(os.sep, version_dir, "temp_mask_frames")
    
    # Create the new versioned directory
    os.makedirs(frames_dir, exist_ok=True)
    os.makedirs(temp_frames_dir, exist_ok=True)
    os.makedirs(temp_mask_dir, exist_ok=True)

except OSError as e:
    raise Exception("Please ensure that the Nuke script is saved and that you have write permissions in the directory where the script is saved.")

def cam_keyframes(knob_name, axis_index):
    #print("CAM KEYFRAMES IN")
    axis = ["x", "y", "z"][axis_index]
    #print(f"keyframes for {axis}")

    node = nuke.thisNode()
    # Get the total number of frames in the script
    total_frames = int(node.knob('max_frames').value())

    # Initialize an empty list to store the knob values
    knob_values = []

    # Check if the value is a float
    if node.input(2) is None:
        return "0:(0)"
    else:
        # Iterate over each frame
        for frame in range(total_frames + 1):
            # Get the value of the knob at the current frame for the specified axis
            value = knob_name.getValueAt(frame, axis_index)
            #print(value)
            # Append the frame number and knob value to the list
            knob_values.append(f"{frame}:({value})")

        # Join the list into a string
        knob_values_str = ','.join(knob_values)
        knob_values_str = knob_values_str.replace(' ', '').replace('[', '').replace(']', '').replace("'", "")

        # Return only the string, not the tuple
        #print(knob_values_str)
        #print("CAM KEYFRAMES OUT")
        return knob_values_str

def keyframes(knob):
    if not isinstance(knob, nuke.Knob):  # Check if the object is not a knob
        return knob  # If it's not a knob, just return the object itself

    if knob.isAnimated():  # Check if the knob is animated
        curve = knob.animation(0)
        keyframes = []
        for kp in curve.keys():
            time = int(kp.x)
            value = kp.y
            frame = f"{time}:({value})"
            keyframes.append(frame)
        keyframes_str = ','.join(keyframes)
        keyframes_str = keyframes_str.replace(' ', '').replace('[', '').replace(']', '').replace("'", "")
        return keyframes_str
        
    else:
        return f"0:({knob.value()})"

interpolate_prompts = nuke.thisNode().knob('interpolate_prompts').value()
stability_key = nuke.thisNode().knob('api-key').value()

animation_prompts_str = nuke.thisNode().knob('animation_prompts').getValue()
animation_prompts = {int(k): v for k, v in json.loads(animation_prompts_str).items()}
negative_prompt = nuke.thisNode().knob('negative_prompt').getValue()
negative_prompt_weight = nuke.thisNode().knob('negative_prompt_weight').value()

width = int(nuke.thisNode().knob('hwh').value())
height = int(nuke.thisNode().knob('hww').value())
sampler = nuke.thisNode().knob('sampler').value()
model = nuke.thisNode().knob('anim_engine_name').value()


custom_model = ""
seed = int(nuke.thisNode().knob('seed').value())
cfg_scale = nuke.thisNode().knob('cfg_scale').getValue()
clip_guidance = nuke.thisNode().knob('clip_guidance').value()
preset = nuke.thisNode().knob('anim_style_preset').value()

animation_mode = nuke.thisNode().knob('animation_mode').value()
max_frames = int(nuke.thisNode().knob('max_frames').value())
border = nuke.thisNode().knob('border').value()
noise_add_curve = keyframes(nuke.thisNode().knob('noise_add_curve'))
noise_scale_curve = keyframes(nuke.thisNode().knob('noise_scale_curve'))
strength_curve = keyframes(nuke.thisNode().knob('strength_curve'))
steps_curve = keyframes(nuke.thisNode().knob('steps_curve'))
steps_strength_adj = nuke.thisNode().knob('steps_strength_adj').value()
interpolate_prompts = nuke.thisNode().knob('interpolate_prompts').value()
locked_seed = nuke.thisNode().knob('locked_seed').value()

angle = keyframes(nuke.thisNode().knob('angle'))
zoom = keyframes(nuke.thisNode().knob('zoom'))
translation_x = cam_keyframes(nuke.thisNode().knob("translate"),0)
translation_y = cam_keyframes(nuke.thisNode().knob("translate"),1)
translation_z = cam_keyframes(nuke.thisNode().knob("translate"),2)
rotation_x = cam_keyframes(nuke.thisNode().knob("rotate"),0)
rotation_y = cam_keyframes(nuke.thisNode().knob("rotate"),1)
rotation_z = cam_keyframes(nuke.thisNode().knob("rotate"),2)

diffusion_cadence_curve = keyframes(nuke.thisNode().knob('diffusion_cadence_curve'))
cadence_interp = nuke.thisNode().knob('cadence_interp').value()
cadence_spans = nuke.thisNode().knob('cadence_spans').value()

color_coherence = nuke.thisNode().knob('color_coherence').value()
brightness_curve = keyframes(nuke.thisNode().knob('brightness_curve'))
contrast_curve = keyframes(nuke.thisNode().knob('contrast_curve'))
hue_curve = keyframes(nuke.thisNode().knob('hue_curve'))
saturation_curve = keyframes(nuke.thisNode().knob('saturation_curve'))
lightness_curve = keyframes(nuke.thisNode().knob('lightness_curve'))
color_match_animate = nuke.thisNode().knob('color_match_animate').value()

depth_model_weight = nuke.thisNode().knob('depth_model_weight').value()
near_plane = nuke.thisNode().knob('near_plane').value()
far_plane = nuke.thisNode().knob('far_plane').value()
fov_curve = keyframes(nuke.thisNode().knob('fov_curve'))
depth_blur_curve = keyframes(nuke.thisNode().knob('depth_blur_curve'))
depth_warp_curve = keyframes(nuke.thisNode().knob('depth_warp_curve'))
save_depth_maps = nuke.thisNode().knob('save_depth_maps').value()

camera_type = nuke.thisNode().knob('camera_type').value()
render_mode = nuke.thisNode().knob('render_mode').value()
mask_power = nuke.thisNode().knob('mask_power').value()

use_inpainting_model = nuke.thisNode().knob('use_inpainting_model').value()
inpaint_border = nuke.thisNode().knob('inpaint_border').value()
mask_min_value = keyframes(nuke.thisNode().knob('mask_min_value'))
mask_binarization_thr = nuke.thisNode().knob('mask_binarization_thr').value()
save_inpaint_masks = nuke.thisNode().knob('save_inpaint_masks').value()
init_image = nuke.thisNode().knob('init_image').value()
init_sizing = nuke.thisNode().knob('init_sizing').value()
mask_path = nuke.thisNode().knob('mask_path').value()
mask_invert = nuke.thisNode().knob('mask_invert').value()
video_init_path = nuke.thisNode().knob('video_init_path').value()
extract_nth_frame = int(nuke.thisNode().knob('extract_nth_frame').value())
video_mix_in_curve = keyframes(nuke.thisNode().knob('video_mix_in_curve'))
video_flow_warp = nuke.thisNode().knob('video_flow_warp').value()

fps = nuke.thisNode().knob('fps').value()
reverse = nuke.thisNode().knob('reverse').value()

if model in ['stable-diffusion-xl-1024-v0-9', 'stable-diffusion-xl-1024-v1-0']:
    nuke.toNode('Switch2')["which"].setValue(1)
else:
    nuke.toNode('Switch2')["which"].setValue(0)

if nuke.thisNode().knob('animation_mode').value() == 'Video Input'and nuke.thisNode().input(0) is not None and nuke.thisNode()['video_init_path'].value() == "" or nuke.thisNode().knob('use_video_input').value()==True:
    ff = int(nuke.thisNode()['video_input_first_frame'].value())
    lf = int(nuke.thisNode()['video_input_last_frame'].value())
    nuke.toNode('write_init_stable_animation_frames')['file'].fromUserText(f"{temp_frames_dir}/stable_animation_frames_v{version:03d}.mp4")
    nuke.toNode('write_init_stable_animation_frames')['file_type'].setValue("mov")
    nuke.toNode('write_init_stable_animation_frames')['mov64_codec'].setValue("h264")
    nuke.toNode('write_init_stable_animation_frames')['mov64_fps'].setValue(fps)
    nuke.execute(nuke.toNode('write_init_stable_animation_frames'), start=ff, end=lf)
    nuke.thisNode()['video_init_path'].setValue(nuke.toNode('write_init_stable_animation_frames')['file'].value())
elif nuke.thisNode().knob('animation_mode').value() == 'Video Input' and nuke.thisNode().knob('use_video_input').value()==True:
    raise nuke.message("Please connect a video to the Image input or change the Animation mode.")

if nuke.thisNode().input(0) is not None and nuke.thisNode()['init_image'].value() == "" or nuke.thisNode().knob('use_init_img_input').value()==True:
    f = int(nuke.thisNode()['init_image_frame'].value())
    nuke.toNode('write_init_sa_init_image')['file'].fromUserText(f"{temp_frames_dir}/stable_animation_init_img_v{version:03d}.png")
    nuke.execute(nuke.toNode('write_init_sa_init_image'), start=f, end=f)
    nuke.thisNode()['init_image'].setValue(nuke.toNode('write_init_sa_init_image')['file'].value())
elif nuke.thisNode().knob('animation_mode').value() != 'Video Input' and nuke.thisNode().knob('use_init_img_input').value()==True:
    raise nuke.message("Please connect a video to the Image input or change the Animation mode.")

if nuke.thisNode().input(1) is not None and nuke.thisNode()['use_inpainting_model'].value():
    nuke.toNode('write_init_stable_animation_mask_frames')['file'].fromUserText(f"{temp_mask_dir}/stable_animation_mask_frames_{version:03d}.mp4")
    nuke.toNode('write_init_stable_animation_mask_frames')['file_type'].setValue("mov")
    nuke.toNode('write_init_stable_animation_mask_frames')['mov64_codec'].setValue("h264")
    nuke.toNode('write_init_stable_animation_mask_frames')['mov64_fps'].setValue(fps)
    nuke.execute(nuke.toNode('write_init_stable_animation_mask_frames'), start=0, end=max_frames)
    nuke.thisNode()['mask_path'].setValue(nuke.toNode('write_init_stable_animation_mask_frames')['file'].value())



STABILITY_HOST = "grpc.stability.ai:443"
STABILITY_KEY = nuke.thisNode().knob('api-key').value()

context = api.Context(STABILITY_HOST, STABILITY_KEY)

args = AnimationArgs()

args.interpolate_prompts = interpolate_prompts

args.width = width
args.height = height
args.sampler = sampler
args.model = model


args.custom_model = custom_model

args.cfg_scale = cfg_scale
args.clip_guidance = clip_guidance
args.init_image = nuke.thisNode().knob('init_image').value()
args.init_sizing = init_sizing
args.mask_path = mask_path
args.mask_invert = mask_invert
args.preset = preset
args.animation_mode = animation_mode

args.border = border
args.noise_add_curve = noise_add_curve
args.noise_scale_curve = noise_scale_curve

args.steps_curve = steps_curve
args.steps_strength_adj = steps_strength_adj

args.angle = angle
args.zoom = zoom
args.translation_x = translation_x
args.translation_y = translation_y
args.translation_z = translation_z
args.rotation_x = rotation_x
args.rotation_y = rotation_y
args.rotation_z = rotation_z

args.cadence_spans = cadence_spans
args.color_coherence = color_coherence
args.brightness_curve = brightness_curve
args.contrast_curve = contrast_curve
args.hue_curve = hue_curve
args.saturation_curve = saturation_curve
args.lightness_curve = lightness_curve
args.color_match_animate = color_match_animate
args.depth_model_weight = depth_model_weight
args.near_plane = near_plane
args.far_plane = far_plane
args.fov_curve = fov_curve
args.depth_blur_curve = depth_blur_curve
args.depth_warp_curve = depth_warp_curve
args.save_depth_maps = save_depth_maps
args.camera_type = camera_type
args.render_mode = render_mode
args.mask_power = mask_power

args.use_inpainting_model = use_inpainting_model
args.inpaint_border = inpaint_border
args.mask_min_value = mask_min_value
args.mask_binarization_thr = mask_binarization_thr
args.save_inpaint_masks = save_inpaint_masks

args.extract_nth_frame = extract_nth_frame
args.video_mix_in_curve = video_mix_in_curve
args.video_flow_warp = video_flow_warp

args.interpolate_prompts = interpolate_prompts
args.locked_seed = locked_seed
args.max_frames = max_frames
args.seed = seed
args.strength_curve = strength_curve
args.diffusion_cadence_curve = diffusion_cadence_curve
args.cadence_interp = cadence_interp
args.video_init_path = nuke.thisNode().knob('video_init_path').value()

# Create Animator object to orchestrate the rendering
animator = Animator(
    api_context = context,
    animation_prompts = animation_prompts,
    negative_prompt = negative_prompt,
    negative_prompt_weight = negative_prompt_weight,
    args=args
)

try:
    # Create a ProgressTask
    progress_task = nuke.ProgressTask("Rendering frames")

    # Render each frame of animation
    idx = 1
    for idx, frame in enumerate(animator.render()):
        # Check if the user cancelled the operation or the global interrupt signal is set
        if progress_task.isCancelled():
            break
            raise Exception("Task cancelled by user")

        # Update the progress bar
        progress = int((idx / (max_frames-1)) * 100)  # Calculate progress percentage
        progress_task.setProgress(progress)

        # Save the frame in the versioned directory
        frame_path = os.path.join(os.sep, frames_dir, f"frame_{idx:05d}.png")

        # Update the message
        progress_task.setMessage(f"Rendering frame {idx + 1} of {max_frames}")

        frame.save(frame_path)

except Exception as e:
    print(str(e))

finally:
    del(progress_task)

# Create a Read node and load the frames
with nuke.root():
    read_node = nuke.createNode("Read", inpanel=False)
    read_node['file'].fromUserText(os.path.join(frames_dir, "frame_#####.png"))
    read_node['first'].setValue(0)
    read_node['last'].setValue(max_frames-1)
"""

    n.addKnob(nuke.PyScript_Knob("anim", "Dream", get_anim))

    n["anim"].setFlag(0x0000000000001000)

    #STABLE VIDEO TAB
    set_video_init_image = """
s = nuke.thisNode()

with s:
    no=nuke.toNode('sv_switch_output')
    no['which'].setValue(1)
    """
    
    n.addKnob(nuke.Tab_Knob("stable_video_tab", "Stable Video Diffusion"))    
    n.addKnob(nuke.PyCustom_Knob("sv_logo", "", "logo(nuke.thisNode())"))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Text_Knob("link"," ",'<a href="https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt"><span  style="color:#ffb936;font-size:8pt;">This model is for research purposes only. Read license<span style="color:#504eaa;"></a>'))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.PyScript_Knob("set_video_init_image_btn", "Preview Init Image", set_video_init_image)) 
    n.addKnob(nuke.Text_Knob(""))  
    n.addKnob(nuke.BeginTabGroup_Knob())
    n.addKnob(nuke.Tab_Knob('svd_setting', 'Settings'))
    n.addKnob(sv_format)
    n.addKnob(nuke.Int_Knob('sv_seed', 'Seed'))
    n['sv_seed'].setValue(0)
    n.addKnob(nuke.Double_Knob('sv_cfg_scale', 'Cfg Scale'))
    n['sv_cfg_scale'].setValue(2.5)  
    n.addKnob(nuke.Int_Knob('motion_bucket', 'Motion Bucket ID'))
    n['motion_bucket'].setValue(40)
    n.addKnob(nuke.EndTabGroup_Knob())
    
    get_video = """
import nuke
import os
import requests
import http.client
import mimetypes
import json
import time

sv_api_key = nuke.thisNode().knob('api-key').value()
sv_seed = nuke.thisNode().knob('sv_seed').value()
sv_cfg_scale = nuke.thisNode().knob('sv_cfg_scale').value()
motion_bucket = nuke.thisNode().knob('motion_bucket').value()

try:
    # Get the directory of the current Nuke script
    script_dir = os.path.dirname(nuke.root().name()).replace('/', os.sep)
    print(script_dir)
    # Set the subdirectory where the image files will be stored
    sub_dir = "Stability"
    # Set the directories where the image files and temp files will be stored
    video_dir = os.path.join(os.sep, script_dir, sub_dir, "stable_video")
    print(video_dir)
    video_temp = os.path.join(os.sep, script_dir, video_dir, "stable_video_temp")
    # Create the directories if they don't exist
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(video_temp, exist_ok=True)

except OSError as e:
    raise Exception("Please ensure that the Nuke script is saved and that you have write permissions in the directory where the script is saved.")

# Define the script name
script_name = os.path.splitext(os.path.basename(nuke.root().name()))[0]

# Define the base name for the video
init_img_video_base_name = f"{script_name}_init_img_stable_video"

# Define the initial video path
init_img_video_path = os.path.join(os.sep, video_temp, f"{init_img_video_base_name}_v001.png")

# Version up if a video already exists at the location
version = 1
while os.path.exists(init_img_video_path):
    version += 1
    init_img_video_path = os.path.join(os.sep, video_temp, f"{init_img_video_base_name}_v00{version}.png")

nuke.toNode('write_init_stable_video_image')['file'].fromUserText(init_img_video_path)
nuke.execute(nuke.toNode('write_init_stable_video_image'), start=1, end=1)

with nuke.thisNode():
    img_path = nuke.toNode('write_init_stable_video_image')['file'].value()


# Open the image file in binary mode
with open(img_path, 'rb') as img_file:
    img_data = img_file.read()

url = "https://api.stability.ai/v2alpha/generation/image-to-video"

payload = {
    'image': ('image.png', img_data, 'image/png'),
    'seed': (None, str(sv_seed)),
    'cfg_scale': (None, str(sv_cfg_scale)),
    'motion_bucket_id': (None, str(motion_bucket))
}

headers = {
    'authorization': f"Bearer {sv_api_key}"
}

response = requests.post(url, files=payload, headers=headers)

print(response.text)

# Convert the response text into a JSON object
response_json = json.loads(response.text)

id = response_json['id']

#msg = nuke.ProgressTask("Generating video")
import http.client

conn = http.client.HTTPSConnection("api.stability.ai")

while True:
    conn.request("GET", f"/v2alpha/generation/image-to-video/result/{id}", headers=headers)
    res = conn.getresponse()
    data = res.read()

    # Try to decode the data as a string and load it into a JSON object
    try:
        data_str = data.decode("utf-8")
        data_json = json.loads(data_str)
    except (UnicodeDecodeError, json.JSONDecodeError):
        # If the data cannot be decoded as a string and loaded into a JSON object,
        # treat it as binary data

        script_name = os.path.splitext(os.path.basename(nuke.root().name()))[0]

        # Define the base name for the video
        video_base_name = f"{script_name}_stable_video"

        # Define the initial video path
        video_path = os.path.join(os.sep, video_dir, f"{video_base_name}_v001.mp4")

        # Version up if a video already exists at the location
        version = 1
        while os.path.exists(video_path):
            version += 1
            video_path = os.path.join(os.sep, video_dir, f"{video_base_name}_v00{version}.mp4")
            
        # Save the video to 'video_dir'
        with open(video_path, 'wb') as f:
            f.write(data)
        #print(f"Generation complete, data saved to '{video_path}'")

        # Create a read node in Nuke to open the video
        read_node = video_path.replace(os.sep, "/")
        video = nuke.createNode("Read",inpanel=False)
        video["file"].fromUserText(read_node) 

        break
    else:
        # If the data can be decoded as a string and loaded into a JSON object,
        # treat it as a status update
        if data_json['status'] == 'complete':
            print("Generation complete!")
            break
        else:
            #nuke.message("Generating video")
            time.sleep(5)

"""
    
    n.addKnob(nuke.PyScript_Knob("video", "Dream", get_video))
    n["video"].setFlag(0x0000000000001000)
    
    #ACCOUNT TAB
    account_details = """import os
import requests

api_host = os.getenv('API_HOST', 'https://api.stability.ai')

# Get user account details
url_account = f"{api_host}/v1/user/account"
sv_api_key = nuke.thisNode().knob('api-key').value()
if sv_api_key is None:
    raise Exception("Missing Stability API key.")

response_account = requests.get(url_account, headers={
    "Authorization": f"Bearer {sv_api_key}"
})

if response_account.status_code != 200:
    raise Exception("Non-200 response: " + str(response_account.text))

# Extract required fields from the payload
payload_account = response_account.json()
email = payload_account.get('email')
profile_picture = payload_account.get('profile_picture')

# Get user balance details
url_balance = f"{api_host}/v1/user/balance"
response_balance = requests.get(url_balance, headers={
    "Authorization": f"Bearer {sv_api_key}"
})

if response_balance.status_code != 200:
    raise Exception("Non-200 response: " + str(response_balance.text))

# Extract 'credits' from the payload
payload_balance = response_balance.json()
credits = "{:.1f}".format(payload_balance.get('credits'))

# Now you can use the extracted values
nuke.thisNode().knob('email').setValue(email)
nuke.thisNode().knob('credits').setValue(str(credits))

    """
    
    n.addKnob(nuke.Tab_Knob("account", "Account"))
    n.addKnob(nuke.PyCustom_Knob("acc_logo", "", "logo(nuke.thisNode())"))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.PyScript_Knob("account_details", "Update Account Details", account_details)) 
    n.addKnob(nuke.Text_Knob("email","Email:","your@email.com"))
    n.addKnob(nuke.Text_Knob("credits","Credits:","0"))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.BeginTabGroup_Knob())
    n.addKnob(nuke.Tab_Knob('acc_setting', 'Settings'))  
    n.addKnob(nuke.Text_Knob("link"," ",'<a href="https://platform.stability.ai/docs/getting-started/authentication"><span  style="color:#ffb936;font-size:8pt;">Get your Stability API key<span style="color:#504eaa;"></a>'))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.String_Knob("api-key","API key", ''))
    n.addKnob(nuke.Text_Knob(""))
    n.addKnob(nuke.Text_Knob("sdinfo", " ",'<span  style="color:#fbeee3;font-weight:bold;font-size:8pt;">STABLE<span style="color:#fc4026;">DIFFUSION</span></span><span style="color:#aaa;font-family:sans-serif;font-size:8pt"> - Version 2.0 - 2024 - <a href="https://github.com/besarismaili/Stable-Diffusion-for-NUKE" style="color:#aaa">Github Page</a></span><p><a href="https://www.linkedin.com/in/besarismaili/" style="color:#aaa">Besar Ismaili</a> </p>'))
    n.addKnob(nuke.Text_Knob(""))
    n['text-to-image'].setFlag(0)
    

ui()