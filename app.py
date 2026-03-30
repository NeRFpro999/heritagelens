from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from monument import Monument
from pipeline import process_images, generate_point_cloud

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Temporary upload folder
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        country = request.form['country']
        year_built = int(request.form['year_built'])
        description = request.form.get('description', '')

        # Handle file uploads
        files = request.files.getlist('images')
        if len(files) < 3:
            return "Please upload at least 3 images."

        image_paths = []
        for file in files:
            if file and file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                image_paths.append(filepath)

        # Create Monument
        monument = Monument(name, country, year_built, image_paths, description)

        # Save to JSON and get output dir
        output_dir = monument.save_to_json()

        # Process images
        processed_paths = process_images(image_paths, output_dir)

        # Generate point cloud
        ply_path = generate_point_cloud(image_paths, output_dir)

        # Clean up temp uploads
        for path in image_paths:
            os.remove(path)

        # Success message with link
        return f"Monument '{name}' processed successfully! <a href='/outputs/{name.replace(' ', '_')}'>View outputs</a>"

    return render_template('index.html')

@app.route('/outputs/<path:filename>')
def outputs(filename):
    return f"Output folder: {filename}"  # Simple, in real app serve files

if __name__ == '__main__':
    app.run(debug=True)