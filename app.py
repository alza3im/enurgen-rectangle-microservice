from flask import Flask, request, jsonify
import cv2
import numpy as np
import os

app = Flask(__name__)


def find_rectangles(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve rectangle detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detector to find edges in the image
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(
        edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    rectangles = []

    # Loop over the contours
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check if the polygon has 4 corners (rectangle)
        if len(approx) == 4:
            # Get the rectangle ID and corner vertices
            rect_id = len(rectangles) + 1
            rect_vertices = approx.reshape(-1, 2)

            rectangles.append({"id": rect_id, "vertices": rect_vertices.tolist()})

    return rectangles


# Flask endpoint
@app.route("/extract-rect-coords", methods=["POST"])
def detect_rectangles():
    # Check if the request contains a file
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files["image"]

    # Check if the file has an allowed extension (you can customize this list)
    allowed_extensions = {"png", "jpg", "jpeg", "gif"}
    if (
        "." not in image_file.filename
        or image_file.filename.split(".")[-1].lower() not in allowed_extensions
    ):
        return jsonify({"error": "Invalid file format"}), 400

    # Save the uploaded image temporarily
    temp_path = "temp_image.jpg"
    image_file.save(temp_path)

    # Call the rectangle detection function
    rectangles = find_rectangles(temp_path)

    # Remove the temporary image file
    os.remove(temp_path)

    return jsonify({"rectangles": rectangles})


if __name__ == "__main__":
    app.run(port=5004)
