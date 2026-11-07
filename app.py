
import os

from flask import Flask, jsonify, render_template_string, request

import target

app = Flask(__name__)

FUNCTIONS = [
    "is_adult", "celsius_to_fahrenheit", "count_vowels",
    "invert", "greet", "find_max", "get_price", "swap",
    "common_items", "is_leap_year", "to_int", "divide",
    "power", "square_root", "factorial", "average"
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Functional Testing App</title>
    <style>
        body {
            font-family: Arial;
            max-width: 700px;
            margin: 50px auto;
        }

        input, select, button {
            padding: 10px;
            margin: 8px 0;
            width: 100%;
        }

        button {
            background: #1769aa;
            color: white;
            border: 0;
            cursor: pointer;
        }

        pre {
            background: #eee;
            padding: 15px;
            white-space: pre-wrap;
        }

        #deployment-info {
            background: #e8f5e9;
            padding: 12px;
            border-radius: 5px;
            overflow-wrap: anywhere;
        }
    </style>
</head>
<body>
    <h1>Functional Testing App</h1>

    <p>Choose a function and enter arguments as JSON.</p>

    <!-- Deployment information -->
    <p id="deployment-info">Checking deployment...</p>

    <select id="function">
        {% for name in functions %}
        <option value="{{ name }}">{{ name }}</option>
        {% endfor %}
    </select>

    <input id="args" value="[]" placeholder='Arguments, e.g. [25]'>
    <input id="kwargs" value="{}" placeholder='Keyword arguments, e.g. {}'>

    <button onclick="runFunction()">Run Function</button>

    <h3>Result</h3>
    <pre id="result">Your result will appear here.</pre>

    <script>
    // Existing function: Run a Python function
    async function runFunction() {
        const result = document.getElementById("result");

        try {
            const response = await fetch("/run", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    name: document.getElementById("function").value,
                    args: JSON.parse(document.getElementById("args").value),
                    kwargs: JSON.parse(document.getElementById("kwargs").value)
                })
            });

            const data = await response.json();
            result.textContent = JSON.stringify(data, null, 2);

        } catch (error) {
            result.textContent = "Error: " + error.message;
        }
    }

    // New function: Display deployment information
    async function showDeploymentInfo() {
        const info = document.getElementById("deployment-info");

        try {
            const response = await fetch("/health");

            if (!response.ok) {
                throw new Error("Health check failed");
            }

            const data = await response.json();

            info.textContent =
                "Deployment Status: " + data.status +
                " | Deployed Commit: " + data.commit;

        } catch (error) {
            info.textContent =
                "Could not load deployment information.";
        }
    }

    // Load deployment information when the page opens
    showDeploymentInfo();
    </script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML, functions=FUNCTIONS)


@app.route("/run", methods=["POST"])
def run_function():
    try:
        data = request.get_json()
        name = data.get("name")
        args = data.get("args", [])
        kwargs = data.get("kwargs", {})

        if name not in FUNCTIONS:
            return jsonify({"error": "Unknown function"}), 400

        if not isinstance(args, list) or not isinstance(kwargs, dict):
            return jsonify({"error": "Invalid arguments format"}), 400

        # Convert JSON lists into Python sets for common_items
        if name == "common_items":
            args = [set(args[0]), set(args[1])]

        result = getattr(target, name)(*args, **kwargs)

        # Convert Python set into a JSON-compatible list
        if isinstance(result, set):
            result = sorted(result)

        return jsonify({
            "success": True,
            "result": result,
            "result_type": type(result).__name__
        })

    except (ValueError, TypeError, ZeroDivisionError, OverflowError, AttributeError) as error:
        return jsonify({
            "success": False,
            "error": str(error),
            "error_type": type(error).__name__
        }), 400


@app.route("/health")
def health():
    commit = (
        os.environ.get("RENDER_GIT_COMMIT")
        or os.environ.get("GITHUB_SHA")
        or "local"
    )

    return jsonify({
        "status": "ok",
        "commit": commit
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "5000"))
    )