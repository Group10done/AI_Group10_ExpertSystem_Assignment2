from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to recommend a destination based on interest
def recommend_destination(interest):
    interest = interest.lower()
    recommendations = {
        "wildlife": "Akagera National Park - Explore Rwanda's rich wildlife.",
        "culture": "Kigali Genocide Memorial - Experience Rwanda's cultural history.",
        "adventure": "Nyungwe Canopy Walk - Enjoy an adventurous walk above the forest.",
        "relaxation": "Lake Kivu - Relax by the beautiful lakeside beaches.",
        "eco-tourism": "Volcanoes National Park - Discover Rwanda's ecological wonders."
    }
    return recommendations.get(interest, "No specific recommendation found. Try another interest.")

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# API route for getting recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    interest = data.get("interest", "")
    recommendation = recommend_destination(interest)
    return jsonify({"recommendation": recommendation})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

