# Streamlit Even Easier Web Lunch (SEEWL)

Make a website from Markdown files. No Python editing or configuration required.

## Quick start

Requires **Python 3.12 or newer**. Open a terminal in this project's folder.

### 1. Install once

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` instead of `source .venv/bin/activate`.

### 2. Start the website

```sh
python -m streamlit run Application/main.py
```

Open the local address printed in the terminal, usually `http://localhost:8501`.
The included homepage works immediately. Press `Ctrl+C` in the terminal to stop.
For later sessions, activate the same virtual environment and run the start command again.

### 3. Make it yours

Replace the text in `Application/pages/Home.md` with your own Markdown and refresh the browser.
Save another `.md` file in `Application/pages/` to add another page.

```text
Application/
  main.py
  config.json       # Optional settings
  pages/
    Home.md         # Your content
    About Me.md     # An optional second page
```

- One page displays directly, without a page selector.
- Multiple pages get automatic sidebar navigation.
- Pages appear alphabetically by filename, ignoring case; the first page opens initially.
- Spaces and underscores are supported. Underscores become spaces in navigation labels.
- If labels would be identical, navigation shows the original filenames so each page remains distinct.
- Only Markdown files directly inside the pages folder are used; other files and subfolders are ignored.
- Save Markdown files as UTF-8.

## Optional customization

Keep, edit, or remove `Application/config.json`. Missing settings use defaults, so a title change needs only:

```json
{
  "application": {
    "applicationName": "My Site"
  }
}
```

| Setting | Default | Purpose |
| --- | --- | --- |
| `application.applicationName` | `My Website` | Browser-tab title and navigation title |
| `application.pageIcon` | Globe icon | Streamlit browser-tab icon |
| `application.layout` | `wide` | `wide` or `centered` |
| `application.initialSidebarState` | `expanded` | `auto`, `expanded`, or `collapsed` |
| `deployRules.pagesFolderAddress` | `pages` | Folder containing your Markdown files |

Relative page-folder paths are resolved from `Application/`, not from the terminal's working directory.
Absolute folder paths also work. The configuration file is always read beside `main.py`.

If the page folder is missing or empty, the website tells you where to add content.
Invalid configuration and unreadable Markdown show an error on the page instead of continuing with broken data.
Fix the reported file and refresh; removing `config.json` restores the defaults.
