
from flask import Flask, request, jsonify, send_file
from diffusers import DiffusionPipeline
from io import BytesIO


ipv4 = "your-ipv4"
port = 5000

# Stable Diffusion setup
pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("mps")
pipe.enable_attention_slicing()

# Get rid of safety filter, from https://github.com/CompVis/stable-diffusion/issues/331#issuecomment-1562198856
def disabled_safety_checker(images, clip_input):
    if len(images.shape) == 4:
        num_images = images.shape[0]
        return images, [False]*num_images
    else:
        return images, False
    
pipe.safety_checker = disabled_safety_checker


# Server setup
app = Flask(__name__)
isGenerating = False

@app.route("/")
def generateImage():
    global isGenerating

    # Exit if a generation is in progress
    if (isGenerating):
      print("Generation in progress, new generation ignored")
      return jsonify({"error":"Generation in progress"})

    prompt = request.headers.get("prompt")
   
    if (prompt):
        
        print("Generating from prompt:", prompt)
        isGenerating = True
        _ = pipe(prompt, num_inference_steps=1)

        image = pipe(prompt).images[0]
        
        # Respond with image, from https://stackoverflow.com/a/11017839/21809626
        buff = BytesIO()
        image.save(buff, format="PNG")
        buff.seek(0)
        
        isGenerating = False
        return send_file(buff, mimetype='image/png')
    
    else:
        print("No prompt given")
        return jsonify({"error":"No prompt given"})



app.run(host=ipv4, port=port)