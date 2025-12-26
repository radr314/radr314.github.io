import flask
import os
from flask import Flask, jsonify, render_template_string
html="""
<select id="jobDropdown">
  <option disabled selected>Loading jobs...</option>
</select>

<script>
  // Make the API call when the page loads
  fetch("/api/jobs")  // <-- your API endpoint
    .then(response => response.json())
    .then(data => {
      const dropdown = document.getElementById("jobDropdown");
      dropdown.innerHTML = ""; // clear default option
      
      data.forEach(job => {
        const option = document.createElement("option");
        option.value = job.id;      // value assigned to option
        option.textContent = job.name; // visible text
        dropdown.appendChild(option);
      });
    })
    .catch(err => {
      console.error("Error fetching jobs:", err);
    });
</script>
"""

app=Flask(__name__)

@app.route('/api/jobs')
def get_jobs():
    jobs = [
        {"id": 1, "name": "Daily Report Job"},
        {"id": 2, "name": "Analytics Pipeline"},
        {"id": 3, "name": "Backup Job"}
    ]
    return jsonify(jobs)

@app.route("/",methods=["GET"])
def home():
  return render_template_string(html)


if __name__=="__main__":
  app.run(debug=False)