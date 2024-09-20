from obsidian_to_hugo import ObsidianToHugo
import os


def main():
    cwd = os.getcwd()

    obsidian_to_hugo = ObsidianToHugo(
        obsidian_vault_dir=os.path.join(cwd, 'obsidian'),
        hugo_content_dir=os.path.join(cwd, 'blog', 'content')
    )

    obsidian_to_hugo.run()

if __name__ == "__main__":
    main()
