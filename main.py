import os
import random
from PIL import Image, ImageSequence
from quickdraw import QuickDrawData,QuickDrawDataGroup
from moviepy.editor import VideoFileClip

qd = QuickDrawData()
current_dir = os.getcwd()

def qd_gif(category, country='MY', current_dir=current_dir, qty=None, seed=None):
    """
    Fetches gif drawings from QuickDraw dataset for a specified category & country,
    Returns a list of file paths to the saved GIFs.
    """

    # Create a QuickDrawDataGroup for the specified category
    category_gp = QuickDrawDataGroup(category, max_drawings=None)
    
    # Search for drawings from selected country
    category_my = category_gp.search_drawings(countrycode=country)
    
    # Limit the number of drawings if qty is specified
    if qty is not None:
        if seed is not None:
            try:
                random.seed(int(seed))  # Ensure seed is an integer
            except (ValueError, TypeError):
                raise ValueError(f"Invalid seed value: {seed}. Seed must be a number or None.")
            
            if qty < len(category_my):
                category_my = random.sample(category_my, qty)
            else:
                category_my = category_my[:qty]
        else:
            # No seed: just take the first {qty}
            category_my = category_my[:qty]

    # Create directory if it doesn't exist
    save_dir = os.path.join(current_dir, "quick draw", category)
    os.makedirs(save_dir, exist_ok=True)
    
    gif_paths = []
    # Save each drawing as a GIF
    for index, drawing in enumerate(category_my, start=1):
        file_name = os.path.join(save_dir, f"{category}{index}.gif")
        if not os.path.exists(file_name):
            drawing.animation.save(file_name)
        gif_paths.append(file_name)
    
    print(f'{len(gif_paths)} GIFs saved in {save_dir}')
    return gif_paths


def qd_vid(category, country='MY',ratio='sq',seed=None):
    """
    Fetches video drawings from QuickDraw dataset for a specified category.
    Fetch a specific number of drawing based on the ratio
    sq: 10:10, 100
    st: 9:16, 144
    ls: 16:9, 144

    Compile the multiple gifs into a video file, corresponding to the ratio.
    """

    if ratio == 'sq':
        qty = 100
        grid_size = (10, 10)
    elif ratio == 'st':
        qty = 144
        grid_size = (9, 16)
    elif ratio == 'ls':
        qty = 144
        grid_size = (16, 9)
    else:
        raise ValueError("Invalid ratio. Use 'sq', 'st', or 'ls'.")

    gif_list = qd_gif(category,country,current_dir,qty,seed)
    gifs = [Image.open(gif) for gif in gif_list]

    # Iniaite grid, assuming all gifs have the same size
    gif_width, gif_height = gifs[0].size
    grid_width = gif_width * grid_size[0]
    grid_height = gif_height * grid_size[1]

    # Get the maximum number of frames in the GIfs from the file list
    max_frames = max(gif.n_frames for gif in gifs)

        # Create a list to store each frame of the grid
    grid_frames = []

    for frame_index in range(max_frames):
        # Create a new image for each frame
        grid_image = Image.new("RGBA", (grid_width, grid_height))
        
        for idx, gif in enumerate(gifs):
            x = (idx % grid_size[0]) * gif_width
            y = (idx // grid_size[0]) * gif_height
            
            try:
                # Select the frame
                gif.seek(frame_index)
            except EOFError:
                # If the gif has fewer frames, keep the last frame
                gif.seek(gif.n_frames - 1)
                
            grid_image.paste(gif, (x, y))
        
        grid_frames.append(grid_image)
    
    # Save all frames as a new GIF with appropriate durations
    output_path = os.path.join(current_dir, "quick draw", f"{category}_{country}_{ratio}.gif")
    grid_frames[0].save(output_path, save_all=True, append_images=grid_frames[1:], loop=0, duration=100)
    print(f'GIF video saved at {output_path}')

    # Convert GIF to video using moviepy
    video_path = os.path.join(current_dir, "quick draw", f"{category}_{country}_{ratio}.mp4")
    clip = VideoFileClip(output_path)
    print(f'Converting GIF to video: {output_path}')
    clip.write_videofile(video_path, codec='libx264')
    print(f'Gif converted to video at: {video_path}')

qd_vid('star','MY','sq')