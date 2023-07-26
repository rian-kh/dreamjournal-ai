# From https://huggingface.co/docs/diffusers/optimization/mps


from diffusers import DiffusionPipeline

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


prompt = "orange cat"

_ = pipe(prompt, num_inference_steps=1)

image = pipe(prompt).images[0]
image.save("output.png")