# Local Project Structure Generator

A simple, clean Streamlit app to visualize and share your project folder structure without the hassle.

## Why I Built This

I was **very much annoyed** of using and explaining the code structure of any folder and project of mine to others and specifically to AI for reasons 😉 ifykyk.

Every single time I needed to share my project structure with someone or paste it into an AI chat, I had to:

- Manually type out the folder tree
- Use clunky CLI tools
- Copy-paste broken formatting
- Spend 10 minutes on something that should take 10 seconds

This tool solved that problem in the most straightforward way possible. Now I just:

1. Open the app
2. Select my folder
3. Deselect what I don't need
4. Copy the clean tree structure

**Time saved: countless hours of frustration.**

## What It Does

This Streamlit app scans any local folder on your machine and generates a clean, visual tree structure. You can:

- **Browse** your entire project structure with an interactive tree view
- **Select/Deselect** specific files and folders you want to include
- **Select All / Deselect All** with one click for quick filtering
- **Copy** the resulting tree structure as clean, formatted text
- **Share** your folder structure with teammates, documentation, or AI assistants

The output is a perfect ASCII tree that looks like this:

```
StructuredFolder/
├── main.py
├── README.md
├── requirements.txt
```

## Features

- **Automatic folder scanning** - Just paste your folder path
- **Interactive tree selection** - Check/uncheck files and folders
- **Smart folder handling** - Checking a folder automatically includes all its contents
- **Clean output** - Properly formatted ASCII tree structure
- **No hidden files** - Automatically filters out `.git`, `.env`, and other hidden items
- **Zero configuration** - Works out of the box

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Adityarya/structuredFolder.git
cd structuredFolder
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

## Usage

### Basic Usage

1. **Launch the app** - Run `streamlit run app.py` in your terminal
2. **Enter folder path** - Type or paste the path to your project folder
3. **Select files** - Use the interactive tree to check/uncheck items
4. **Copy output** - The right panel shows your clean tree structure ready to copy

### Quick Actions

- **Select All** - Click to include everything in your folder
- **Deselect All** - Click to start fresh and manually pick items
- **Re-check folders** - Checking a folder automatically includes all its children

### Tips for Best Results

- Start with "Select All" and then remove what you don't need
- Hidden files (starting with `.`) are automatically excluded
- Use this for README documentation, AI prompts, or team collaboration
- The output is plain text - perfect for copying into markdown, chat, or docs

## Requirements

```
streamlit
streamlit-tree-select
```

Create a `requirements.txt` file with the above dependencies.

## UX Highlights

The interface is designed to be **dead simple**:

- **Left panel**: Interactive tree where you select what you want
- **Right panel**: Live preview of your formatted structure
- **Two-click workflow**: Select folder → Copy result

No configuration files. No complex settings. No learning curve.

## Contributing

I'm grateful if you use this script! If something breaks or you have ideas for features to add, please:

- Open an issue describing the problem or suggestion
- Submit a pull request with improvements
- Let me know what you think

I just needed to manage my folder structure and hence created this simple Streamlit project. If it helps you too, that's awesome!

## License

Fiir se generate kar diya ChatGPT yeh License wagerah, Arre open hai bhai!

---

**Made with frustration turned into productivity**

If this saves you time, consider giving it a Star on GitHub! Agar mann hai toh =).
