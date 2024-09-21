from obsidian_to_hugo import ObsidianToHugo
import shutil
import os
import re


def process_images_in_content(file_contents: str, obsidian_assets_dir: str, hugo_images_dir: str) -> str:
    """
    Process image links in the markdown content.
    
    :param file_contents: The contents of the markdown file as a string.
    :param obsidian_assets_dir: Directory in Obsidian where assets (images) are stored.
    :param hugo_images_dir: Directory in Hugo where images will be copied.
    :return: Processed markdown content with updated image links.
    """
    # Regex to match Obsidian-style image links ![[image.png]]
    image_pattern = re.compile(r"!\[\[(.*?)\]\]")

    # Find all image references in the markdown content
    image_references = image_pattern.findall(file_contents)

    if image_references:
        # Ensure the Hugo images directory exists
        os.makedirs(hugo_images_dir, exist_ok=True)

        for image_name in image_references:
            image_src = os.path.join(obsidian_assets_dir, image_name)

            if os.path.exists(image_src):
                # Copy the image to the Hugo images directory
                image_dest = os.path.join(hugo_images_dir, image_name)
                shutil.copy(image_src, image_dest)

                # Update the markdown reference to the new image path in Hugo
                new_image_path = f"/images/{image_name}"
                file_contents = file_contents.replace(f"![[{image_name}]]", '{{ $image := resources.Get ' + f'"{new_image_path}"' + '}}')

    return file_contents

def process_file(file_contents: str) -> str:
    """
    Custom processor to modify file contents.
    """
    # Directory paths for Obsidian assets and Hugo images
    obsidian_assets_dir = os.path.join(os.getcwd(), 'obsidian', 'assets')
    hugo_images_dir = os.path.join(os.getcwd(), 'blog', 'content', 'images')

    # Process images within the file contents
    processed_contents = process_images_in_content(file_contents, obsidian_assets_dir, hugo_images_dir)

    return processed_contents

def main():
    cwd = os.getcwd()

    obsidian_to_hugo = ObsidianToHugo(
        obsidian_vault_dir=os.path.join(cwd, 'obsidian'),
        hugo_content_dir=os.path.join(cwd, 'blog', 'content'),
        processors=[process_file]
    )

    obsidian_to_hugo.run()

if __name__ == "__main__":
    main()
