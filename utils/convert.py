from obsidian_to_hugo import ObsidianToHugo
import os


def main()
    pd = os.path.dirname(os.getcwd())

    obsidian_to_hugo = ObsidianToHugo(
        obsidian_vault_dir=os.path.join(pd, 'obsidian'),
        hugo_content_dir=os.path.join(pd, 'blog', 'content')
    )

    obsidian_to_hugo.run()

if __name__ == "__main__":
    main()
