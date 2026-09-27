# OnboardFlow

OnboardFlow is a Python static-site generator that consumes a `repo_blueprint.json`
file — produced by an automated pipeline — and renders it into a self-contained,
shareable HTML architecture tour page. The page covers project metadata, the live
Mermaid architecture diagram, execution flow, data models, API endpoints, and a
setup playbook, all in a single file you can open in a browser or host on GitHub Pages.

## Quick start

```bash
# 1. Install dependencies (none yet beyond stdlib — will grow as the renderer is built)
python --version   # requires >= 3.10

# 2. Drop your blueprint file into fixtures/
cp path/to/your/repo_blueprint.json fixtures/callbridge.json

# 3. Generate the tour page
python visualizer.py

# 4. Open the result
start output/architecture_tour.html   # Windows
# open output/architecture_tour.html  # macOS
```

Override defaults with flags:

```bash
python visualizer.py \
  --blueprint fixtures/my_project.json \
  --template  template.html \
  --output    output/my_project.html
```

The generated file at `output/architecture_tour.html` is committed to this repo and
served via GitHub Pages at:
`https://<your-username>.github.io/<repo-name>/output/architecture_tour.html`
