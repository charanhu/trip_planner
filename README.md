# Trip Planner

Trip Planner is a Python application that uses AI agents to help plan your trips based on your origin, interests, and date range. The application interacts with Watsonx services to provide tailored travel recommendations.

## Features

- Selects cities based on your preferences
- Gathers local information and activities
- Plans travel itineraries

## Prerequisites

- Python 3.11 or later
- Access to Watsonx API

## Installation

### Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/charanhu/trip_planner.git
cd trip_planner
```

### Create a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
```

### Activate the Virtual Environment

Activate the virtual environment:

- **On Windows:**

  ```bash
  .\venv\Scripts\activate
  ```

- **On macOS and Linux:**

  ```bash
  source venv/bin/activate
  ```

### Install Requirements

Install the required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Create Environment Variables

Create a `.env` file in the root directory and add the following variables with your Watsonx API credentials:

```env
WATSONX_API=<your_watsonx_api_key>
WATSONX_URL=<your_watsonx_api_url>
WATSONX_PID=<your_watsonx_project_id>
```

## Usage

To run the application, navigate to the `src` directory and execute the `main.py` script:

```bash
cd src
python main.py
```

Follow the prompts to enter your travel preferences and receive your customized trip plan.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### Explanation

- **Project Overview**: Provides a brief description of what the project does.
- **Prerequisites**: Lists the software and tools needed to run the application.
- **Installation Steps**: Provides step-by-step instructions to set up the environment, including cloning the repository, creating and activating a virtual environment, installing dependencies, and setting up environment variables.
- **Usage**: Explains how to run the application.
- **Contributing and License**: Provides information on how to contribute and the project's license.

This `README.md` provides clear instructions for setting up and running the Trip Planner application. Adjust the placeholders in the `.env` file section with your actual Watsonx API credentials.