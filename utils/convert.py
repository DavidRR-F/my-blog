from obsidian_to_hugo import ObsidianToHugo
import os
import re

def process_post_configuration(file_contents):
    config_pattern = r'\`\`\`config(.*?)\`\`\`'
    def replace_config_wrapper(match):
        config = match.group(1)
        return f'---{config}---'
    
    return re.sub(config_pattern, replace_config_wrapper, file_contents)


def process_image_tags(file_contents):
    image_folder = 'images'
    image_pattern = r'!\[(.*?)\]\(\{\{< ref "(.*?)" >\}\}\)'
        
    def replace_image_tag(match):
        filename = match.group(1)
        return f'![{filename}]({image_folder}/{filename})'

    processed_content = re.sub(image_pattern, replace_image_tag, file_contents)
    return processed_content if processed_content else file_contents

def main():
    cwd = os.getcwd()

    obsidian_to_hugo = ObsidianToHugo(
        obsidian_vault_dir=os.path.join(cwd, 'obsidian'),
        hugo_content_dir=os.path.join(cwd, 'blog', 'content'),
        processors=[process_image_tags, process_post_configuration]
    )

    obsidian_to_hugo.run()

if __name__ == "__main__":
    main()
