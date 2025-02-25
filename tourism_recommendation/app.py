from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    interest = data.get("interest", "")
    recommendation = recommend_destination(interest)
    return jsonify({"recommendation": recommendation})

if __name__ == '__main__':
    app.run(debug=True)
