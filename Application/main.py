import json
from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent


def load_config(config_file):
    config = {
        "application": {
            "applicationName": "My Website",
            "pageIcon": "🌐",
            "layout": "wide",
            "initialSidebarState": "expanded",
        },
        "deployRules": {"pagesFolderAddress": "pages"},
    }
    try:
        overrides = json.loads(config_file.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return config
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"Cannot read {config_file}: {exc}. "
            "Fix the file or remove it to use the default settings."
        ) from exc

    if not isinstance(overrides, dict):
        raise ValueError(f"{config_file} must contain a JSON object.")

    for section, defaults in config.items():
        values = overrides.get(section, {})
        if not isinstance(values, dict):
            raise ValueError(f"'{section}' in {config_file} must be a JSON object.")
        for key in defaults:
            if key in values:
                value = values[key]
                if not isinstance(value, str) or not value.strip():
                    raise ValueError(
                        f"'{section}.{key}' in {config_file} must be a non-empty string."
                    )
                defaults[key] = value

    application = config["application"]
    if application["layout"] not in ("wide", "centered"):
        raise ValueError("'application.layout' must be 'wide' or 'centered'.")
    if application["initialSidebarState"] not in ("auto", "expanded", "collapsed"):
        raise ValueError(
            "'application.initialSidebarState' must be 'auto', 'expanded', or 'collapsed'."
        )
    return config


def main():
    try:
        config = load_config(APP_DIR / "config.json")
    except ValueError as exc:
        st.error(str(exc))
        st.stop()

    application = config["application"]
    st.set_page_config(
        page_title=application["applicationName"],
        page_icon=application["pageIcon"],
        layout=application["layout"],
        initial_sidebar_state=application["initialSidebarState"],
    )

    pages_dir = APP_DIR / config["deployRules"]["pagesFolderAddress"]
    try:
        pages = sorted(
            (
                page
                for page in pages_dir.iterdir()
                if page.is_file() and page.suffix.lower() == ".md"
            ),
            key=lambda page: (page.name.casefold(), page.name),
        )
    except OSError as exc:
        st.error(
            f"Cannot open the pages folder {pages_dir}: {exc}. "
            "Create that folder and add a Markdown (.md) file."
        )
        st.stop()

    if not pages:
        st.info(f"Add a Markdown (.md) file to {pages_dir}, then refresh this page.")
        st.stop()

    selected_page = pages[0]
    if len(pages) > 1:
        labels = [page.stem.replace("_", " ") for page in pages]
        if len(set(labels)) != len(labels):
            labels = [page.name for page in pages]
        page_labels = dict(zip(pages, labels))
        st.sidebar.title(application["applicationName"])
        selected_page = st.sidebar.selectbox(
            "Page", options=pages, format_func=page_labels.__getitem__
        )

    try:
        content = selected_page.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        st.error(f"Cannot read {selected_page}: {exc}. Save it as a UTF-8 Markdown file.")
        st.stop()
    st.markdown(content)


if __name__ == "__main__":
    main()