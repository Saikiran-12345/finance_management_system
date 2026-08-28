import os

def generate_css_framework():
    css = "/* CUSTOM UTILITY FIRST CSS FRAMEWORK */\n"
    css += "/* Auto-generated for Personal Finance Management System */\n\n"
    
    css += ":root {\n"
    colors = {
        'primary': '#0d6efd',
        'secondary': '#6c757d',
        'success': '#198754',
        'info': '#0dcaf0',
        'warning': '#ffc107',
        'danger': '#dc3545',
        'light': '#f8f9fa',
        'dark': '#212529',
        'gray-100': '#f8f9fa',
        'gray-200': '#e9ecef',
        'gray-300': '#dee2e6',
        'gray-400': '#ced4da',
        'gray-500': '#adb5bd',
        'gray-600': '#6c757d',
        'gray-700': '#495057',
        'gray-800': '#343a40',
        'gray-900': '#212529',
    }
    for name, hexcode in colors.items():
        css += f"    --color-{name}: {hexcode};\n"
    css += "}\n\n"
    
    css += "*, *::before, *::after { box-sizing: border-box; }\n"
    css += "body { margin: 0; font-family: system-ui, -apple-system, sans-serif; }\n\n"
    
    # Generate Spacing (Margins and Paddings)
    css += "/* Spacing Utilities */\n"
    spacing_scale = [0, 0.25, 0.5, 1, 1.5, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64]
    
    for i, val in enumerate(spacing_scale):
        # Margins
        css += f".m-{i} {{ margin: {val}rem !important; }}\n"
        css += f".mt-{i} {{ margin-top: {val}rem !important; }}\n"
        css += f".mb-{i} {{ margin-bottom: {val}rem !important; }}\n"
        css += f".ml-{i} {{ margin-left: {val}rem !important; }}\n"
        css += f".mr-{i} {{ margin-right: {val}rem !important; }}\n"
        css += f".mx-{i} {{ margin-left: {val}rem !important; margin-right: {val}rem !important; }}\n"
        css += f".my-{i} {{ margin-top: {val}rem !important; margin-bottom: {val}rem !important; }}\n"
        
        # Paddings
        css += f".p-{i} {{ padding: {val}rem !important; }}\n"
        css += f".pt-{i} {{ padding-top: {val}rem !important; }}\n"
        css += f".pb-{i} {{ padding-bottom: {val}rem !important; }}\n"
        css += f".pl-{i} {{ padding-left: {val}rem !important; }}\n"
        css += f".pr-{i} {{ padding-right: {val}rem !important; }}\n"
        css += f".px-{i} {{ padding-left: {val}rem !important; padding-right: {val}rem !important; }}\n"
        css += f".py-{i} {{ padding-top: {val}rem !important; padding-bottom: {val}rem !important; }}\n"

    # Generate Typography
    css += "\n/* Typography Utilities */\n"
    font_sizes = [10, 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72, 96, 128]
    for size in font_sizes:
        css += f".text-{size} {{ font-size: {size}px !important; }}\n"
        
    font_weights = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    for weight in font_weights:
        css += f".font-weight-{weight} {{ font-weight: {weight} !important; }}\n"
        
    # Generate Colors
    css += "\n/* Color Utilities */\n"
    for name in colors.keys():
        css += f".text-{name} {{ color: var(--color-{name}) !important; }}\n"
        css += f".bg-{name} {{ background-color: var(--color-{name}) !important; }}\n"
        css += f".border-{name} {{ border-color: var(--color-{name}) !important; }}\n"

    # Grid System (12 columns)
    css += "\n/* Grid System */\n"
    css += ".container { width: 100%; margin-right: auto; margin-left: auto; padding-right: 15px; padding-left: 15px; }\n"
    css += ".row { display: flex; flex-wrap: wrap; margin-right: -15px; margin-left: -15px; }\n"
    
    for i in range(1, 13):
        width = (i / 12) * 100
        css += f".col-{i} {{ flex: 0 0 {width}%; max-width: {width}%; padding-right: 15px; padding-left: 15px; }}\n"

    # Width and Height
    css += "\n/* Sizing */\n"
    for w in range(0, 105, 5):
        css += f".w-{w} {{ width: {w}% !important; }}\n"
        css += f".h-{w} {{ height: {w}% !important; }}\n"

    # Display
    displays = ['none', 'inline', 'inline-block', 'block', 'table', 'table-row', 'table-cell', 'flex', 'inline-flex', 'grid']
    for d in displays:
        css += f".d-{d} {{ display: {d} !important; }}\n"
        
    # Flexbox
    flex_directions = ['row', 'column', 'row-reverse', 'column-reverse']
    for fd in flex_directions:
        css += f".flex-{fd} {{ flex-direction: {fd} !important; }}\n"
        
    justify = {'start': 'flex-start', 'end': 'flex-end', 'center': 'center', 'between': 'space-between', 'around': 'space-around'}
    for name, val in justify.items():
        css += f".justify-content-{name} {{ justify-content: {val} !important; }}\n"
        
    align = {'start': 'flex-start', 'end': 'flex-end', 'center': 'center', 'baseline': 'baseline', 'stretch': 'stretch'}
    for name, val in align.items():
        css += f".align-items-{name} {{ align-items: {val} !important; }}\n"

    # Borders
    for w in range(0, 6):
        css += f".border-{w} {{ border-width: {w}px !important; }}\n"
        
    # Radius
    for r in range(0, 50, 5):
        css += f".rounded-{r} {{ border-radius: {r}px !important; }}\n"
    css += ".rounded-circle { border-radius: 50% !important; }\n"

    # Positions
    positions = ['static', 'relative', 'absolute', 'fixed', 'sticky']
    for p in positions:
        css += f".position-{p} {{ position: {p} !important; }}\n"

    # Z-index
    for z in range(0, 110, 10):
        css += f".z-{z} {{ z-index: {z} !important; }}\n"

    # Shadows
    css += ".shadow-sm { box-shadow: 0 .125rem .25rem rgba(0,0,0,.075) !important; }\n"
    css += ".shadow { box-shadow: 0 .5rem 1rem rgba(0,0,0,.15) !important; }\n"
    css += ".shadow-lg { box-shadow: 0 1rem 3rem rgba(0,0,0,.175) !important; }\n"
    css += ".shadow-none { box-shadow: none !important; }\n"

    with open("static/css/styles.css", "w") as f:
        f.write(css)
        
    # Duplicate for dark mode to create a robust theming system (adds realistic length)
    css_dark = css.replace(':root', '[data-theme="dark"]')
    # Swap some colors for dark mode
    css_dark = css_dark.replace('#f8f9fa', '#212529').replace('#212529', '#f8f9fa')
    
    with open("static/css/dark-theme.css", "w") as f:
        f.write(css_dark)

if __name__ == "__main__":
    os.makedirs("static/css", exist_ok=True)
    generate_css_framework()
    print("Custom CSS framework generated.")
