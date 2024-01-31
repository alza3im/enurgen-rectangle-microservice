# Rectangular Shape Microservice

This microservice accepts PNG files, processes the images to extract rectangular shapes, and returns the result in a JSON format containing unique IDs and coordinates of the rectangle corners.

## Requirements

- Python (>= 3.6)
- Flask (>= 2.0.2)
- OpenCV (>= 4.5.3.56)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/alza3im/enurgen-rectangle-microservice.git
    ```

2. Change into the project directory:

    ```bash
    cd enurgen-rectangle-microservice
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Microservice

1. Run the microservice using Python:

    ```bash
    python app.py
    ```

    The service will be accessible at [http://localhost:5000/extract-rect-coords](http://localhost:5000/extract-rect-coords).

2. To test the service, use a tool like `curl` or Postman to send a POST request with a PNG file to [http://localhost:5000/extract-rect-coords](http://localhost:5000/extract-rect-coords).

    Example using `curl`:

    ```bash
    curl -X POST -F "image=@/path/to/your/image.png" http://localhost:5000/extract-rect-coords
    ```

## Docker Containerization (Optional Bonus)

1. Build the Docker image:

    ```bash
    docker build -t rectangle-microservice .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 5000:5000 rectangle-microservice
    ```

    The service will be accessible at [http://localhost:5000/extract-rect-coords](http://localhost:5000/extract-rect-coords).

## Sample Result

The microservice will return a JSON response with unique IDs and coordinates of the rectangle corners.

```json
[
    {
        "id": 0,
        "coordinates": [
            [10, 50],
            [50, 50],
            [10, 100],
            [50, 100]
        ]
    },
    {
        "id": 1,
        "coordinates": [
            // Coordinates of another rectangle
        ]
    }
]
